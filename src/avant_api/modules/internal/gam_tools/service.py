"""Service das ferramentas do GAM no painel interno.

Usa ``trusted_uow()`` (sem RLS) porque as execuções são só do painel interno e as networks
são de várias Empresas; o core confere ``ensure_staff`` e as permissões
``internal.gam_tools.view`` e ``internal.gam_tools.run``. A execução roda no worker
(``avant.gam.run_tool``), que escreve no GAM.
"""

import io
import uuid
import zipfile

from avant_core.access.models import Actor
from avant_core.gam.tools.services import (
    gam_install_files,
    get_ads_txt,
    get_gam_tool_network,
    get_gam_tool_run,
    page_gam_tool_networks,
    page_gam_tool_runs,
    start_gam_tool,
)
from avant_core.identity.models import User
from avant_core.shared.clock import Clock

from avant_api.app.ports import UnitOfWorkFactory
from avant_api.app.tasks import RUN_GAM_TOOL, TaskQueue
from avant_api.modules.internal.gam_tools.dto import (
    AdsTxtOut,
    GamToolNetworkDetailOut,
    GamToolNetworkOut,
    GamToolRunIn,
    GamToolRunOut,
)
from avant_api.shared.dto import PageOut, page_out


class GamToolService:
    """Networks, execuções, ads.txt e o arquivo de instalação das ferramentas do GAM."""

    def __init__(
        self, uows: UnitOfWorkFactory, clock: Clock, tasks: TaskQueue, groone_network_code: str
    ) -> None:
        self._uows = uows
        self._clock = clock
        self._tasks = tasks
        self._groone_network_code = groone_network_code

    def networks(self, actor: Actor, query: str | None, page: int) -> PageOut[GamToolNetworkOut]:
        """Uma página das networks dos clientes."""
        found = page_gam_tool_networks(
            self._uows.trusted_uow(), actor=actor, query=query, page=page
        )
        return page_out(found, GamToolNetworkOut.of)

    def network(self, actor: Actor, network_id: uuid.UUID) -> GamToolNetworkDetailOut:
        """A network com os sites e os blocos de cada um."""
        view = get_gam_tool_network(self._uows.trusted_uow(), actor=actor, network_id=network_id)
        return GamToolNetworkDetailOut.of_detail(view)

    def runs(self, actor: Actor, network_id: uuid.UUID, page: int) -> PageOut[GamToolRunOut]:
        """Uma página das execuções da network."""
        found = page_gam_tool_runs(
            self._uows.trusted_uow(), actor=actor, network_id=network_id, page=page
        )
        people = self._people({run.requested_by for run in found.items})
        return page_out(found, lambda run: GamToolRunOut.of(run, people))

    def run(self, actor: Actor, run_id: uuid.UUID) -> GamToolRunOut:
        """Uma execução com os passos."""
        found = get_gam_tool_run(self._uows.trusted_uow(), actor=actor, run_id=run_id)
        return GamToolRunOut.of(found, self._people({found.requested_by}))

    def start(self, actor: Actor, body: GamToolRunIn) -> GamToolRunOut:
        """Abre a execução e enfileira no worker."""
        run = start_gam_tool(
            self._uows.trusted_uow(),
            actor=actor,
            network_id=body.network_id,
            kind=body.kind,
            clock=self._clock,
            domains=body.domains,
            block_format=body.format,
        )
        self._tasks.send(RUN_GAM_TOOL, str(run.id))
        return GamToolRunOut.of(run, self._people({run.requested_by}))

    def ads_txt(self, actor: Actor, network_id: uuid.UUID) -> AdsTxtOut:
        """As linhas do ads.txt da network."""
        return AdsTxtOut(
            lines=get_ads_txt(self._uows.trusted_uow(), actor=actor, network_id=network_id)
        )

    def install(
        self,
        actor: Actor,
        network_id: uuid.UUID,
        domains: list[str],
        language: str,
        label_language: str,
    ) -> tuple[str, bytes, str]:
        """O arquivo de instalação: o .txt de um site ou um .zip com um .txt por site."""
        files = gam_install_files(
            self._uows.trusted_uow(),
            actor=actor,
            network_id=network_id,
            domains=domains,
            language=language,
            label_language=label_language,
            groone_network_code=self._groone_network_code,
        )
        if len(files) == 1:
            return files[0].name, files[0].content.encode("utf-8"), "text/plain; charset=utf-8"
        buffer = io.BytesIO()
        with zipfile.ZipFile(buffer, "w", zipfile.ZIP_DEFLATED) as archive:
            for file in files:
                archive.writestr(file.name, file.content)
        return "blocos.zip", buffer.getvalue(), "application/zip"

    def _people(self, user_ids: set[uuid.UUID]) -> dict[uuid.UUID, User]:
        """As pessoas que pediram as execuções, pelo id."""
        with self._uows.trusted_uow() as uow:
            found = (uow.users.get(user_id) for user_id in user_ids)
            return {user.id: user for user in found if user is not None}
