import Mylibrary

midterm = int(input('Enter Midterm Point (100 point)-> 30% : '))
final = int(input('Enter Final Point (100 point)-> 50% : '))
homework = int(input('Enter Homework Point (100 point) -> 20% : '))

midterm = Mylibrary.calToPercent(midterm, 100, 30)
final = Mylibrary.calToPercent(final, 100, 50)
homework = Mylibrary.calToPercent(homework, 100, 20)

print('You Point : {:.0f}'.format(midterm + final + homework))
print('You Grade : {}'.format(Mylibrary.calGrade(midterm + final + homework)))
