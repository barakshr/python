from pydantic import BaseModel


class Junk(BaseModel):
    name: str
    age: int | None = None
