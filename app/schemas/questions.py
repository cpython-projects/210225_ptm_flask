from pydantic import BaseModel, field_validator, Field


class QuestionCreate(BaseModel):
    question: str = Field(..., min_length=10, max_length=100)


class QuestionResponse(BaseModel):
    id: int
    question: str = Field(..., min_length=10, max_length=100)

    class Config:
        orm_mode = True
        from_attributes = True


class MessageResponse(BaseModel):
    message: str
