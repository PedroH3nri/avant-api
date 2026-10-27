"""Grupos de funcionários da Empresa ativa: /api/v1/groups."""

import uuid

from avant_core.company.service import Actor
from fastapi import APIRouter, Depends, status

from avant_api.app.security import require
from avant_api.modules.groups.dependencies import group_service
from avant_api.modules.groups.dto import GroupIn, GroupMembersIn, GroupOut, GroupPatchIn
from avant_api.modules.groups.service import GroupService
from avant_api.shared.dto import ItemsOut

router = APIRouter(prefix="/groups", tags=["groups"])


@router.get("")
def index(
    actor: Actor = Depends(require("groups.view")),
    service: GroupService = Depends(group_service),
) -> ItemsOut[GroupOut]:
    """Lista os grupos da Empresa ativa com as pessoas de cada um."""
    return ItemsOut(items=service.list_all(actor))


@router.post("", status_code=status.HTTP_201_CREATED)
def create(
    body: GroupIn,
    actor: Actor = Depends(require("groups.manage")),
    service: GroupService = Depends(group_service),
) -> GroupOut:
    """Cria um grupo com pelo menos uma pessoa."""
    return service.create(actor, body)


@router.get("/{group_id}")
def show(
    group_id: uuid.UUID,
    actor: Actor = Depends(require("groups.view")),
    service: GroupService = Depends(group_service),
) -> GroupOut:
    """Mostra um grupo com as pessoas dele."""
    return service.detail(actor, group_id)


@router.patch("/{group_id}")
def edit(
    group_id: uuid.UUID,
    body: GroupPatchIn,
    actor: Actor = Depends(require("groups.manage")),
    service: GroupService = Depends(group_service),
) -> GroupOut:
    """Troca o nome e a descrição do grupo."""
    return service.update(actor, group_id, body)


@router.delete("/{group_id}", status_code=status.HTTP_204_NO_CONTENT)
def remove(
    group_id: uuid.UUID,
    actor: Actor = Depends(require("groups.manage")),
    service: GroupService = Depends(group_service),
) -> None:
    """Exclui o grupo, ativo ou inativo."""
    service.delete(actor, group_id)


@router.post("/{group_id}/members")
def add_members(
    group_id: uuid.UUID,
    body: GroupMembersIn,
    actor: Actor = Depends(require("groups.manage")),
    service: GroupService = Depends(group_service),
) -> GroupOut:
    """Põe pessoas que ainda não têm grupo no grupo."""
    return service.add_members(actor, group_id, body)


@router.delete("/{group_id}/members/{membership_id}")
def remove_member(
    group_id: uuid.UUID,
    membership_id: uuid.UUID,
    actor: Actor = Depends(require("groups.manage")),
    service: GroupService = Depends(group_service),
) -> GroupOut:
    """Tira uma pessoa do grupo; a última pessoa não sai (409)."""
    return service.remove_member(actor, group_id, membership_id)
