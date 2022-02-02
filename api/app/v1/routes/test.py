from typing import Dict

from fastapi import APIRouter, Body, Query, Request, Response, status

from app.v1.models import Message, Result, Status

router = APIRouter()

STATUS_MAP: Dict[Status, int] = {
    Status.OK: status.HTTP_200_OK,
    Status.ERROR: status.HTTP_500_INTERNAL_SERVER_ERROR,
    Status.FAIL: status.HTTP_400_BAD_REQUEST,
}


@router.get("/check", response_model=Result, tags=["Test"])
async def check(*, request: Request, response: Response) -> Result:
    return Result(status=Status.OK)


@router.get("/check-status", response_model=Result, tags=["Test"])
async def check_status(
    *, status_info: Status = Query(Status.OK), request: Request, response: Response
) -> Result:
    response.status_code = STATUS_MAP[status_info]
    return Result(status=status_info)


@router.post("/message", response_model=Message, tags=["Test"])
async def send_message(
    *, message: Message = Body(..., embed=False), request: Request, response: Response
) -> Result:
    return message
