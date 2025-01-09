from pydantic import BaseModel, HttpUrl, model_validator
from typing import Optional


class HomePageScrapperIn(BaseModel):
    url: HttpUrl
    openai_key: str
    model: Optional[str] = "gpt-4o"

    @model_validator(mode="after")
    def validate_fields(self):

        if not self.openai_key or self.openai_key.strip() == "":
            raise ValueError("The 'openai_key' field must be a non-empty string.")

        if not self.url:
            raise ValueError("The 'url' field must be a valid URL.")

        allowed_models = ["gpt-4o", "gpt-3.5", "gpt-4"]  # Example allowed models
        if self.model and self.model not in allowed_models:
            raise ValueError(f"The 'model' field must be one of {allowed_models}.")

        return self


class HomePageScrapperOut(BaseModel):
    industry: str
    company_size: str
    location: str

    class Config:
        from_attributes = True
