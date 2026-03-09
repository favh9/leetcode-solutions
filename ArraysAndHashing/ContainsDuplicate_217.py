def contains_duplicate(nums) -> bool:
        
    map = {}

    for num in nums:
        if num in map.keys():
            return True
        else:
            map[num] = 1
    
    return True


    