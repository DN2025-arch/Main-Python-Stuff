
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

## 54321
##  5432
##   543
##    54
##     5

print("-----------------")

##    @
##   @@
##  @@@
##   @@
##    @
