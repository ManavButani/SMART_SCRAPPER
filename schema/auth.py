from pydantic import BaseModel
from typing import Optional


# Token schema used when the token is issued
class Token(BaseModel):
    access_token: str
    token_type: str


# TokenData schema used when decoding a JWT token
class TokenData(BaseModel):
    username: Optional[str] = None
