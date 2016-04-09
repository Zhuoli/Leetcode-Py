class Solution(object):
    def wordPattern(self, pattern, str):
        mapper = [' ']*(ord('z')-ord('a')+1)
        strList = str.split()

        # False if count not the same
        if len(pattern) != len(strList):
            return False

        # process each element
        for idx in range(len(pattern)):

            # get element
            char = pattern[idx]

            mapperIdex = ord(char) - ord('a')
            # get mapping value

            # initialize if not set
            if mapper[mapperIdex] == ' ':
                mapper[mapperIdex] = strList[idx]

            elif mapper[mapperIdex] != strList[idx]:
                return False

        valueset = set(mapper)
        valueset.remove(' ')
        patternset = set(list(pattern))
        return len(valueset) == len(patternset)

solution = Solution()
pattern = 'abba'
str="dog cat cat dog"
print(solution.wordPattern(pattern, str))