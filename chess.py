import re
a=['1','2','3','4','5','6','7','8']
b=['A','B','C','D','E','F','H','G']
p=[q.upper() for q in input("Enter your rook positions:").split(" ")]
numbers=[]
alphabet=[]
output=[]
for i in p:
    numbers.append(re.findall(r'\d',i)[0])
for i in p:
    alphabet.append(re.findall(r'[A-Za-z]',i)[0])
print(numbers)
print(alphabet)
for char in numbers:
    if char in a:
        a.remove(char)
for char in alphabet:
    if char in b:
        b.remove(char)
for j in a:
    for k in b:
        output.append(str(k)+str(j))
print(output)