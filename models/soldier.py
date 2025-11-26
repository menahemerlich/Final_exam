from sqlmodel import SQLModel, Field
from typing import Optional

class Soldier(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    personal_number: str
    First_name: str
    Last_name: str
    sex: str
    City: str
    Distance: str





