"""Junta os controllers do painel interno num único router."""

from fastapi import APIRouter

from avant_api.modules.internal.clients.controller import router as clients
from avant_api.modules.internal.contracts.controller import router as contracts
from avant_api.modules.internal.goals.controller import router as goals
from avant_api.modules.internal.mcm.controller import router as mcm
from avant_api.modules.internal.people.controller import router as people
from avant_api.modules.internal.results.controller import router as results
from avant_api.modules.internal.staff.controller import router as staff

router = APIRouter()
for child in (clients, people, staff, mcm, results, contracts, goals):
    router.include_router(child)
