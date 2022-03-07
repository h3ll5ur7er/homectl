#! /usr/bin/env python3
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.routing import APIRoute
from fastapi.staticfiles import StaticFiles
from subprocess import check_output, check_call
try:
    from .dto import *
except ImportError:
    from dto import *
try:
    from .config import SCRIPTS
except ImportError:
    from config import SCRIPTS

app = FastAPI()
frontend = FastAPI()
backend = FastAPI()


try:
    # SPA routing
    @frontend.middleware("http")
    async def add_custom_header(request, call_next):
        response = await call_next(request)
        if response.status_code == 404:
            return FileResponse('frontend/dist/homectl/index.html')
        return response
    @frontend.exception_handler(404)
    def not_found(request, exc):
        return FileResponse('frontend/dist/homectl/index.html')

    # Static files
    frontend.mount('/', StaticFiles(directory='frontend/dist/homectl'))
except RuntimeError:
    pass

@backend.get("/call/{name}", response_model=Script)
def readScript(name: str):
    return SCRIPTS.get(name, Script(name=name, command=None))

@backend.post("/call/{name}", response_model=ScriptResult)
def runScript(name: str, params: ScriptParams):
    print(f"running script {name} with params ({', '.join(params.params)})")
    cmd = SCRIPTS.get(name, Script(name=name, command="echo unknown script")).command.split(' ') + params.params
    print("cmd: ", cmd)
    output = check_output(cmd)
    return ScriptResult(name=name, result=output.decode('utf-8'))

@backend.get("/call", response_model=ScriptList)
def listScripts():
    return ScriptList(scripts=list(SCRIPTS.keys()))



for route in backend.routes:
    if isinstance(route, APIRoute):
        route.operation_id = route.name

app.mount('/api', app=backend)
app.mount('/', app=frontend)

def serve(
        host_ip: str = "0.0.0.0",
        host_port: int = 8001):
    import uvicorn
    uvicorn.run(app, host=host_ip, port=host_port)

def generate_api_definition(file_name: str):
    from fastapi.openapi.utils import get_openapi
    import json
    with open(file_name, 'w') as f:
        json.dump(get_openapi(
            title=backend.title,
            version=backend.version,
            openapi_version=backend.openapi_version,
            description=backend.description,
            routes=backend.routes
        ), f)


if __name__ == "__main__":
    from sys import argv
    _, command, *args = argv
    default_action = lambda *a, **kw: print("Unknown command: {}".format(command))
    {
        "serve": serve,
        "generate": generate_api_definition
    }.get(command, default_action)(*args)

