class Solution:
    def scoreOfString(self, s: str) -> int:
        score = 0
        for i in range(len(s) -1):
            s1 = ord(s[i])
            s2 = ord(s[i+1])
            loopscore = abs(s2 - s1)
            score += loopscore 
        return score
        