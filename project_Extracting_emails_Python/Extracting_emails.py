import re

with open("data.txt","r") as f:
    content=f.read()

pattern=re.compile(r'\w+@\w+.com')

dictionary={}
matches=pattern.findall(content)
i=1
for match in matches:
    values={f"Email {i}":f"{match}"}
    dictionary.update(values)
    i+=1

print(dictionary)