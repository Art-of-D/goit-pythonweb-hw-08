from fastapi import FastAPI

from src.app.routes import contacts

app = FastAPI()

app.include_router(contacts.router, prefix="/api")


if __name__ == "__main__":
    print("Start app")
    