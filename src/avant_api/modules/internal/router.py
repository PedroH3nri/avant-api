"""Junta os controllers do painel interno num único router."""

from fastapi import APIRouter

from avant_api.modules.internal.client_documents.controller import router as client_documents
from avant_api.modules.internal.client_notes.controller import router as client_notes
from avant_api.modules.internal.clients.controller import router as clients
from avant_api.modules.internal.commissions.controller import router as commissions
from avant_api.modules.internal.contracts.controller import router as contracts
from avant_api.modules.internal.dashboard_templates.controller import router as dashboard_templates
from avant_api.modules.internal.goals.controller import router as goals
from avant_api.modules.internal.inventory.controller import router as inventory
from avant_api.modules.internal.invoices.controller import router as invoices
from avant_api.modules.internal.mcm.controller import router as mcm
from avant_api.modules.internal.people.controller import router as people
from avant_api.modules.internal.results.controller import router as results
from avant_api.modules.internal.staff.controller import router as staff
from avant_api.modules.internal.tasks.controller import router as tasks
from avant_api.modules.internal.views.controller import router as views

router = APIRouter()
for child in (
    clients,
    client_documents,
    client_notes,
    people,
    staff,
    mcm,
    results,
    contracts,
    goals,
    commissions,
    invoices,
    views,
    dashboard_templates,
    inventory,
    tasks,
):
    router.include_router(child)
