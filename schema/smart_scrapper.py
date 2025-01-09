from pydantic import BaseModel
from typing import Optional


class HomePageScrapperIn(BaseModel):
    url: str
    openai_key: str
    model: Optional[str] = "gpt-4o"


class HomePageScrapperOut(BaseModel):
    industry: str
    company_size: str
    location: str

    class Config:
        from_attributes = True
