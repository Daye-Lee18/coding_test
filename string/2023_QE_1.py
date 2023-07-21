'''
Consider a string s that contains only lower-case alphabets. The number of characters in s does not exceed 10. 

(a) Implement a function foo(s) that returns a string t in which no two adjacent characters are adjacent in s, 
and t contains exactly the same number of characters as that of s. Moreover, when a character appears in s, 
t should contain it as often as in s. 

When there is no such string t, it returns an empty string "". 

If there are multiple strings that satisfy the conditions, return any of them. 

For example,
- when the string s is "abcde", foo(s) returns "adbec" 
- when the string s is "abc", foo(s) returns "". 
- when the string s is "", foo(s) returns ""/
- when the string s is "abccde" foo(s) returns "cacebd"
- when the string s is "abcdcef", foo(s) returns "cacfbed" 

'''

# 문제에서 two adjacent characters는 string안에서 "index" 가 -1, +1 로 바로 옆이 아닌 것을 말하는 것 같다. 


def foo(s: str) -> str:
    if len(s) <= 4:
        return ""
    
    even_list = []
    odd_list = []
    
    for idx in range(len(s)):
        if idx // 2 == 0:
            even_list.append(idx)
        else:
            odd_list.append(idx) 
    
    result = ''.join(s[even_list])
    result = result + ''.join(s[odd_list])

    return result  

'''

Implement a function bar(s) that returns a string t in which no two adjacent characters are adjacent in s, and s and t are different strings. 
When a character appears in s, t should contain it only once. 
When there is no such string t, it returns an empty string "". 
If there are multiple strings that satisfy the conditions, return any of them. 
For example, 

- when the string s is "abcde", bar(s) returns "adbec"
- when the string s is "abc", bar(s) returns ""
- when the string s is "", bar(S) return ""
- when the string s is "abccde", bar(s) returns "caebd" 
- when the string s is "abcdcef", bar(s) returns "cafbed" 

'''

def bar(s: str) -> str: 
    if len(s) <= 4:
        return ""
    
    # when a character appears in s, t should contain it only once 
    # 한 번만 하도록 dict에 채워줌 
    char_list = []
    idx_list = []
    for idx, char in enumerate(s): 
        if char not in  char_list:
            char_list.append(char)
            idx_list.append(idx) 
        else:
            continue 
    
    # 퐁당퐁당 
    even_result = ''
    odd_result = ''
    cur_str = ''.join(char_list)
    for char, idx in zip(char_list, idx_list):
        if idx // 2 == 0:
            even_result += char 
        else:
            odd_result += char   
    return even_result + odd_result 