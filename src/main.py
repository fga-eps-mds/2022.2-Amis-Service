from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer
from fastapi.responses import JSONResponse
import requests

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
from .assistentes.router import router as assistentes_router
from .alunas.router import router as aluna_router
from .turmas.router import router as turma_router
from .matricula.router import router as matricula_router
from .receita.router import router as receita_router

app.include_router(aluna_router)
app.include_router(turma_router)
app.include_router(assistentes_router)
app.include_router(matricula_router)
app.include_router(receita_router)

endpoint = ("https://auth-amis.azurewebsites.net/login/token")

whiteList = {"/alunas/count/formada", "/alunas/count/", "/docs", "/openapi.json","/receita/"}

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    print("middleware verificar token")
    if str(request.url.path) in whiteList:
        return await call_next(request)

    auth_token = request.headers.get('Authorization')

    if (auth_token):
        bearer_token: str = auth_token.split('Bearer')[1].strip()
        headers = {"Authorization": "Bearer " + bearer_token}
        
        token_validado = requests.get(endpoint, None, headers = headers).json()

        if (token_validado.get("detail")):
            status_code_request = token_validado.get("detail").get("status_code")
            detail_request = token_validado.get("detail").get("response")

            if(status_code_request == int(401)):
                return JSONResponse(content = detail_request, status_code = status_code_request)
    else:
        return JSONResponse(content = "Token é necessário", status_code = 401)

    response = await call_next(request)
    return response

@app.get('/')
async def hello_world():
    return {
        "db_type": settings.db_type,
        "db_url": settings.db_url,
    }
