"""PDF da invoice, em inglês como no Genius: De GROONE, LLC para o funcionário, as linhas e
o total. Fonte DejaVu Sans no pacote (licença em fonts/LICENSE), para o travessão e os acentos dos nomes."""

from decimal import Decimal
from pathlib import Path

from avant_core.company.services.client_profile_rules import TAX_TYPES
from avant_core.invoices.enums import InvoiceStatus
from avant_core.invoices.models import InvoiceView
from fpdf import FPDF

from avant_api.modules.internal.commissions.dto import dollars

FONTS = Path(__file__).parent / "fonts"
FONT = "DejaVu"
INK = (23, 23, 23)
MUTED = (115, 115, 115)
RULE = (229, 229, 229)
PAYER = (
    "GROONE, LLC",
    "EIN 30-1462306",
    "1191 E Newport Center Dr 103",
    "Deerfield Beach, FL 33442",
)
STATUS = {
    InvoiceStatus.DRAFT: "Draft",
    InvoiceStatus.ISSUED: "Issued",
    InvoiceStatus.PAID: "Paid",
}


def money(amount: Decimal) -> str:
    """Dólares com sinal, separador de milhar e duas casas, como US$ no Genius."""
    sign = "-" if amount < 0 else ""
    return f"{sign}US$ {abs(amount):,.2f}"


def render_invoice(view: InvoiceView) -> bytes:
    """Monta o PDF de uma página A4 com o cabeçalho, as partes, as linhas e o pagamento."""
    pdf = FPDF(format="A4", unit="mm")
    pdf.set_margins(18, 18, 18)
    pdf.set_auto_page_break(auto=True, margin=22)
    pdf.add_font(FONT, "", str(FONTS / "DejaVuSans.ttf"))
    pdf.add_font(FONT, "B", str(FONTS / "DejaVuSans-Bold.ttf"))
    pdf.set_title(f"Invoice {view.invoice.number}")
    pdf.set_author("Groone Avant")
    pdf.add_page()
    _header(pdf, view)
    _parties(pdf, view)
    _items(pdf, view)
    _payment(pdf, view)
    _footer(pdf)
    return bytes(pdf.output())


def _logo(pdf: FPDF, left: float, top: float, size: float) -> None:
    """O logo do Avant: o quadrado escuro com o A sem travessão e o ponto no lugar dele."""
    scale = size / 32
    pdf.set_fill_color(*INK)
    pdf.rect(left, top, size, size, style="F", round_corners=True, corner_radius=7.2 * scale)
    pdf.set_draw_color(255, 255, 255)
    pdf.set_line_width(3.4 * 0.78 * scale)

    def point(across: float, down: float) -> tuple[float, float]:
        """Converte um ponto do desenho de 32 unidades para a página."""
        return left + (3.52 + across * 0.78) * scale, top + (3.52 + down * 0.78) * scale

    pdf.polyline([point(7, 25), point(16, 7.5), point(25, 25)])
    pdf.set_fill_color(255, 255, 255)
    center_x, center_y = point(16, 19.4)
    radius = 2.5 * 0.78 * scale
    pdf.ellipse(center_x - radius, center_y - radius, radius * 2, radius * 2, style="F")


