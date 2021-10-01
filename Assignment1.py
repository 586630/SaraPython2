#Task1
checking = input()
savings = input()
if (savings < 1 or checking < 1):
    print("Balance is negative")
operation = input()
if(operation == 1):
    account = input()
    if(account ==1):
        amount = input()
        savings += amount 
    elif(account == 2):
        amount = input()
        checking += amount 
    else:
        print("Not valid")
elif(operation == 2):
    account = input()
    if(account == 1):
        amount = input()
        if(savings -amount<0):
            print("Not enough money")
        else:
            savings -= amount
    elif(account == 2):
        account = input()
        if(account == 1):
            amount = input()
            if(checking -amount<0):
                print("Not enough money")
            else:
                checking -= amount
    else:
        print("Not valid")
elif(operation == 3):
    accountFrom = input()
    accountReciver = input()
    if(accountReciver == accountFrom):
        print("Same account")
    elif(accountFrom == 1):
        amount = input()
        if(savings - amount<0):
            print("Not enough money")
        else:
            savings -= amount
            checking += amount
    elif(accountFrom == 2):
        amount = input()
        if(checking - amount < 0):
            print("Not enough money")
        else:
            checking -= amount
            savings += amount
    else:
        print("Not valid")
else:
    print("Not Valid")

#Task2

hours = float(input())
salary = float(input())
extra = 0
if(hours > 40):
    extra = hours - 40
    hours = 40
print((hours*salary) + (extra*(salary*1.5)))

#Task3
target = input()
currentPrice = input()

def minTargetPrice(sequence):
    min = 0
    for i in sequence:
        if i < min:
            min = i
    return min

while(minTargetPrice(target) <= currentPrice):
    print("dont buy")
print("buy")

#Task4
s = "hannah"
s1 = s[:len(s)//2]
s2 = s[len(s)//2:]
s2 = s2[::-1]
if(s1 == s2):
    print("Palindromes")