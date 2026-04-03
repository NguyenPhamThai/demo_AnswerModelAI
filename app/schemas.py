from pydantic import BaseModel, Field


class GenerateRequest(BaseModel):
    prompt: str = Field(..., min_length=1, description="The input prompt for text generation")


class GenerateResponse(BaseModel):
    input: str = Field(..., description="The original input prompt")
    response: str = Field(..., description="The generated text response")


class HealthResponse(BaseModel):
    status: str = Field(..., description="The health status of the service")
