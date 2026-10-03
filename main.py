import uvicorn
from fastapi import FastAPI, status

app = FastAPI(
    title="FastAPI Fundamentals",
    description="This Project is all about learning FastAPI fundamentals"
                "route design, "
                "coding practice with proper examples",
    version="1.0.0"
)


@app.get("/",
         summary="Get API Welcome Message",
         description="Returns a welcome message to verify that API is running.!",
         status_code=status.HTTP_200_OK,
         tags=["General"]
         )
async def hello():
    return {"message": "Hello, World"}


@app.get("/health-check",
         summary="Check API Health",
         description="Checks whether the FastAPI application instance is running.",
         status_code=status.HTTP_200_OK,
         tags=["Health"]
         )
async def health_check():
    return {"message": "FastAPI instance is connected"}


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
             reload=True,
    )
