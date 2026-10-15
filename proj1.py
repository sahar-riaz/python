T = int(input("Enter Total bill: "))
TP = int(input("Enter Tip percentage: "))
NP = int(input("Enter Number of people splitting the bill: "))
#Operations#
Tip = T * TP / 100
Total = T + Tip
print("Total tip is =", Tip)
print("Overall total =", Total)
print("Individual's pay amount is =", Total / NP)

# 2nd program
P = input("Enter your password: ")
if len(P) >= 8 and P.isupper() == False and P.islower() == False and any(c.isupper() for c in P) and any(c.islower() for c in P) and any(c.isdigit() for c in P):
    print("Strong Password")
elif len(P) >= 6:
    print("Moderate Password")
else:
    print("Weak Password")

#3rd prorgam
    secret = 42
attempts = 0
while attempts < 5:
    guess = int(input("Guess the number (1-100): "))
    if guess < 1 or guess > 100:
        print("Invalid number")
        continue
    attempts = attempts + 1
    if guess == secret:
        print("Correct guess!")
        break
    else:
        print("Wrong guess")
else:
    print("Game Over! You lost.")
   
 #4ht program
name = input("Enter your full name: ")
parts = name.split()
first = parts[0]
last = parts[-1]
initials = first[0].upper() + ". " + last[0].upper() + "."
print("Initials =", initials)
print("Uppercase name =", name.upper())
print("Reversed name =", name[::-1])

#5th program
bank_balance = 5000

def deposit(amount):
    global bank_balance
    bank_balance += amount
    print("Updated balance =", bank_balance)

def withdraw(amount):
    global bank_balance

    if amount <= bank_balance:
        bank_balance -= amount
        print("Updated balance =", bank_balance)

    else:
        print("Insufficient balance")

deposit(1000)

withdraw(2000)

#6th program

sentence = input("Enter a long sentence: ")

characters = set(sentence)

characters.discard(" ")

print("Unique characters =", characters)

print("Total unique characters =", len(characters))
#7th program

students = {
    "Ali": 85,
    "Ayesha": 92,
    "Ahmed": 75,
    "Sara": 65,
    "Usman": 45
}

for name, marks in students.items():

    if marks >= 90:
        grade = "A"

    elif marks >= 80:
        grade = "B"

    elif marks >= 70:
        grade = "C"

    else:
        grade = "F"

    print(name, "Grade =", grade)