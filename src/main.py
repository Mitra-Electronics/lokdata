from fastapi import FastAPI
import src.accounts.router as arouter

app = FastAPI()
app.include_router(arouter.app, prefix="/accounts")


@app.get("/registe")
def register():
    return "Hello World"
