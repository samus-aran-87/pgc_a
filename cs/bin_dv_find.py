def binarysearch(mylist, iskat, start, stop):
    if start > stop:
        return False
    else:
        mid = (start + stop) // 2
        if iskat == mylist[mid]:
            return mid
        elif iskat < mylist[mid]:
            return binarysearch(mylist, iskat, start, mid-1)
        else:
            return binarysearch(mylist, iskat, mid+1, stop)


mylist = [10, 12, 13, 15, 20, 24, 27, 33, 42, 51, 57, 68, 70, 77, 79, 81, 90]
iskat = 79
start = 0
stop = len(mylist)

x = binarysearch(mylist, iskat, start, stop)
if x == False:
    print("Item {} not found".format(iskat))
else:
    print("Item {} found: {}".format(iskat, x))

for n, i in enumerate(mylist):
    if i == iskat:
        print(n, i)
