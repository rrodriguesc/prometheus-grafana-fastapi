from enum import Enum

from pydantic.main import BaseModel


class Status(Enum):
    OK: str = "ok"
    FAIL: str = "fail"
    ERROR: str = "error"


class Result(BaseModel):
    status: Status


class Message(BaseModel):
    user: str
    message: str
