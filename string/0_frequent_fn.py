
def is_palindrome(s:str) -> bool:
    mid = len(s) // 2 
    if len(s) % 2 ==0:
        l = mid -1 
        r = mid 
    else:
        l = r= mid 
    
    while l >= 0 and r < len(s) and s[l] == s[r]:
        l -= 1 
        r += 1 
    
    if l < 0:
        return True 
    return False 