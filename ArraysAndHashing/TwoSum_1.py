from typing import List

def two_sum(nums: List[int], target: int):
    # target = a + b
    # a = target - b
    # we solve the eq. for every value 'b',
    # we store every value 'b' as the key
    # and use the difference to look up that key later

    map = {}
    
    for i in range(len(nums)):

        curr = nums[i]
        diff = target - curr

        if diff in map:
            # we found the pair
            return [map[diff], i]
        
        map[curr] = i