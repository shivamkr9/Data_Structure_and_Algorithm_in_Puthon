class BinarySearch:
    def algorithm(self, num, target):
        if len(num) == 0:
            return -1
        start = 0
        endValue = len(num) - 1
        while(start <= endValue):
            midValue = int((start +endValue) / 2)
            if target>num[midValue]:
                endValue= midValue-1
            elif target<num[midValue]:
                start=midValue+1
            else:
                return midValue
        return -1


num = [18,16,14,9,5,3,2]
target = 14
ans =BinarySearch().algorithm(num=num, target=target)
print(ans)