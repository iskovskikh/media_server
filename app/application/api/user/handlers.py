from fastapi import HTTPException, Depends
from fastapi import status
from fastapi.routing import APIRouter
from punq import Container

from application.api.schemas import ErrorSchema
from application.api.user.filters import GetUsersFilters
from application.api.user.schema import GetUsersQueryResponseSchema, UserDetailSchema, EditUserResponseSchema
from domain.exceptions.base import ApplicationException
from logic.init import init_container
from logic.mediator import Mediator
from logic.queries.user import GetUsersQuery

router = APIRouter(
    tags=['Users']
)


@router.get(
    '/',
    status_code=status.HTTP_200_OK,
    description='Получить всех пользователей',
    responses={
        status.HTTP_200_OK: {'model': GetUsersQueryResponseSchema},
        status.HTTP_400_BAD_REQUEST: {'model': ErrorSchema}
    }
)
async def get_user_list_handler(
        filters: GetUsersFilters = Depends(),
        container: Container = Depends(init_container)
) -> GetUsersQueryResponseSchema:
    mediator: Mediator = container.resolve(Mediator)

    try:
        user_list, count = await mediator.handle_query(GetUsersQuery(filters=filters.to_infra()))
    except ApplicationException as exception:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail={'error': exception.message})

    return GetUsersQueryResponseSchema(
        count=count,
        limit=filters.limit,
        offset=filters.offset,
        items=[UserDetailSchema.from_entity(user) for user in user_list]
    )


async def update_user_handler(
        container: Container = Depends(init_container)
) -> EditUserResponseSchema:
    ...
