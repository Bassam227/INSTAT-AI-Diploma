import re


fi = open(r"C:\Users\Ehtyat\Desktop\test.txt")
text = fi.read()



name = []
number = []
email = []


pattern = re.compile(r"[A-Za-z]+\s[A-Za-z]+")
Name = pattern.finditer(text)

pattern = re.compile(r"01\d{8}")
Number = pattern.finditer(text)

pattern = re.compile(r"\w+@gmail.com")
Email = pattern.finditer(text)

for n in Name:
    start = n.span()[0]
    end = n.span()[1]
    name.append(text[start:end])
print("Names : ",name)

for n in Number:
    start = n.span()[0]
    end = n.span()[1]
    number.append(text[start:end])
print("Phone Number : ",number)

for n in Email:
    start = n.span()[0]
    end = n.span()[1]
    email.append(text[start:end])
print("Emails : ",email)





