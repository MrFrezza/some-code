grades_count = int(input().rstrip())

grades = []

for _ in range(grades_count):
    grades_item = int(input().strip())
    grades.append(grades_item)


final = []
for i in grades:
    if i < 38:
        final.append(i)
    else:
        a = 1
        t = True
        while a < 3:
            if (i+a)%5 == 0:
                final.append(i+a)
                t = False
                break            
            a += 1
        
        if t:
            final.append(i)

print(final)