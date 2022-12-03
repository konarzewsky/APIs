import uvicorn

from config.env import ENVIRONMENT

if __name__ == "__main__":
    uvicorn.run(
        "graphql_api.app:app",
        host="0.0.0.0",
        port=8000,
        log_level="info",
        reload=ENVIRONMENT == "development",
    )
