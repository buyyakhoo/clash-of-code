weight = int(input())
feet, inches = [int(i) for i in input().split()]

bmi = round(703 * (weight / ((feet * 12) + inches) ** 2), 1)
print(bmi)

if bmi >= 30:
    print('Obese')
elif bmi >= 25:
    print('Overweight')
elif bmi >= 18.5:
    print('Normal')
elif bmi < 18.5:
    print('Underweight')