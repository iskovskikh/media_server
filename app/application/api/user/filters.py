from pydantic import BaseModel

from infrastructure.repositories.filters.user import GetUsersFilters as GetUsersInfraFilters


class GetUsersFilters(BaseModel):
    limit: int = 10
    offset: int = 0

    def to_infra(self):
        return GetUsersInfraFilters(
            limit=self.limit,
            offset=self.offset
        )
