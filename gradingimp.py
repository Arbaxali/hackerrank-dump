# mysolution

grades  =[22, 25, 35, 48,78,56,97,233]
new  = []



def grad(num):
    n  = 0 
    while (n < 2):
        num += 1
        n+=1

    return num
for i in grades:
    if i > 38 and i % 5 >= 3:
        num = i
        s =  grad(num) 
        new.append(s)
    else :
        new.append(i)

print(new)

# hackerrank solution
def gradingStudents(grades):
    new_grades = []
    for grade in grades:
        if grade >= 38 and grade%5 >= 3:
            s = (grade+(5-grade%5))
            new_grades.append(s)
        else:
            new_grades.append(grade)
    return(new_grades)

s = gradingStudents(grades)

print(s)
