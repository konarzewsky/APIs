import strawberry
from fastapi import Depends, FastAPI, Request
from fastapi.responses import HTMLResponse, RedirectResponse, Response
from graphql_api.extensions import dbSessionExtension
from strawberry.fastapi import GraphQLRouter
from graphql_api.graphql import Mutation, Query
from graphql_api.dependencies import verify_auth_token


app = FastAPI()


schema = strawberry.Schema(
    query=Query,
    mutation=Mutation,
    extensions=[dbSessionExtension],
)

app.include_router(
    GraphQLRouter(schema),
    prefix="/graphql",
    dependencies=[Depends(verify_token_header)],
)

@app.get("/")
def root():
    return {"message": "GraphQL api - Welcome!"}
