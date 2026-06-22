from collections import Counter

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        # Count the frequency of all characters in the text
        counts = Counter(text)
        
        # Calculate how many instances of each letter are available
        # Divide counts of 'l' and 'o' by 2 because 'balloon' requires two of each
        b = counts['b']
        a = counts['a']
        l = counts['l'] // 2
        o = counts['o'] // 2
        n = counts['n']
        
        # The limiting factor determines the maximum number of words formed
        return min(b, a, l, o, n)
