
mylist = [9,4,7,2,3,6,10,1,5,8]
print(mylist)

# Merge Sort

def mergedivide(lis,low,high,):
    if low < high:
        middle = (high+low)//2
        mergedivide(lis,low,middle)
        mergedivide(lis,middle+1,high)
        mergesort(lis,low,middle,high)

def mergesort(lis,low,middle,high):
    sortedlist = []
    x = low
    y = middle+1
    while x<=middle and y<=high:
        if mylist[x] < mylist[y]:
            sortedlist.append(mylist[x])
            x += 1
        else:
            sortedlist.append(mylist[y])
            y += 1
    while x<=middle:
        sortedlist.append(mylist[x])
        x += 1
    while y<=high:
        sortedlist.append(mylist[y])
        y += 1
    k = 0
    for i in range(low,high+1):
        mylist[i] = sortedlist[k]
        k+=1

        
mergedivide(mylist,0,9)

print(mylist)
