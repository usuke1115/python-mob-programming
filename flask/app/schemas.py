
from pydantic import BaseModel, ConfigDict, HttpUrl


class ShortenUrlRequestModel(BaseModel):
    original_url: HttpUrl
    keyword: str | None


class CreateUrlModel(BaseModel):
    original_url: str
    shortened_url: str


class UrlResponseModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    original_url: str
    shortened_url: str
