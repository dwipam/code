class Solution(object):
    def letterCombine(self, digits):
        letters = {"1":"1", "2":"abc"
                    ,"3":"def","4":"ghi",
                    "5":"jkl", "6":"mno",
                    "7":"pqrs", "8":"tuv", "9":"wxyz",
                    "0":"0"}
        digits = map(lambda x: x.encode(),list(digits))
        letter = []
        for i in range(len(digits)):
            combi1 = letters[digits[i]]
            for j in range(i+1,len(digits)):
                combi2 = letters[digits[j]]
                for k in list(combi1):
                    for l in list(combi2):
                        letter.append(k+l)
        return letter

s = Solution()
print s.letterCombine("12")
