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

# Intuition -- 
# Both strings only contain lowercase English letters, so we can use a counting approach.
# Count each letter in the first word, then subtract counts using the second word.
# If all counts end up at zero, the string are anagrams
def is_anagram_v2(s: str, t: str) -> bool:
     
    if len(s) != len(t):
        return False
    
    abc = [0] * 26

    for i in range(len(s)):

        abc[ord(s[i]) - ord('a')] += 1
        abc[ord(t[i]) - ord('a')] -= 1
    
    for num in abc:
        if num != 0:
            return False

    return True

     