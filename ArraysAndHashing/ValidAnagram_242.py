def is_anagram(s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        s_map = {}
        # build a dictionary to store the letters 
        # and the count of each one
        for ch in s:
            if ch in s_map.keys():
                s_map[ch] += 1
            else:
                s_map[ch] = 1
        
        # decrement the count of each letter
        for ch in t:
            if ch in s_map.keys() and s_map.get(ch, 0) > 0:
                s_map[ch]-=1
            else:
                return False

        return True
