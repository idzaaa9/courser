import uuid
from sqlmodel import Field, SQLModel

from models import register_model

@register_model
class Course(SQLModel, table=True, extra="ignore"):
    id: uuid.UUID = Field(
            primary_key=True,
            index=True,
            nullable=False,
            description="Primary key as UUID4, generated by the backend, not the db"
            )
    uni_id: int = Field(
            ...,
            foreign_key="university.id"
            )
    is_summer: bool = Field(...)
    name: str = Field(
            ...,
            min_length=1
            )
    ects: int = Field(
            ...,
            ge=1
            )
