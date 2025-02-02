from fastapi import FastAPI, Query, HTTPException
import requests
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from typing import List  # Import List from typing
from .utils import is_prime, is_perfect, is_armstrong, digit_sum
from .schemas import NumberResponse, ErrorResponse

app = FastAPI()

# Fun Fact API URL
FUN_FACT_API_URL = "http://numbersapi.com/{}/math?json"

@app.get("/api/classify-number", response_model=NumberResponse)
async def classify_number(number: str = Query(..., description="The number to classify")):
    try:
        number_int = int(number)
    except ValueError:
        raise HTTPException(status_code=400, detail={"number": number, "error": True})

    # Get fun fact
    response = requests.get(FUN_FACT_API_URL.format(number_int))
    fun_fact = response.json().get("text", "No fun fact available.")

    # Determine properties
    properties: List[str] = []  # Use List[str] instead of list[str]
    if is_armstrong(number_int):
        properties.append("armstrong")
    if number_int % 2 == 0:
        properties.append("even")
    else:
        properties.append("odd")

    return {
        "number": number_int,
        "is_prime": is_prime(number_int),
        "is_perfect": is_perfect(number_int),
        "properties": properties,
        "digit_sum": digit_sum(number_int),
        "fun_fact": fun_fact
    }

@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse(status_code=exc.status_code, content=exc.detail)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)