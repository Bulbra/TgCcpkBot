from pydantic import BaseModel, ConfigDict

class Station(BaseModel):
    code: str
    name: str
    nameEn: str

    model_config = ConfigDict(extra='ignore')
