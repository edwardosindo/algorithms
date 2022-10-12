# Simple sorting Algorith
#Simple implementation
#Quadratic running time o(n^2 ) which makes it abit slower

def insertion_sort(arr):
    #outerloop that goes from the second element to the last element
    for i in range(1, len(arr)):
        # we need an inner loop that starts at the index of the outer loop and iterates the list to the left
        # and checks if we need to do swaps and stops if we dont need to swap anymore
        j = i
        #inner loops needs conditions, the first condition is our swaping condition (arr[j -1] > arr[j]) 
        #we want to check if the left neighboor is bigger than the current element and if so we want to do is swap
        while arr[j -1] > arr[j] and j > 0:
            #swap in python is implemented like
            arr[j - 1], arr[j] = arr[j], arr[j -1]
            # we need to go further to the left in our list after the swap and we need to check if we are at the left most side of the list
            j -= 1


        



#define our list so that we have something to test
arr = [2,4,7,6,7,8,9,89]