'''
- implement max_palindrome(s) 
- returns a list of substrings of s that are maximal palindromes 
- the list contains palidromes that are not a substring of another palindrome
- ex) 
For s = "kabccbadzdefgfeda",
max palindromes(s) should return ["k", "abccba", "dzd", "defgfed"]

For s = "kabccba dzabccbaza",
max palindromes(s) should return ["k", " ", "d", "zabccbaz", "aza"]
'''

# problem (a) 
# a function checks if the string s is a palindrome 
def palindrome(s:str) -> bool:
    if len(s) == 1: 
        return True
    len_s = len(s) 
    mid = len_s // 2 
    if len_s % 2 == 0:
        l = mid -1
        r = mid 
    else:
        l = r = mid 

    while l >= 0 and r < len_s and s[l] == s[r]:
            l -= 1 
            r += 1 

    if l < 0 :
         return True 
    return False 



# problem (b) 
# a function substring(s, t) that checks if the string t is a substring(s,t) 

def substring(s:str,t:str) -> bool:
    if len(s) >= len(t):
        len_t = len(t) 
        difference_len = len(s) - len(t) 
        for idx, char in enumerate(s[:difference_len]):
            if s[idx:idx+len_t] == t:
                return True 

        return False 
    else:
        return False 




# problem (c) 
# funtion max_palindromes(s) that uses palidrome(s) and substring(s,t) 
def max_palindrome(s:str) -> list:
    temp = []

    # find all palindromes 
    for i in range(len(s)):
        for j in range(i, len(s)+1):
            candidate_s = s[i:j]
            if palindrome(candidate_s):
                temp.append(candidate_s) 
    
    for _ in temp:
        print(temp)

    # find whether there are some substring or the same palindrome
    result = set(temp) 
    result = list(result)
    result.remove('')
    # print(result, len(result))

    # combination not permutation since you do the opposite in the 2 consecutive if prahse below
    # remove_list = []

    # for i in range(len(result)-1):
    #     for j in range(i+1, len(result)):
    #         # print(i,j)
    #         if substring(result[i], result[j]) == True:
    #             # result.remove(result[j]) # result의 길이가 계속 변해서 안됨 
    #             remove_list.append(result[j])
    #         if substring(result[j], result[i]) == True:
    #             # result.remove(result[i])
    #             remove_list.append(result[i])
    # print(remove_list)
    # print(result)
    # #subtract 
    # for rem in remove_list:
    #     result.remove(rem)
    
    def remove_redundant_substring(string_list):
        result = []
        ### important to sort first #### 
        string_list.sort(key=len) # sort the strings by length to process short substrings first 
    
        for i, s in enumerate(string_list):
            is_redundant = False 
            for j in range(i+1, len(string_list)):
                if substring(string_list[j],s):
                    is_redundant = True 
                    break 
            if not is_redundant:
                result.append(s) 
        return result 
    
    ans = remove_redundant_substring(result)

    return ans


            
if __name__ == '__main__':
    # s = "kabccbadzdefgfeda"
    s = "kabccba dzabccbaza"
    # t = 'sdvxz' 
    # print(substring(s,t))
    print(max_palindrome(s))
         

              