# LAST LAST NA BREAKFAST GO END AM LOVE CALCULATOR

print("Welcome to the Premium Breakfast Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

lovers_names = name1.lower() + name2.lower()

t = (lovers_names.count("t"))
r = (lovers_names.count("r"))
u = (lovers_names.count("u"))
e = (lovers_names.count("e"))

l = (lovers_names.count("l"))
o = (lovers_names.count("o"))
v = (lovers_names.count("v"))
e2 = (lovers_names.count("e"))

add_true = (t + r + u + e)
add_love = (l + o + v + e2)

str_add_true = str(add_true)
str_add_love = str(add_love)

final_score = int(str_add_true + str_add_love)
# print(type(final_score))

if final_score < 10 or final_score > 90:
    print(f"Your score is {final_score}, you go together like coke and mentos.")
elif final_score >= 40 and final_score <= 50:
    print(f"Your score is {final_score}, you are alright together.")
else:
    print(f"Your score is {final_score}.")


