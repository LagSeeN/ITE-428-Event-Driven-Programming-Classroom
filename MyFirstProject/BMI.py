from Mylibrary import CalBMI, line

height = float(input('Please enter your height (cm) : '))
weight = float(input('Please enter your weight (kg) : '))

line()
print("YOUR BMI = {:.2f}".format(CalBMI(weight, height)))
line()
if CalBMI(weight, height) > 10:
    print('Good')
elif CalBMI(weight, height) < 5:
    print('So so')
else:
    print('Bad')
line()
