input = ['bcbc','aaab','baa','aaa']
def palindromeIndex(s):
    for i in range(len(s)):
       if s[i]!=s[-i-1]:
           if s[i]==s[-i-2]:
               return len(s)-1
           return i
    return -1
for i in input:
    print(palindromeIndex(i))
