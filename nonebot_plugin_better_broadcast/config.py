from pydantic import BaseModel

class Config(BaseModel):
    bc_blacklist: list = []
    bc_random_delay: bool = True
