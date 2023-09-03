from collections import Counter

class Solution:
    def originalDigits(self, s):
        # Create a Counter object to count the occurrences of each character in the input string.
        cnt = Counter(s)
        
        # List of words representing the digits in decreasing order of uniqueness.
        Digits = ["zero", "two", "four", "six", "eight", "one", "three", "five", "seven", "nine"]
        
        # Corresponding indices for the digits in the "Digits" list.
        Corresp = [0, 2, 4, 6, 8, 1, 3, 5, 7, 9]
        
        # Create a list of Counter objects for each digit word.
        Counters = [Counter(digit) for digit in Digits]
        
        # Initialize a list to keep track of how many times each digit is found.
        Found = [0] * 10
        
        # Loop through each digit's Counter and try to find the maximum possible occurrence.
        for it, C in enumerate(Counters):
            # Calculate the potential number of times this digit can be formed based on available characters.
            k = min(cnt[x] // C[x] for x in C)
            
            # Adjust the counters of characters in the current digit word by the calculated factor.
            for i in C.keys():
                C[i] *= k
            
            # Update the main counter by subtracting the adjusted digit counter.
            # counter는 subtracting이됨, value가 0이 되면 해당 key는 사라짐. 
            cnt -= C
            
            # Update the "Found" list to store how many times this digit was found.
            Found[Corresp[it]] = k
        
        # Generate the final output string by joining the digits based on the count of their occurrences.
        return "".join([str(i) * Found[i] for i in range(10)])
