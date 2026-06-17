from pydantic import BaseModel


class ComfortOption(BaseModel):
    key: str
    name: str
    description: str
    latinDescription: str
