"""DTOs do login com Google."""

from pydantic import BaseModel


class GoogleStatusOut(BaseModel):
    # A Groone configurou o cliente OAuth.
    available: bool
    linked: bool
