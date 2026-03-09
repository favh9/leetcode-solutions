from fastapi import FastAPI
from ArraysAndHashing.ContainsDuplicate_217 import contains_duplicate
from typing import List

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/contains-duplicate-217")
def check_contains_duplicate(nums: List[int]):
    result = contains_duplicate(nums)
    return {"nums": nums, "contains_duplicate": result}
