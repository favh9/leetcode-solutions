from typing import List

def compute_counter(s1: str) -> List[int]:
    
    counter = [0] * 26
    for i in range(len(s1)):
        
        counter[ord(s1[i]) - ord('a')] += 1
            
    
    return tuple(counter)

def group_anagrams(strs: List[str]) -> List[List[str]]:

    """
        Collect the frequency of each letter of every word and
        make that the hash key. Every key will point us to a list
        of words that fit the exact frequency of each letter.
    """
    
    groups = {}
    output = []

    for word in strs:

        key = compute_counter(word)
        if key in groups:
            groups[key].append(word)
        else:
            groups[key] = [word]
    
    for list_of_words in groups.values():
        new_list = []
        for word in list_of_words:
            new_list.append(word)
        output.append(new_list)
    
    return output
    


