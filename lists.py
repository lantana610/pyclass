languages = ["python", "Go", "JavaScript"]

languages.append("Rust")
languages.remove("Go")
print(len(languages))

for language in languages:
    print(language)