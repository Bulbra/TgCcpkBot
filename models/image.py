from pydantic import BaseModel
from typing import Optional


class Image(BaseModel):
    title: Optional[str] = None
    alt: Optional[str] = None
    url: str
