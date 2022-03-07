from typing import List, Optional
from pydantic import BaseModel

class Script(BaseModel):
    name: str
    command: Optional[str]

class ScriptParams(BaseModel):
    params: List[str]

class ScriptList(BaseModel):
    scripts: List[str]

class ScriptRegistration(BaseModel):
    name: str
    ip: str

class ScriptResult(BaseModel):
    name: str
    result: str
