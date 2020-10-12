grade_input = float(input("what is the grade?"))
def grade_rounding(g):
    if g >= 6:
        if 0.25<= g%1 <0.75:
            grade = int(g) + 0.5
            return "grade " + str(g) + " is rounded to a " + str(grade) + " and is a pass"
    else:
        grade = round(g)
        return "grade " + str(g) + " is rounded to a " + str(grade) + " and is a fail"

print (grade_rounding(grade_input)
