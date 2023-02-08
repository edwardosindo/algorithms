# https://www.youtube.com/watch?v=cVZMah9kEjI&ab_channel=FelixTechTipshttps://www.youtube.com/watch?v=cVZMah9kEjI&ab_channel=FelixTechTips

# OVERVIEW
# - Divide and conquer algorithm : The problem is divided into multiple subproblems recursively until they become simple to solve, solutions are combined to solve original problem
# - It has O(n * log(n)) running time - Which is the optimal running time for comparison based algorith
def merge_sort(arr):
    if len(arr) > 1:
        left_arr = arr[:len(arr)//2]
        right_arr = arr[len(arr)//2:]

        # recursion
        merge_sort(left_arr)
        merge_sort(right_arr)

        # Merge
        i = 0  # for left_arr idx
        j = 0  # for right_arr idx
        k = 0  # for merged arr idx

        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
                k += 1
            else:
                arr[k] = right_arr[j]
                j += 1
                k += 1

        # We assume there is nothing in the right array
        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1

        # We assume there is nothing in the left array
        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1


arr_test = [2,3,5,1,7,4,4,2,6,0]
merge_sort(arr_test)
print(arr_test)