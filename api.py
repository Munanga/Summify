from fastapi import FastAPI, Depends
from fastapi.security.api_key import APIKey
from api_utils import get_api_key_data
from pydantic import BaseModel
from summify.summify import gpt_summarize
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(docs_url=None, redoc_url=None, openapi_url=None)

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class RequestData(BaseModel):
    text: str


@app.post("/summarize")
async def earnings_dates_snapshot(request_data: RequestData, api_key: APIKey = Depends(get_api_key_data)):
    text_input = request_data.text
    summarized_text = gpt_summarize(text_input)
    return {"summary": summarized_text}


@app.get("/")
async def earnings_dates_snapshot(api_key: APIKey = Depends(get_api_key_data)):
    return {"status": "OK!"}
