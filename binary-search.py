# https://www.youtube.com/watch?v=zeULw-a7Mw8&list=PL5tcWHG-UPH1K7oTJgIbWy6rCMc8-8Lfm&ab_channel=LucidProgramming

data = [2,3,5,7,8,9,10,15,16,29,30,45]
target = 45

# Solution using linear binary search
def linear_search(data, target):
    for i in range(len(data)):
        if data[i] == target:
            return True
    return False

# Iterative Binary Search

# Step-by-step Binary Search Algorithm: We basically ignore half of the elements just after one comparison.

# 1. Compare x with the middle element.
# 2. If x matches with the middle element, we return the mid index.
# 3. Else If x is greater than the mid element, then x can only lie in the right half subarray after the mid element.
# So we recur for the right half.
# 4. Else (x is smaller) recur for the left half.


def binary_search_iterative(data, target):
    low = 0
    high = len(data) - 1

    while low <= high:
        mid = (low + high) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return False


# # Recursive Binary Search
def binary_search_recursive(data,target, low, high):
    # Base function
    if low > high:
        return False
    else:
        mid = (low + high) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            return binary_search_recursive(data, target, low, mid-1)
        else:
            return binary_search_recursive(data, target, mid+1, high)

print(linear_search(data, target))
print(binary_search_iterative(data, target))
print(binary_search_recursive(data, target, 0, len(data)-1))