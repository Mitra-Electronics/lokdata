from fastapi import FastAPI
import src.password.router as prouter

app = FastAPI()
app.include_router(prouter.app)


@app.get("/register")
def register():
    return "Hello World"
