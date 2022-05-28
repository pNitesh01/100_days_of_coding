print("Welcome to the love Calculator!")
name1 = input("What is your name?\n")
name2 = input("What is their name?\n")

name = name1.lower() + name2.lower()

t = name.count('t')
r = name.count('r')
u = name.count('u')
e = name.count('e')
true_score = t + r + u + e

l = name.count('l')
o = name.count('o')
v = name.count('v')
e = name.count('e')
love_score = l + o + v + e

final_score = true_score * 10 + love_score

if final_score < 10 or final_score > 90:
    print(f"Your score is {final_score}, you go together like coke and mentos.")
elif final_score >= 40 and final_score <= 50:
    print(f"Your score is {final_score}, you are alright together.")
else:
    print(f"Your score is {final_score}.")
