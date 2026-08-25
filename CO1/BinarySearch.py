def Library(target):
    array=list(range(1,1000001))
    low=0
    high=len(array)-1
    while low<=high:
        mid=low+(high-low)//2
        if array[mid]==target:
            return mid
        elif array[mid]<target:
            low=mid+1
        else:
            high=mid-1
    return -1
print("what book do you want to find:")
n=int(input())
result = Library(n)
if result==-1:
    print("book not found")
else:
    print("book is at: ",result)
