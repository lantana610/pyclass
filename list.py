skills = ["python", "Go", "Git", "linux"]
print(skills)
print(skills[0])
print(skills[3])
for skill in skills:
    print(skill)

# bonus challenge  

skills = []

skill1 = input("enter skill 1: ")
skill2 = input("enter skill 2: ")
skill3 = input("enter skill 3: ")

skills.append(skill1)
skills.append(skill2)
skills.append(skill3)

print(skills)

for i in range(3):
    skill = input("Enter a skill: ")
    skills.append(skill)
print(skills)