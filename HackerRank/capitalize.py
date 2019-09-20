s = input()
# s = s.strip()
# lista = s.split()
final = ""

# for i in lista:
#     final += i.capitalize() + " "

# print(final.strip())

for j in range(len(s)):
    if j == 0 or s[j-1] == ' ':
        final += s[j].capitalize()
    else:
        final += s[j]

print(final)