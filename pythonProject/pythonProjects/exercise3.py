name = input("Enter your name: \n")
print("Hello " + name + ", welcome to this program that will help you calculate your gpa for this semester")

credit_units = list()
course_units = list()
student = list()
total_point = 0.0

number = int(input("Enter the no of course units your doing this semester:\n"))
count = 0
while count < number:
    count = count + 1

    course_name = input(f"Enter the name of the course unit {count} :\n")
    course_units.append(course_name)

    marks = int(input(f"Enter the target marks in the course unit {count} \n"))
    student.append(marks)

    credit_unit = int(input(f"Enter the credit unit in the course unit {count} \n"))
    credit_units.append(credit_unit)

print(f'{course_units}, {student}, {credit_units}')

counter = 0
for mark in student:
    if 80 <= float(mark) <= 100:
        grade = 'A'
        print(f"For {course_units[counter]}, grade is {grade}")
        grade_point = 5.0
        total_point += (credit_units[counter] * grade_point)

    elif float(mark) >= 75:
        grade = 'B+'
        print(f"For {course_units[counter]}, grade is {grade}")
        grade_point = 4.5
        total_point += (credit_units[counter] * grade_point)

    elif float(mark) >= 70:
        grade = 'B'
        print(f"For {course_units[counter]}, grade is {grade}")
        grade_point = 4.0
        total_point += (credit_units[counter] * grade_point)

    elif float(mark) >= 65:
        grade = 'C+'
        print(f"For {course_units[counter]}, grade is {grade}")
        grade_point = 3.5
        total_point += (credit_units[counter] * grade_point)

    elif float(mark) >= 60:
        grade = 'C'
        print(f"For {course_units[counter]}, grade is {grade}")
        grade_point = 3.0
        total_point += (credit_units[counter] * grade_point)

    elif float(mark) >= 55:
        grade = 'D+'
        print(f"For {course_units[counter]}, grade is {grade}")
        grade_point = 2.5
        total_point += (credit_units[counter] * grade_point)

    elif float(mark) >= 50:
        grade = 'D'
        print(f"For {course_units[counter]}, grade is {grade}")
        grade_point = 2.0
        total_point += (credit_units[counter] * grade_point)

    elif float(mark) < 50:
        grade = 'F'
        print(f"For {course_units[counter]}, grade is {grade}")
        grade_point = 0
        total_point += (credit_units[counter] * grade_point)

    counter = counter + 1

total_credit_units = sum(credit_units)
print('total credit units is:', total_credit_units)

print('total_point:', total_point)

gpa = total_point / total_credit_units
print(f' hello {name}, your gpa is {gpa}')

if 4.40 <= gpa <= 5.0:
    print("You have a first class degree")
elif gpa >= 3.60:
    print("You have a second class upper")
elif gpa >= 3.00:
    print("You have a second class lower")
elif gpa >= 2.50:
    print("You have a pass")
elif gpa < 2.50:
    print("You have failed")

# End of grade computation and calculation of gpa
# improvement in the grades and gpa after increase in the target by 5%

print('if you can only increase your target marks by 5% you have a greater difference in your grade and gpa: ')
marks = marks + (5 / 100 * marks)
