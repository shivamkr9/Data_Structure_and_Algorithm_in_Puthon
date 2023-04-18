from typing import List
# import array as ar
'''
def bubbleShort(arr:List)-> None:
    for i in range(len(arr)-1):
        isShorted = False
        for j in range(1,len(arr)-i):
            if arr[j]< arr[j-1]:
                temp = arr[j]
                arr[j]= arr[j-1]
                arr[j-1]= temp
                print(i)
                isShorted = True
        if not isShorted:
            break;
    print(arr)
'''

class BubbleShorting():
    def bubbleShort(self, arr: List) -> None:
        for i in range(len(arr) - 1):
            isShorted = False
            for j in range(1, len(arr) - i):
                if arr[j] < arr[j - 1]:
                    temp = arr[j]
                    arr[j] = arr[j - 1]
                    arr[j - 1] = temp
                    isShorted = True
            if not isShorted:
                break;

if __name__ == "__main__":
    # arr =[1,2,3,4,5,6]
    arr = [1,5,7,4,88,-5]
    BubbleShorting().bubbleShort(arr=arr)
    print(arr)