from fastapi import FastAPI
from routes.faces import router
import uvicorn

app = FastAPI(
    title="Bio-Face Service",
    description="API de reconhecimento facial para autenticação biométrica.",
    version="0.0.1"
)


app.include_router(router)

@app.get("/")
async def root():
    return {"message": "Bio-Face Service is running."}

@app.get('/health')
async def health_check():
    return {"status": "ok"}    


def run():
    uvicorn.run('service:app', host='0.0.0.0', port=8000, reload=True)
