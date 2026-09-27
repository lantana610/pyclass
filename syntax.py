user_age = int(input('enter your age:'))

if user_age >= 18:
    print("you are eligible to vote")
else:
    print("you are not eligible to vote")

# bonus challenge 

score = int(input("your score:"))


if score < 0 or score > 100:
    print('invalid score')
elif score >= 80:
    print("you got A")
elif score >= 70:
    print("you got B")
elif score >= 60:
    print("you got C")
elif score >= 50:
    print("you got D")
else:
    print("you got F")        
       