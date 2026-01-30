
quantatity = int(input("Quantatity:"))

for row in range(1,quantatity+1):
    for column in range(1,quantatity+1):
        print("*", end="", sep=",")
        # end="\n" on default
        # sep=" " on default. 
    print()  # by default: \n

print("-----------------")

for row in range(1,quantatity+1):
    for column in range(1,row+1):
        print("*", end="")
    print()

print("-----------------")

for row in range(1,quantatity+1):
    for column in range(1,row+1):
        print(f"{row}", end="")
    print()

print("-----------------")

for row in range(1,quantatity+1):
    for column in range(1,row+1):
        print(f"{column}", end="")
    print()

print("-----------------")

numb = 1
for row in range(1,quantatity+1):
    for column in range(1,row+1):
        print(f"{numb}", end="")
        numb += 1
    print()

print("-----------------")

for row in range(1,quantatity+1):
    for column in range(1,row+1):
        print(f"{quantatity+1 - row}", end="")
    print()

print("-----------------")

for row in range(1,quantatity+1):
    for column in range(1,quantatity-row+1):
        print(f"{quantatity - row}", end="")
    print()

print("-----------------")

spaces = ""
for row in range(1,quantatity+1):
    for column in range(1,quantatity-row+1):
        print(f"{quantatity - row}", end="")
    print()
    spaces += " "
    print(f"{spaces}",end="")
spaces = ""
print()

print("-----------------")

for row in range(1,quantatity+1):
    for sp in range(1,quantatity-row+1):
        print(" ",end="")
    for column in range(1,row+1):
        print(f"{row}", end="")
    print()

print("-----------------")

half = quantatity // 2
##print(half)

for row in range(1,quantatity+1):
    if row <= half:
        for sp in range(1,half-row+1):
            print(" ",end="")
        for column in range(1,row+1):
            print(f"@", end="")
        print()
    else:
        for sp in range(half,row):
            print(" ",end="")
        for column in range(quantatity,row,-1):
            print(f"@", end="")
        print()

##    @
##   @@
##  @@@
##   @@
##    @
