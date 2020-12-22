import operator

Student_Score = []
print('{}'.format(Student_Score))
avg = 0
while True:
    Name = input('Enter StudentName : ')
    Score = int(input('Enter StudentScore : '))
    avg += Score
    Student_Score.append([Name, Score])
    if input('Stop Y / y ').upper() == 'Y': break

avg /= Student_Score.__len__()
Student_Score_sorted = sorted(Student_Score, reverse=True, key=operator.itemgetter(1))

for i in range(Student_Score_sorted.__len__()):
    print('{} {:<10} {:>3} '.format(i + 1, Student_Score_sorted[i][0], Student_Score_sorted[i][1]), end='')
    if int(Student_Score_sorted[i][1]) > avg:
        print('+{:.2f}'.format(int(Student_Score_sorted[i][1]) - avg))
    else:
        print('-')
