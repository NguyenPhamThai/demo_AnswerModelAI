# Information of Student who created this project
Student id: 24120396
FUll name: Phạm Thái Nguyên
Class: 24CTT5

# FastAPI Hugging Face Chatbot

A simple FastAPI application that integrates a Hugging Face GPT-2 model for text generation, functioning as a mini chatbot.

## Features

- RESTful API with FastAPI
- Text generation using GPT-2 model from Hugging Face Transformers
- Input validation with Pydantic
- Health check endpoint
- Clean architecture with separated concerns

## Model

This application uses the **GPT-2** model for text generation. The model is loaded once at startup and reused for all requests.

## Setup Instructions

1. **Clone or navigate to the project directory**

2. **Create a virtual environment (recommended)**
   ```bash
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Web Interface

A simple web page is provided to test the API directly in your browser without using command line tools.

- **Access the web interface:** `http://localhost:8000/static/index.html`
- Features:
  - Input prompt and generate text
  - Real-time feedback for errors (validation, connection issues)
  - Clean, responsive design

## How to Run the Server

1. **Start the FastAPI server**
   ```bash
   uvicorn app.main:app --reload
   ```

   The server will start on `http://localhost:8000`

2. **Access the API documentation**
   - Swagger UI: `http://localhost:8000/docs`
   - ReDoc: `http://localhost:8000/redoc`

## API Usage

### Endpoints

#### GET /
Returns a description of the API.

**Response:**
```json
{
  "message": "FastAPI Chatbot API with GPT-2 text generation"
}
```

#### GET /health
Returns the health status of the system.

**Response:**
```json
{
  "status": "ok"
}
```

#### POST /generate
Generates text based on the input prompt.

**Request:**
```json
{
  "prompt": "Tell me a joke"
}
```

**Response:**
```json
{
  "input": "Tell me a joke",
  "response": "Why don't scientists trust atoms? Because they make up everything!"
}
```

### Example Usage with curl

```bash
curl -X POST "http://localhost:8000/generate" \
     -H "Content-Type: application/json" \
     -d '{"prompt": "Write a short poem about coding"}'
```

## Testing

Run the test script to verify the API is working:

```bash
python tests/test_api.py
```

This will send a POST request to the `/generate` endpoint and print the response.

## Project Structure

```
fastapi-huggingface-demo/
│
├── app/
│   ├── main.py          # FastAPI app and routes
│   ├── model.py         # Model loading and inference
│   ├── schemas.py       # Pydantic models
│   └── utils.py         # Utility functions
│
├── tests/
│   └── test_api.py      # API test script
│
├── notebooks/
│   └── experiment.ipynb # Optional experimentation notebook
│
├── requirements.txt     # Python dependencies
├── README.md           # This file
└── .gitignore          # Git ignore file
```

## Dependencies

- **fastapi**: Web framework for building APIs
- **uvicorn**: ASGI server for running FastAPI
- **transformers**: Hugging Face transformers library
- **torch**: PyTorch (required for transformers)
- **pydantic**: Data validation
- **requests**: HTTP library for testing

## Notes

- The GPT-2 model is loaded into memory on startup, which may take a few seconds
- Text generation parameters are set to reasonable defaults but can be adjusted in `model.py`
- The model runs on CPU by default; change `device=-1` to `device=0` in `model.py` for GPU usage (if available)
## Demo Youtube
- https://youtu.be/XYRE4ztpkvs