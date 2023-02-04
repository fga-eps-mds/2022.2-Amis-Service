from fastapi import FastAPI, Request, HTTPException, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import requests
from .config import settings

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

whiteList = {"/alunas/count/formada", "/alunas/count/", "/docs", "/openapi.json","/receita/", "/testeLogin"}

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    print("middleware verificar token")
    if str(request.url.path) in whiteList or str(request.url.path).find('receita') != -1:
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


def form_body(cls):
    cls.__signature__ = cls.__signature__.replace(
        parameters=[
            arg.replace(default=Form(...))
            for arg in cls.__signature__.parameters.values()
        ]
    )
    return cls

@form_body
class Item(BaseModel):
    username: str
    password: str

@app.get('/testeLogin')
async def test():
    endpoint = ("https://auth-amis.azurewebsites.net/login/")
     
    token_validado = requests.post(endpoint, data={"username": settings.user_name, "password": settings.password})
    token = token_validado.json()
    return token['access_token']


@app.get('/')
async def hello_world():
    return {
        "status":'online'
    }
