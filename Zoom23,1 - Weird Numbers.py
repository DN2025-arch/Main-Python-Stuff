#NEXT: HCF & LCM
a = int(input("choose a number A"))
b = int(input("choose a number B"))

c = a*b
if a > b:
    d = a
else:
    d = b
for i in range(d,c+1):
    if i%a == 0 and i%b == 0:
        print(f"LCM: {i}")
        break

scf = 0
for i in range(1,d+1):
    if a%i == 0 and b%i == 0:
        scf = i
print(f"HCF: {scf}")


chosen = input("choose a number")
chosen = int(chosen)
digits_list = []
temp = chosen
palindrome = True
while temp > 0:
    digits_list.append(temp%10)
    temp = temp//10
for i in range(len(digits_list)):
    if digits_list[i] != digits_list[-(i+1)]:
        palindrome = False
print(f"PALINDROME NUMBER: {palindrome}")



chosen = input("choose a Number")

##digits = len(list(chosen))
##armstrong = False
##adding = []
##for i in chosen:
##    i = int(i)
##    new = i**digits
##    adding.append(new)
##if sum(adding) == int(chosen):
##    armstrong = True

chosen = int(chosen)
temp = chosen
digits = 0
new = 0
armstrong = False
while temp > 0:
    d = temp%10      # Give each digit
    digits += 1
    temp = temp//10  # Divide, only give integer part
temp = chosen
while temp > 0:
    d = temp%10      # Give each digit
    temp = temp//10  # Divide, only give integer part
    new += d**digits
if new == chosen:
    armstrong = True

print(f"ARMSTRONG NUMBER: {armstrong}")


chosen = input("choose a Number")
chosen = float(chosen)

if chosen%2 == 0:
    print("EVEN NUMBER: True")
else:
    print("EVEN NUMBER: False")

chosen = input("choose a Number")
chosen = int(chosen)
print("calculating...")

prime = False
factors = 0
for i in range(1,chosen+1):
    #print(i)
    if chosen%i == 0:
        factors += 1
if factors >= 3:
    prime = False
elif factors == 2:
    prime = True

print(f"PRIME NUMBER: {prime}")


chosen = input("choose a Number")
chosen = int(chosen)

buzz = False
if chosen%7 == 0:
    buzz = True
chosen = str(chosen)
if chosen[-1] == "7":
    buzz = True

print(f"BUZZ NUMBER: {buzz}")



