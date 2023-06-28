numList = input("Please enter 10 numbers separated by space: ")
numListSplit = numList.split()

# Convert String list to Int list
numListSplit = [int(num) for num in numListSplit]

# Checks if ODD, add to list
finalNum = [num for num in numListSplit if num % 2 == 1]

if not finalNum:
    print("No odd numbers were entered.")
else:
    print(max(finalNum))
