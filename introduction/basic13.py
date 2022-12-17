# 1. Print all intergers fron 1 to 255

# for i in range(1,256):
#     print(i)

# 2. Print intergers from 0 to 255, with each intergers print out the sum so far


# def printwithSum(): 
#     for i in range(256):
#         sum = 0
#         sum += i 
#         print(f"i: {i}, sum: {sum}")

# printwithSum()

# 3. Given an array, find and print its largest element


# def findLargest(list):
#     largest = list[0]
#     for i in range(len(list)):
#         if list[i] > largest:
#             largest = list[i]
#             print(f"found the new largest: {largest}")
#     print(f"largest is: {largest}")
# findLargest([4,8,9,3,1,8,5,7,8])

# 4. Create an array with all the odd intergers between 1 to 255 

# def oddList():
#     list = []
#     for i in range(1,256):
#         if i%2 != 0:
#             list.append(i)
#     print(list)
# oddList()


# def oddList():
#     list = []
#     for i in range(1,256,2):
#         list.append(i)
#     print(list)
# oddList()

# 5. Given an arr, move all values forward by one index, dropping the first and leaving a '0' value at the end.

# def shiftValue(list):
#     for i in range(len(list)):
#         if i != len(list) - 1:
#             list[i] = list[i+1]
#         else:
#             list[i] = 0
#     print(list)
# shiftValue([4,5,6,7,8,9])


def shiftValue(list):
    for i in range(len(list) - 1):
        list[i] = list[i+1]
    list[-1] = 0
    print(list)
shiftValue([4,5,6,7,8,9])
