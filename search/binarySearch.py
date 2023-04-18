class binarySearch:
    def searchLogic(self,arr,target) -> int:
        start= 0
        end = len(arr)-1
        if(target==arr[start]):
            return start
        elif(target==arr[end]):
            return end
        else:
            while(start!=end):
                mid = int(start + (end - start)/2)
                if(target==arr[mid]):
                    return mid
                elif(target<arr[mid]):
                    end = mid-1
                else:
                    start = mid+1
        return -1
arr = [2, 3, 5, 9, 14, 16, 18]
target = 8
result =binarySearch().searchLogic(arr, target)
print(result)