from hmac import compare_digest
from typing import Optional

from fastapi import Header, HTTPException

from config.env import API_AUTH_TOKEN


async def verify_auth_token(auth_token: Optional[str] = Header(None)):
    if not auth_token:
        raise HTTPException(status_code=400, detail="Auth-Token header not provided")
    elif not (
        compare_digest(auth_token, API_AUTH_TOKEN) and auth_token == API_AUTH_TOKEN
    ):
        raise HTTPException(status_code=401, detail="Auth-Token header invalid")
