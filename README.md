# 2022.2-Amis-Service

## Como rodar:

### Usando python:

Vamos rodar usando o virtual enviroment do python para ajudar a rodar alguns comandos
```sh
python3 -m venv venv
```

Para ativar esse ambiente vitual rode o seguinte comando na raiz do repositório
```
source venv/bin/activate
```

Em seguida é necessário instalar as dependencias
```
pip install -r requirements.txt
```

Por fim, para colocar a api em funcionamento, rode:
```
uvicorn src.main:app --reload
```

### Usando docker

A única dependencia para rodar nessa maneira é o docker. PAra rodar apenas use o docker compose
```
docker compose up --build
```

Ps: Algumas máquinas precisam rodar o comando acima com permissão de root, nesse caso apenas adicione o `sudo` ao começo do comando
Ps2: Versões mais antigas do docker compose, ainda tem o hifen. Nesse caso apenas adicione o hifen entre docker e compose ficando `docker-compose`

## Analise estática de código:

Para fazer a analize do código (lint), inicie a venv e após rode o seguinte comando:
```
pylint src/*
```