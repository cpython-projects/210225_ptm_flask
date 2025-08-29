from pydantic import BaseModel, Field, ConfigDict


class QuestionCreate(BaseModel):
    question: str = Field(..., min_length=10, max_length=100)


class QuestionResponse(BaseModel):
    id: int
    question: str = Field(..., min_length=10, max_length=100)

    model_config = ConfigDict(
        from_attributes=True
    )


class MessageResponse(BaseModel):
    message: str
