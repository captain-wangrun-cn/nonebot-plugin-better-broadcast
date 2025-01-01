from pydantic import BaseModel

class Config(BaseModel):
    bc_blacklist: list = []