def _header(pdf: FPDF, view: InvoiceView) -> None:
    """Logo e marca à esquerda; número e situação da invoice à direita."""
    top = pdf.get_y()
    _logo(pdf, pdf.l_margin, top, 9)
    pdf.set_xy(pdf.l_margin + 12, top + 1.5)
    pdf.set_font(FONT, "B", 15)
    pdf.set_text_color(*INK)
    pdf.cell(40, 6, "Avant")
    pdf.set_xy(pdf.l_margin, top)
    pdf.set_font(FONT, "", 8)
    pdf.set_text_color(*MUTED)
    pdf.cell(0, 4, "INVOICE", align="R", new_x="LMARGIN", new_y="NEXT")
    pdf.set_font(FONT, "B", 12)
    pdf.set_text_color(*INK)
    pdf.cell(0, 6, view.invoice.number, align="R", new_x="LMARGIN", new_y="NEXT")
    pdf.set_font(FONT, "", 9)
    pdf.set_text_color(*MUTED)
    pdf.cell(0, 5, STATUS[view.invoice.status], align="R", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(8)


def _parties(pdf: FPDF, view: InvoiceView) -> None:
    """Três colunas: De (a GroOne), Para (o funcionário) e as datas."""
    invoice = view.invoice
    payee = invoice.payee or {}
    width = (pdf.w - pdf.l_margin - pdf.r_margin) / 3
    top = pdf.get_y()
    document = TAX_TYPES.get(payee.get("tax_type", ""), payee.get("tax_type", ""))
    payee_lines = (
        [
            payee.get("legal_name", ""),
            f"{document} {payee.get('tax_id', '')}".strip(),
            payee.get("billing_address", ""),
            f"+{payee.get('billing_phone_ddi', '')} {payee.get('billing_phone', '')}",
        ]
        if payee
        else [view.owner.name, "Payment details are added when the invoice is issued."]
    )
    if view.role_name:
        payee_lines.insert(1, view.role_name)
    dates = [
        ("Period", invoice.month.strftime("%B %Y")),
        ("Created", invoice.created_at.strftime("%m/%d/%Y")),
        ("Issued", invoice.issued_at.strftime("%m/%d/%Y") if invoice.issued_at else "-"),
        ("Paid", invoice.paid_at.strftime("%m/%d/%Y") if invoice.paid_at else "-"),
    ]
    bottoms = [
        _block(pdf, pdf.l_margin, top, width - 4, "FROM", list(PAYER)),
        _block(pdf, pdf.l_margin + width, top, width - 4, "BILL TO · PAYEE", payee_lines),
        _dates(pdf, pdf.l_margin + width * 2, top, width, dates),
    ]
    pdf.set_y(max(bottoms) + 8)


def _block(pdf: FPDF, left: float, top: float, width: float, label: str, lines: list[str]) -> float:
    """Um bloco com o rótulo, a primeira linha em negrito e as outras em cinza."""
    pdf.set_xy(left, top)
    pdf.set_font(FONT, "", 7.5)
    pdf.set_text_color(*MUTED)
    pdf.cell(width, 4, label, new_x="LEFT", new_y="NEXT")
    pdf.ln(1)
    for index, line in enumerate(lines):
        pdf.set_x(left)
        pdf.set_font(FONT, "B" if index == 0 else "", 9.5 if index == 0 else 9)
        pdf.set_text_color(*(INK if index == 0 else MUTED))
        pdf.multi_cell(width, 4.6, line, align="L", new_x="LEFT", new_y="NEXT")
    return pdf.get_y()


def _dates(pdf: FPDF, left: float, top: float, width: float, dates: list[tuple[str, str]]) -> float:
    """As datas da invoice, rótulo à esquerda e valor à direita."""
    pdf.set_xy(left, top + 5)
    for label, value in dates:
        pdf.set_x(left)
        pdf.set_font(FONT, "", 9)
        pdf.set_text_color(*MUTED)
        pdf.cell(width / 2, 5, label)
        pdf.set_text_color(*INK)
        pdf.cell(width / 2, 5, value, align="R", new_x="LEFT", new_y="NEXT")
        pdf.set_x(left)
    return pdf.get_y()


def _items(pdf: FPDF, view: InvoiceView) -> None:
    """A tabela de serviços: título e descrição à esquerda, valor à direita, e o total."""
    width = pdf.w - pdf.l_margin - pdf.r_margin
    amount_width = 34
    _line(pdf)
    pdf.set_font(FONT, "", 8)
    pdf.set_text_color(*MUTED)
    pdf.cell(width - amount_width, 7, "Services")
    pdf.cell(amount_width, 7, "Amount", align="R", new_x="LMARGIN", new_y="NEXT")
    _line(pdf)
    for item in view.items:
        top = pdf.get_y() + 2.5
        pdf.set_xy(pdf.l_margin, top)
        pdf.set_font(FONT, "B", 9.5)
        pdf.set_text_color(*INK)
        pdf.multi_cell(
            width - amount_width - 4, 5, item.title, align="L", new_x="LMARGIN", new_y="NEXT"
        )
        if item.description:
            pdf.set_font(FONT, "", 8.5)
            pdf.set_text_color(*MUTED)
            pdf.multi_cell(
                width - amount_width - 4,
                4.4,
                item.description,
                align="L",
                new_x="LMARGIN",
                new_y="NEXT",
            )
        bottom = pdf.get_y()
        pdf.set_xy(pdf.l_margin + width - amount_width, top)
        pdf.set_font(FONT, "", 9.5)
        pdf.set_text_color(*INK)
        pdf.cell(amount_width, 5, money(dollars(item.amount_micros)), align="R")
        pdf.set_y(bottom + 2.5)
        _line(pdf)
    pdf.ln(3)
    pdf.set_font(FONT, "B", 10)
    pdf.cell(width - amount_width, 8, "Total")
    pdf.set_font(FONT, "B", 14)
    pdf.cell(
        amount_width, 8, money(dollars(view.total_micros)), align="R", new_x="LMARGIN", new_y="NEXT"
    )
    pdf.ln(6)


def _payment(pdf: FPDF, view: InvoiceView) -> None:
    """Os dados bancários copiados na emissão; em rascunho não há o que mostrar."""
    payee = view.invoice.payee
    if not payee:
        return
    width = pdf.w - pdf.l_margin - pdf.r_margin
    pdf.set_fill_color(245, 245, 245)
    pdf.set_font(FONT, "B", 9)
    pdf.set_text_color(*INK)
    pdf.cell(width, 7, "  Payment details", fill=True, new_x="LMARGIN", new_y="NEXT")
    pdf.set_font(FONT, "", 9)
    pdf.set_text_color(*MUTED)
    details = (
        f"  {payee['bank_name']} · SWIFT {payee['swift_code']} · Account "
        f"{payee['account_number']} · Routing {payee['routing_number']}"
    )
    pdf.multi_cell(width, 6, details, align="L", fill=True, new_x="LMARGIN", new_y="NEXT")


def _footer(pdf: FPDF) -> None:
    """A marca d'água do rodapé: o logo pequeno e "Avant by GroOne"."""
    pdf.set_auto_page_break(auto=False)
    pdf.set_y(-18)
    width = pdf.w - pdf.l_margin - pdf.r_margin
    center = pdf.l_margin + width / 2
    _logo(pdf, center - 15, pdf.get_y() + 0.5, 4)
    pdf.set_xy(center - 10, pdf.get_y())
    pdf.set_font(FONT, "", 8)
    pdf.set_text_color(*MUTED)
    pdf.cell(30, 5, "Avant by GroOne")


def _line(pdf: FPDF) -> None:
    """Uma linha fina de separação na largura do conteúdo."""
    pdf.set_draw_color(*RULE)
    pdf.set_line_width(0.2)
    pdf.line(pdf.l_margin, pdf.get_y(), pdf.w - pdf.r_margin, pdf.get_y())
