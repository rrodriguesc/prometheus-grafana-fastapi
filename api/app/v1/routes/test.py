from fastapi import APIRouter, Body, Query, Request, Response

from app.v1.models import Message, Result, Status

router = APIRouter()


@router.get("/check", response_model=Result, tags=["Test"])
async def check(*, request: Request, response: Response) -> Result:
    return Result(status=Status.OK)


@router.get("/check-status", response_model=Result, tags=["Test"])
async def check_status(
    *, status: Status = Query(Status.OK), request: Request, response: Response
) -> Result:
    return Result(status=status)


@router.post("/message", response_model=Message, tags=["Test"])
async def send_message(
    *, message: Message = Body(..., embed=False), request: Request, response: Response
) -> Result:
    return message
