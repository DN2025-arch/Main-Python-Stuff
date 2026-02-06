# recursion
inp = int(input(">>"))

# Recursive Case
def func_print(repeats):
    if repeats == 0:
        return
    else:
        print("Daniel")
        func_print(repeats-1)

func_print(inp)





def fun2(count):
   if count == 0:
       return
   else:
       fun2(count-1)
       print(count)
fun2(inp)

def sumfunc(count):
    if count == 0:
        return 0
    else:
        return count+sumfunc(count-1)
print(sumfunc(inp))

def factfunc(count):
    if count == 1:
        return 1
    else:
        return count*factfunc(count-1)
print(factfunc(inp))

def binfunc(count):
    if count == 1:
        return 1
    else:
        return str(binfunc(count//2))+str(count%2)
        
print(binfunc(inp))

def binfunc2(count):
    if count == 1:
        return 1
    else:
        return binfunc2(count//2)*10+count%2
        
print(binfunc2(inp))


def fibfunc(count):
    if count == 0:
        return 0
    if count == 1:
        return 1
    return fibfunc(count-1) + fibfunc(count-2) #last two terms

for i in range(1,inp):
    print(fibfunc(i))

def revfunc(st):
    if len(st) <= 1:
        return st
    return revfunc(st[1:]) + st[0] #place first letter in front
print(revfunc("hello world"))
