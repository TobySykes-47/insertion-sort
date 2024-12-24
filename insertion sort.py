#importing the random module
import random
#function creating the data to sort 
dataList = []
def data():
#creating an empty list that can be accessed anywhere in the program
    global dataList
#fills the list with 20 random numbers
    for i in range(20):
        dataList.append(random.randint(1, 100))
#outputs the unsorted list of data
    print(dataList)

#function that actually sorts the data and has the list of numbers passed through
def insertionSort(dataList):
#creating a variable for the size of the list
    size = len(dataList)
#for loop to iterate the same ammount of times as numbers in the list
    for i in range (1, size):
#the number to be put into the correct position in the list
        x = dataList[i]
#the number to be swapped if it's in the incorrect position
        y = i-1
#loop to move the selected number 1 index to the right if its in the incorrect position
        while y >= 0 and x < dataList[y]:
#swapping the numbers around
            dataList[y+1] = dataList[y]  
            y -= 1
        dataList[y+1] = x
#outputting the list every iteration of the sort
        print(dataList)
        
#function that creates and displayes the random list
data()
#function that sorts the list with the list passed through
insertionSort(dataList)           