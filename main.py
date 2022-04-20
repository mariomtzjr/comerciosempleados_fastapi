from fastapi import FastAPI

app = FastAPI(
    title="Dapp FastAPI Example",
    description="Dapp FastAPI Example",
    version="1.0.0",
)

@app.get("/")
async def get_root():
    return {"message": "Hello World"}