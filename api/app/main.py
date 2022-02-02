import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from starlette.responses import RedirectResponse

from app.v1.routes import test as test_v1

tags_metadata = [
    {
        "name": "Test",
        "description": "",
    }
]

app = FastAPI(
    title="Api",
    openapi_tags=tags_metadata,
    version="0.0.0",
    docs_url="/api/docs",
    redoc_url="/api/redoc",
    openapi_url="/api/openapi.json",
)


app.include_router(
    test_v1.router,
    prefix="/api",
    tags=["Test"],
    responses={
        400: {"description": "Bad Request"},
        401: {"description": "Unauthorized"},
        404: {"description": "Not Found"},
        500: {"description": "Internal Server Error"},
    },
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(GZipMiddleware, minimum_size=1024 * 1000)


@app.get("/api")
async def main():
    response = RedirectResponse(url="api/docs")
    return response


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=6069, reload=True, workers=1)
