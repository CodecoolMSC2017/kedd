import sys

def solve(grades):
    a=[]
    for grade in grades:
        if grade <= 38:
                a.append(grade)
        else:
            if grade % 10 == 7:
                a.append(grade)
            elif grade % 10 == 3:
                grade +=2
                a.append(grade)
            elif grade % 10 < 5:
                if grade % 5 < 3:
                    grade-= (grade % 5)
                elif grade % 5 > 3:
                    grade+=1
                a.append(grade)
            elif grade % 10 > 5:
                if grade % 5 < 3:
                    grade-= (grade % 5)
                elif grade % 5 > 3:
                    grade+=1
                elif grade % 5 == 3:
                    grade+=2
                a.append(grade)
    return a    # Complete this function

n = int(input().strip())
grades = []
grades_i = 0
for grades_i in range(n):
   grades_t = int(input().strip())
   grades.append(grades_t)
result = solve(grades)
print ("\n".join(map(str, result)))
