
def mostfrequeent(list):
    # Initialize count, index, and temp variable
    count = 0
    index = 0
    temp = 0

    # create a for loop that runs from 0 to len of list
    for x in range (0, len(list)):
        # count each number from the list and how many times they appear
        temp = list.count(list[x])
        # print(temp)

        # write an if statement to compare temp var and count var
        if (temp>count):
            count = temp 
            print(count)
            index = x

    mostfrequent= list[index]

    print("this is the answer:", mostfrequent)
    print("The number appeared", count, "times")

list = [1,2,2,2,2,2,24,6,6,6,]