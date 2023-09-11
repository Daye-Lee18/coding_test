'''
input: string s
output: reverse the order of the words 
    - without leading or trailing spaces 
    - s = "  hello world   "
    - output = "world hello"


ex) 

s = "the sky is blue"
output = "blut is sky the" 

'''

# s.split() 은 default로 " "에 의해 split되어 list로 반환된다. 
# 그 반환된 list를 reversed()로 순서를 뒤집는데 이때 실제 s.split()된 list의 order에는 아무런 영향을 미치지는 않음 순간적으로 reversed 됨 
# s = "Hello world"
# list1 = s.split()
# reversed(list1)
# print(list1)

class Solution:
  def reverseWords(self, s: str) -> str:
    return ' '.join(reversed(s.split()))
