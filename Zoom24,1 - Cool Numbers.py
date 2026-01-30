chosen = int(input("Choose a Number"))

squared = chosen ** 2

total = 0
temp = squared
while temp > 0:
    total += temp%10
    temp = temp // 10

if total == chosen:
    print(f"This Number is a Neon Number")
else:
    print(f"This Number is not a Neon Number")

chosen = int(input("Choose a Number"))

total_digits = 0
temp = chosen
while temp > 0:
    total_digits += 1
    temp = temp // 10
print(total_digits)

power = 10 ** total_digits
squared = chosen ** 2

if squared%power == chosen:
    print(f"This Number is a Automorphic Number.")
else:
    print(f"This Number is not a Automorphic Number.")


chosen = int(input("Choose a Number"))

product = 1
for i in range(1,chosen+1):
    product *= i
print(product)



chosen = int(input("Choose a Number"))
squared = chosen ** 2

total_digits = 0
temp = squared
while temp > 0:
    total_digits += 1
    temp = temp // 10

if not total_digits%2 == 0:
    print("Impossible")
else:
    half1 = squared//10 ** (total_digits//2)
    half2 = squared%10 ** (total_digits//2)

    if half1 + half2 == chosen:
        print("This Number is a Tech Number")
    else:
        print("This Number isn't a Tech Number")


# Duck Number, Hashtag Number, Perfect Number, Spy Number



chosen = str(input("Choose a Number -Duck"))

duck = False

if not chosen[0] == "0":
    for i in chosen:
        if i == "0":
            duck = True

if duck:
    print("This Number is a Duck Number")
else:
    print("This Number isn't a Duck Number")


chosen = int(input("Choose a Number -Hash"))

total_dig = 0
temp = chosen
while temp > 0:
    total_dig += 1
    temp = temp // 10
power = 10 ** (total_dig-1)

if chosen//power == chosen%10:
    print("This Number is a Hashtag Number")
else:
    print("This Number isn't a Hashtag Number")


chosen = int(input("Choose a Number -Perfect"))

total = 0

for i in range(1,chosen):
    if chosen%i == 0:
        total += i

if chosen == total:
    print("This Number is a Perfect Number")
else:
    print("This Number isn't a Perfect Number")


chosen = int(input("Choose a Number -Spy"))

total = 0
product = 1
temp = chosen
while temp > 0:
    total += temp%10
    product *= temp%10
    temp = temp // 10

if total == product:
    print(f"This Number is a Spy Number")
else:
    print(f"This Number is not a Spy Number")




