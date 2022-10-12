#Anagram is a word or a name formed by rearranging the letters of another, such as a spar, formed rasp.
#Given two strings s and t, write a function to determine if t is anagram of s

# You assume the string contains only lowercase
def isAnagram(s,t):
    if len(s)!= len(t):
        return False
    return sorted(s) == sorted(t)