# 9. A school has the following rules for grading system:
# i) Below 50 – F; ii) 50 to 60 – D; iii) 60 to 70 – C; iv) 70 to 80 – B; v) Above 80 – A
# • Ask user to enter marks and print the corresponding grade.

marks = int(input("Enter marks: "))

if marks > 100 and marks < 0:
    print('Enter correct marks')
elif marks > 80:
    print('Your Grade is : A')
elif marks >= 70:
    print('Your Grade is : B')
elif marks >= 60:
    print('Your Grade is : C')
elif marks >= 50:
    print('Your Grade is : D')
else:
    print('Your Grade is : F')
