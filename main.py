from fastapi import FastAPI
from ArraysAndHashing.ContainsDuplicate_217 import contains_duplicate
from ArraysAndHashing.ValidAnagram_242 import is_anagram
from typing import List
from fastapi import Body


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/217")
def check_contains_duplicate(nums: List[int]):
    result = contains_duplicate(nums)
    return {"nums": nums, "contains_duplicate": result}

@app.post("/242")
def check_valid_anagram(s: str = Body(str), t: str = Body(str)):
    return {"is_anagram": is_anagram(s, t)}
    
