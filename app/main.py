import uvicorn
from ariadne import QueryType, make_executable_schema, load_schema_from_path, snake_case_fallback_resolvers
from ariadne.asgi import GraphQL
from fastapi import FastAPI
from api.queries import query
from api.mutations import mutation

type_defs = load_schema_from_path("graphql/schemas/schema.graphql")

app = FastAPI(
    title="ScrapAD",
    description="ScrapAD is a web scraping API",
    version="0.0.1",
    docs_url="/",
)

resolvers = [mutation, query]

schema = make_executable_schema(type_defs, resolvers)
graphql = GraphQL(schema, debug=True)
schema = make_executable_schema(type_defs, query)
app.mount("/", graphql)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, loop="asyncio")