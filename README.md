# Number Classification API

## Overview
The **Number Classification API** is a FastAPI-based service that takes a number as input and returns interesting mathematical properties about it, along with a fun fact fetched from the Numbers API.

## Features
- Classifies a given number as **prime, perfect, Armstrong, odd, or even**.
- Computes the **sum of its digits**.
- Fetches a **fun fact** about the number from the Numbers API.
- Returns responses in **JSON format**.
- Handles **error cases** appropriately.
- Deployed to a **publicly accessible endpoint**.

## API Specification
### Endpoint:
```
GET /api/classify-number?number=<integer>
```

### Sample Response (200 OK)
```json
{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,
    "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}
```

### Error Response (400 Bad Request)
```json
{
    "error": "Invalid input. Please provide a valid integer."
}
```

## Project Structure
```
number-classification-api/
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI application
│   ├── utils.py             # Helper functions (e.g., is_prime, is_armstrong, etc.)
│   └── schemas.py           # Pydantic models
├── requirements.txt         # List of dependencies
├── README.md                # Project documentation
└── start.sh                 # Script to run the application
```

## Installation & Setup
### Prerequisites
- Python 3.8+
- Virtual environment (recommended)

### Steps
1. Clone the repository:
   ```sh
   git clone <repo-url>
   cd number-classification-api
   ```
2. Create and activate a virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Run the application:
   ```sh
   bash start.sh
   ```
   The API will be accessible at: `http://127.0.0.1:8000/api/classify-number?number=371`

## Deployment
- Deploy the API to a publicly accessible server.
- Ensure CORS is properly handled.
- API should have a **fast response time (<500ms)**.


## Resources
- Fun fact API: [Numbers API](http://numbersapi.com/#42)
- [Parity in Mathematics](https://en.wikipedia.org/wiki/Parity_(mathematics))

