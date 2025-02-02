from fastapi import FastAPI, Query, HTTPException
import requests
from pydantic import BaseModel
from fastapi.responses import JSONResponse

app = FastAPI()

# Fun Fact API URL
FUN_FACT_API_URL = "http://numbersapi.com/{}/math?json"

class NumberResponse(BaseModel):
    number: int
    is_prime: bool
    is_perfect: bool
    properties: list[str]
    digit_sum: int
    fun_fact: str

class ErrorResponse(BaseModel):
    number: str
    error: bool

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n: int) -> bool:
    if n < 2:
        return False
    sum_divisors = 1
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            sum_divisors += i
            if i != n // i:
                sum_divisors += n // i
    return sum_divisors == n

def is_armstrong(n: int) -> bool:
    digits = [int(d) for d in str(n)]
    num_digits = len(digits)
    return sum(d ** num_digits for d in digits) == n

def digit_sum(n: int) -> int:
    return sum(int(d) for d in str(n))

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
    properties = []
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

