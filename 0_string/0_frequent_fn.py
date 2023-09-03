
# from collections import Counter 

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

# char dictionary 
        # # INIT
        # digit_dict = dict()
        # digit_dict['z'] = [('ero', 0)] # 0 
        # digit_dict['o'] = [('ne', 1)] # 1 
        # digit_dict['t'] = [('wo',2),('hree',3)] # 2, 3 
        # # digit_dict['f'] = ['our', 'ive'] # 4, 5 
        # # digit_dict['s'] = ['ix', 'even'] # 6, 7 
        # # digit_dict['e'] = ['ight'] # 8
        # # digit_dict['n'] = ['ine'] # 9
        # digit_dict['f'] = [('our', 4), ('ive', 5)] # 4, 5 
        # digit_dict['s'] = [('ix', 6), ('even', 7)] # 6, 7 
        # digit_dict['e'] = [('ight', 8)] # 8
        # digit_dict['n'] = [('ine', 9)] # 9

        # idx_set = set()  
        # ans = ""

        # while input:
        #     for idx, char in enumerate(input):
        #         if char in digit_dict:
        #             idx_set.add(idx) 
        #             if len(digit_dict[char]) == 1 : # 0, 1, 8, 9
        #                 other_char = digit_dict[char]
        #                 other_char = list(other_char[0])
        #                 len_other_char= len(other_char)
        #                 cur_idx = 0
        #                 while other_char:
        #                     if other_char[cur_idx] in input:
        #                         idx_set.add(cur_idx)
        #                         other_char = other_char[:cur_idx] + other_char[cur_idx+1:]
        #                         cur_idx += 1 
        #                     else:
        #                         break 
                        
        #                 if cur_idx == len_other_char -1:
        #                     input = 

        # my own dictionary 
        # digits = 'zeroonetwothreefourfivesixseveneightnine'
        # digits_dict = {}
        # zero = {'z':1, 'e':1, 'r':1, 'o':1}
        # one = {'o':1, 'n':1, 'e':1}
        # two = {'t':1, 'w':1, 'o':1}
        # three = {'t':1, 'h':1, 'r':1, 'e':1, 'e':1}
        # four = {'f':1, 'o':1, 'u':1, 'r':1}
        # five = {'f':1, 'i':1, 'v':1, 'e':1}
        # six = {'s':1, 'i':1, 'x':1}
        # seven = {'s':1, 'e':1, 'v':1, 'e':1, 'n':1}
        # eight = {'e':1,'i':1,'g':1, 'h':1,'t':1} 
        # nine  = {'n':1,'i':1,'n':1,'e':1}
        # digits_dict[0] = zero
        # digits_dict[1] = one
        # digits_dict[2] = two
        # digits_dict[3] = three
        # digits_dict[4] = four
        # digits_dict[5] = five
        # digits_dict[6] = six   
        # digits_dict[7] = seven
        # digits_dict[8] = eight
        # digits_dict[9] = nine