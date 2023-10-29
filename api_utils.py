from fastapi import Security, HTTPException
from fastapi.security import APIKeyQuery, APIKeyHeader
from starlette.status import HTTP_403_FORBIDDEN
import os
import hashutil

API_KEY_NAME = "api_key"
API_KEY_DATA_HASH = os.getenv("API_KEY_DATA_HASH")

api_key_query_data = APIKeyQuery(name=API_KEY_NAME, auto_error=False)
api_key_header_data = APIKeyHeader(name=API_KEY_NAME, auto_error=False)


async def get_api_key_data(
    api_key_query: str = Security(api_key_query_data),
    api_key_header: str = Security(api_key_header_data),
):

    if api_key_query and hashutil.hash_key(api_key_query) == API_KEY_DATA_HASH:
        return api_key_query
    elif api_key_header and hashutil.hash_key(api_key_header) == API_KEY_DATA_HASH:
        return api_key_query
    else:
        raise HTTPException(
            status_code=HTTP_403_FORBIDDEN,
            detail="Incorrect API Key. Do you have access to the stock ticks api?",
        )
