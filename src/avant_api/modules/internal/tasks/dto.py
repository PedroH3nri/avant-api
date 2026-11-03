"""DTOs das tarefas de suporte no painel interno."""

import uuid
from datetime import datetime

from avant_core.company.models import Company
from avant_core.gam.inventory.models import Site
from avant_core.gam.networks.models import Network
from avant_core.identity.models import User
from avant_core.support_tasks.enums import TaskEventKind, TaskPriority, TaskStatus
from avant_core.support_tasks.models import TaskDetail, TaskEventView, TaskInput, TaskView
from avant_core.support_tasks.services import TaskChange
from pydantic import BaseModel, Field


class TaskPersonOut(BaseModel):
    id: uuid.UUID
    name: str

    @classmethod
    def of(cls, user: User | None) -> "TaskPersonOut | None":
        """Nome da pessoa; vazio se ela foi apagada."""
        return cls(id=user.id, name=user.name) if user else None


class TaskClientOut(BaseModel):
    id: uuid.UUID
    name: str

    @classmethod
    def of(cls, company: Company | None) -> "TaskClientOut | None":
        """O cliente da tarefa."""
        return cls(id=company.id, name=company.name) if company else None


class TaskNetworkOut(BaseModel):
    id: uuid.UUID
    network_code: str
    name: str | None

    @classmethod
    def of(cls, network: Network | None) -> "TaskNetworkOut | None":
        """A network da tarefa."""
        if network is None:
            return None
        return cls(id=network.id, network_code=network.network_code, name=network.display_name)


class TaskSiteOut(BaseModel):
    id: uuid.UUID
    domain: str

    @classmethod
    def of(cls, site: Site | None) -> "TaskSiteOut | None":
        """O site da tarefa."""
        return cls(id=site.id, domain=site.domain) if site else None


class TaskOut(BaseModel):
    id: uuid.UUID
    subject: str
    description: str
    priority: TaskPriority
    status: TaskStatus
    creator: TaskPersonOut | None
    assignee: TaskPersonOut | None
    client: TaskClientOut | None
    network: TaskNetworkOut | None
    site: TaskSiteOut | None
    domain: str | None
    created_at: datetime
    updated_at: datetime
    editable: bool

    @classmethod
    def of(cls, view: TaskView) -> "TaskOut":
        """Monta a tarefa com as pessoas, o cliente, a network e o site."""
        task = view.task
        return cls(
            id=task.id,
            subject=task.subject,
            description=task.description,
            priority=task.priority,
            status=task.status,
            creator=TaskPersonOut.of(view.creator),
            assignee=TaskPersonOut.of(view.assignee),
            client=TaskClientOut.of(view.client),
            network=TaskNetworkOut.of(view.network),
            site=TaskSiteOut.of(view.site),
            domain=task.domain,
            created_at=task.created_at,
            updated_at=task.updated_at,
            editable=view.editable,
        )


class TaskEventOut(BaseModel):
    id: uuid.UUID
    kind: TaskEventKind
    author: TaskPersonOut | None
    created_at: datetime
    message: str | None
    old_value: str | None
    new_value: str | None
    old_user: TaskPersonOut | None
    new_user: TaskPersonOut | None

    @classmethod
    def of(cls, item: TaskEventView) -> "TaskEventOut":
        """Monta um item da linha do tempo; nas mudanças de responsável, as duas pessoas."""
        event = item.event
        return cls(
            id=event.id,
            kind=event.kind,
            author=TaskPersonOut.of(item.author),
            created_at=event.created_at,
            message=event.message,
            old_value=event.old_value,
            new_value=event.new_value,
            old_user=TaskPersonOut.of(item.old_user),
            new_user=TaskPersonOut.of(item.new_user),
        )


class TaskDetailOut(TaskOut):
    events: list[TaskEventOut]

    @classmethod
    def of_detail(cls, detail: TaskDetail) -> "TaskDetailOut":
        """Monta a tarefa com a linha do tempo, da mais antiga para a mais nova."""
        return cls(
            **TaskOut.of(detail.view).model_dump(),
            events=[TaskEventOut.of(item) for item in detail.events],
        )


class TaskDataIn(BaseModel):
    subject: str = Field(min_length=1, max_length=1000)
    description: str = Field(default="", max_length=10000)
    priority: TaskPriority = TaskPriority.NORMAL
    client_id: uuid.UUID | None = None
    network_id: uuid.UUID | None = None
    site_id: uuid.UUID | None = None
    domain: str | None = Field(default=None, max_length=255)

    def to_input(self, assignee_id: uuid.UUID | None = None) -> TaskInput:
        """Os dados no formato do caso de uso."""
        return TaskInput(
            subject=self.subject,
            description=self.description,
            priority=self.priority,
            client_id=self.client_id,
            network_id=self.network_id,
            site_id=self.site_id,
            domain=self.domain or None,
            assignee_id=assignee_id,
        )


class TaskIn(TaskDataIn):
    assignee_id: uuid.UUID | None = None


class TaskPatchIn(BaseModel):
    """Mudança numa tarefa: ``assignee_id`` null tira o responsável e ausente mantém."""

    status: TaskStatus | None = None
    priority: TaskPriority | None = None
    assignee_id: uuid.UUID | None = None
    data: TaskDataIn | None = None

    def to_change(self) -> TaskChange:
        """A mudança no formato do caso de uso."""
        unassign = "assignee_id" in self.model_fields_set and self.assignee_id is None
        return TaskChange(
            status=self.status,
            priority=self.priority,
            assignee_id=self.assignee_id,
            unassign=unassign,
            data=self.data.to_input() if self.data else None,
        )


class TaskCommentIn(BaseModel):
    message: str = Field(min_length=1, max_length=2000)
