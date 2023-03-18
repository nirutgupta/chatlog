from fastapi import FastAPI


app = FastAPI(
    title="Chatlog Service",
    description="Manage user chatlogs",
    docs_url="/v1/chatlogs",
    openapi_url="/v1/chatlogs/openapi.json"
)
