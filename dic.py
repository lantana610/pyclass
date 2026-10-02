student = {
    "name": "Lantana",
    "age": 4,
    "skill": "python"
}
student["age"] = 5
student["country"] = "Nigeria"
print(student["name"])
print(student["age"])
print(student["skill"])

print(
f"{student['name']} is {student['age']} years old, lives in {student['country']}, and is learning {student['skill']}."
)