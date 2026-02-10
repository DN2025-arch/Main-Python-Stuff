
mylist = [1,2,3,6,7,8,9,10]

chosen = int(input(">>"))

##if chosen in mylist:
##    print("hi")
##
##index = 0
##for i in mylist:
##    index += 1
##    if i == chosen:
##        print("hi", index)


# Linear Search Algerithm
found = False
for i in range(len(mylist)):
    #print(mylist[i])
    if chosen == mylist[i]:
        found = True
        print("Present! Position:", i)
        break
if found == False:
    print("Absent!")

# Best Case:   Ω(1)
# Worst Case:  Ο(n)
# Average Case:θ(n/2)
# Where n is len of list

# Binary Search Algerithm
start = 0
end = len(mylist)
while start<=end:
    middle = (end+start)//2
    if mylist[middle] == chosen:
        print("Found At:", middle)
        break
    else:
        if chosen > mylist[middle]:
            start = middle+1
        else:
            end = middle-1
    if not start <= end:
        print("Not Found")

# Best Case:   Ω(n/2)
# Worst Case:  O(log_2 n)
# Average Case:θ(log_2 n)
# Where n is len of list

