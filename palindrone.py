# Palidrome is a word/phrase that reads the same backwards and forward
def isPalidrome(s):
    return s == s[::-1]

#Driver code
s = "malayalam"
ans = isPalidrome(s)
if ans:
    print("Yes")
else: 
    print("No")