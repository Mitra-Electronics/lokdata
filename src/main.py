from fastapi import FastAPI
import src.accounts.router as arouter

app = FastAPI()
app.include_router(arouter.app)


@app.get("/register")
def register():
    return "Hello World"
