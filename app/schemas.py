from typing import List, Union
from pydantic import BaseModel

class NumberResponse(BaseModel):
    number: Union[int, float]
    is_prime: bool
    is_perfect: bool
    properties: List[str]
    digit_sum: Union[int, None]
    fun_fact: str

class ErrorResponse(BaseModel):
    number: str
    error: bool