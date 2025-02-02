from fastapi import FastAPI, Query, HTTPException
import requests
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from typing import List, Union
from .utils import is_prime, is_perfect, is_armstrong, digit_sum
from .schemas import NumberResponse, ErrorResponse

app = FastAPI()

# Fun Fact API URL
FUN_FACT_API_URL = "http://numbersapi.com/{}/math?json"

@app.get("/api/classify-number", response_model=NumberResponse)
async def classify_number(number: Union[int, float, str] = Query(..., description="The number to classify")):
    try:
        # Convert the input to a float first (to handle both integers and floating-point numbers)
        number_float = float(number)
        # If the input is a whole number, convert it to an integer
        number_int = int(number_float) if number_float.is_integer() else number_float
    except (ValueError, TypeError):
        # If the input cannot be converted to a number, return a 400 Bad Request
        raise HTTPException(status_code=400, detail={"number": str(number), "error": True})

    # Get fun fact
    response = requests.get(FUN_FACT_API_URL.format(number_int if isinstance(number_int, int) else number_float))
    fun_fact = response.json().get("text", "No fun fact available.")

    # Determine properties
    properties: List[str] = []
    if isinstance(number_int, int):
        if number_int >= 0:  # Only check for prime, perfect, and Armstrong for non-negative integers
            if is_prime(number_int):
                properties.append("prime")
            if is_perfect(number_int):
                properties.append("perfect")
            if is_armstrong(number_int):
                properties.append("armstrong")
        if number_int % 2 == 0:
            properties.append("even")
        else:
            properties.append("odd")
    else:
        # Floating-point numbers have no properties
        pass

    return {
        "number": number_int if isinstance(number_int, int) else number_float,
        "is_prime": is_prime(number_int) if isinstance(number_int, int) else False,
        "is_perfect": is_perfect(number_int) if isinstance(number_int, int) else False,
        "properties": properties,
        "digit_sum": digit_sum(number_int) if isinstance(number_int, int) else None,
        "fun_fact": fun_fact
    }

@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse(status_code=exc.status_code, content=exc.detail)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)