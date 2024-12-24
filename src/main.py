from fastapi import FastAPI
import src.accounts.router as arouter
import src.survey.router as srouter

app = FastAPI()
app.include_router(arouter.app, prefix="/accounts")
app.include_router(srouter.app, prefix="/surveys")


@app.get("/status")
def status():
    return {"status":200}
