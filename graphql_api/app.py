import strawberry
from fastapi import Depends, FastAPI
from strawberry.fastapi import GraphQLRouter

from graphql_api.dependencies import verify_auth_token
from graphql_api.extensions import dbSessionExtension
from graphql_api.graphql.mutation import Mutation
from graphql_api.graphql.query import Query

app = FastAPI()


schema = strawberry.Schema(
    query=Query,
    mutation=Mutation,
    extensions=[dbSessionExtension],
)

app.include_router(
    GraphQLRouter(schema),
    prefix="/graphql",
    dependencies=[Depends(verify_auth_token)],
)


@app.get("/")
def root():
    return {"message": "GraphQL api - Welcome!"}
