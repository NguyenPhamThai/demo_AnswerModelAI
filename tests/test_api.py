import requests

# Base URL of the API (adjust if running on different host/port)
BASE_URL = "http://localhost:8000"

def test_generate_endpoint():
    """
    Test the /generate endpoint by sending a POST request.
    """
    url = f"{BASE_URL}/generate"
    payload = {
        "prompt": "Tell me a joke"
    }

    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()  # Raise an exception for bad status codes

        data = response.json()
        print("Request successful!")
        print(f"Input: {data['input']}")
        print(f"Response: {data['response']}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    test_generate_endpoint()
