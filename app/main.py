from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import logging
from app.model import load_model, generate_text
from app.schemas import GenerateRequest, GenerateResponse, HealthResponse
from app.utils import clean_generated_text

# Create FastAPI app
app = FastAPI(
    title="FastAPI Hugging Face Chatbot",
    description="A simple chatbot API using GPT-2 for text generation",
    version="1.0.0"
)

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Load the model on startup
@app.on_event("startup")
async def startup_event():
    load_model()


@app.get("/", summary="API Description")
async def root():
    """
    Return a short description of the API.
    """
    return {"message": "FastAPI Chatbot API with GPT-2 text generation"}


@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    return FileResponse("static/favicon.ico")


@app.get("/health", response_model=HealthResponse, summary="Health Check")
async def health():
    """
    Return the health status of the system.
    """
    return HealthResponse(status="ok")


@app.post("/generate", response_model=GenerateResponse, summary="Generate Text")
async def generate(request: GenerateRequest):
    """
    Generate text based on the input prompt.

    - **prompt**: The input prompt for text generation (must not be empty)
    """
    logger.info(f"Received generate request: {request}")
    try:
        # Generate the response
        raw_response = generate_text(request.prompt)

        # Clean the response
        cleaned_response = clean_generated_text(raw_response)

        # Return the response
        return GenerateResponse(
            input=request.prompt,
            response=cleaned_response
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating text: {str(e)}")
