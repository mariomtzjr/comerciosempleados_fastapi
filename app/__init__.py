from fastapi import FastAPI, Depends


def create_app():
    app = FastAPI(
        title="Dapp FastAPI Example",
        description="Dapp FastAPI Example",
        version="1.0.0",
    )
    
    return app