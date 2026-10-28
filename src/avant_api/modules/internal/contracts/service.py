"""Service dos contratos de revshare no painel interno."""

import uuid

from avant_core.access.models import Actor
from avant_core.gam.contracts.enums import ContractStatus
from avant_core.internal.services import (
    create_contract,
    delete_contract,
    end_contract,
    get_contract,
    list_contract_networks,
    list_contracts,
    update_contract,
)
from avant_core.shared.clock import Clock

from avant_api.app.ports import UnitOfWorkFactory
from avant_api.modules.internal.contracts.dto import (
    ContractIn,
    ContractNetworkOut,
    ContractOut,
    ContractPatchIn,
)


class ContractService:
    """Contratos das networks: o revshare de um contrato nunca muda."""

    def __init__(self, uows: UnitOfWorkFactory, clock: Clock) -> None:
        self._uows = uows
        self._clock = clock

    def list_all(
        self,
        actor: Actor,
        company_id: uuid.UUID | None,
        network_id: uuid.UUID | None,
        status: ContractStatus | None,
    ) -> list[ContractOut]:
        """Os contratos, do mais novo para o mais antigo, com filtros."""
        views = list_contracts(
            self._uows.trusted_uow(),
            actor=actor,
            company_id=company_id,
            network_id=network_id,
            status=status,
        )
        return [ContractOut.of(view) for view in views]

    def networks(self, actor: Actor) -> list[ContractNetworkOut]:
        """Networks MCM ativas com o contrato em vigor e se aceitam contrato à mão."""
        views = list_contract_networks(self._uows.trusted_uow(), actor=actor)
        return [ContractNetworkOut.of(view) for view in views]

    def show(self, actor: Actor, contract_id: uuid.UUID) -> ContractOut:
        """Um contrato."""
        return ContractOut.of(
            get_contract(self._uows.trusted_uow(), actor=actor, contract_id=contract_id)
        )

    def create(self, actor: Actor, body: ContractIn) -> ContractOut:
        """Contrato à mão de uma network Manage Inventory; encerra o ativo, se houver."""
        view = create_contract(
            self._uows.trusted_uow(),
            actor=actor,
            network_id=body.network_id,
            revshare=body.revshare,
            notes=body.notes,
            clock=self._clock,
        )
        return ContractOut.of(view)

    def update(self, actor: Actor, contract_id: uuid.UUID, body: ContractPatchIn) -> ContractOut:
        """Edita a observação do contrato."""
        view = update_contract(
            self._uows.trusted_uow(),
            actor=actor,
            contract_id=contract_id,
            notes=body.notes,
            clock=self._clock,
        )
        return ContractOut.of(view)

    def end(self, actor: Actor, contract_id: uuid.UUID) -> ContractOut:
        """Encerra um contrato feito à mão."""
        view = end_contract(
            self._uows.trusted_uow(), actor=actor, contract_id=contract_id, clock=self._clock
        )
        return ContractOut.of(view)

    def delete(self, actor: Actor, contract_id: uuid.UUID) -> None:
        """Exclui um contrato feito à mão (cadastro errado)."""
        delete_contract(
            self._uows.trusted_uow(), actor=actor, contract_id=contract_id, clock=self._clock
        )
