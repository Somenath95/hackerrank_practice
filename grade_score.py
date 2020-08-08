grade = int(input())

rem = grade%5
print(rem)
if grade < 38:
    print(grade)

elif (grade > 40) & (rem >= 3):
    grade = grade + (5 - rem)
    print(grade)

else:
    print(grade)    