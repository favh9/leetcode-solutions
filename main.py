from fastapi import FastAPI
from ArraysAndHashing.ContainsDuplicate_217 import contains_duplicate
from ArraysAndHashing.ValidAnagram_242 import is_anagram_v2
from ArraysAndHashing.TwoSum_1 import two_sum
from ArraysAndHashing.GroupAnagrams_49 import group_anagrams
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
    return {"is_anagram": is_anagram_v2(s, t)}

@app.post("/1")
def check_two_sum(nums: List[int] = Body(List[int]), target: int = Body(int)):
    return {"two_sum": two_sum(nums, target)}

@app.post("/49")
def check_group_anagrams(strs: List[str] = Body(List[str])):
    return {"anagram_groups": group_anagrams(strs)}
    
