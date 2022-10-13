# A pandigital number is an integer that has each digit of its base at least once.
# Its is assumed that base is smaller than or equal to 36.

# Make a boolean hash array of size equal to base of the number and initialize it with false.
# Now iterate each digit of the number mark its corresponding index value as true in the hash array.
# In the end, check whether all the value in hash array are marked or not, if marked print "Yes" i.e Pandigital number else print "No"
# Below is the implementation of this approach

# Python3 program to check if a number is pandigital in given base.

# Return true if n is pandigit else return false.
def checkPandigital(b, n):

    # Checking length is less than base
    if (len(n) < b):
        return 0;

    hash = [0] * b;

    # Traversing each digit of the number.
    for i in range(len(n)):

        # If digit is integer
        if (n[i] >= '0' and n[i] <= '9'):
            hash[ord(n[i]) - ord('0')] = 1;

        # If digit is alphabet
        else:
            if (ord(n[i]) - ord('A') <= b - 11):
                hash[ord(n[i]) - ord('A') + 10] = 1;

    # Checking hash array, if any index is unmarked
    for i in range(b):
        if (hash[i] == 0):
            return 0;

    return 1;

# Driver Code
b = 13;
n = "1298450376ABC";

if(checkPandigital(b, n)):
    print("Yes");
else:
    print("No");
