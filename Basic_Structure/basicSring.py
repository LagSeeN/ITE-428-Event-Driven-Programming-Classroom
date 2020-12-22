def testString():
    Universiy = "Thai-Nichi Institute "
    Universiy = Universiy.strip()
    Universiy = Universiy + " of Technology"

    print('{}'.format(Universiy.split(' ')))
    List_Universiy = Universiy.split(' ')
    for i in List_Universiy:
        print(('-- {}'.format(i)))
    print('>> {}'.format(List_Universiy[0]))
    for i in range(List_Universiy.__len__()):
        print('-- {}'.format(List_Universiy[i]))
    print('{}'.format(Universiy))
    print('{}'.format(type(Universiy)))
    print('{}'.format(Universiy[2:8:2]))
    print('{}'.format(Universiy[:8:]))
    print('String Size = {}'.format((len(Universiy))))
    print('String Size = {}'.format(Universiy.__len__()))
    print('LOWER = {}'.format(Universiy.lower()))
    print('UPPER = {}'.format(Universiy.upper()))
    print('capitalize = {}'.format(Universiy.capitalize()))
    for i in Universiy:
        print('{}'.format(i))


def practicesSlide54():
    total = 0;
    print('Senior : 65 up \nAdult  : 18-64 \nJunior : 4-17\nChild  : 0-3')
    List_Guest = input('Enter number of Senior,Adult,Junior,Child ').split(',')
    for i in range(List_Guest.__len__()):
        if i == 0:
            total += int(List_Guest[i]) * 19.95
        elif i == 1:
            total += int(List_Guest[i]) * 22.95
        elif i == 2:
            total += int(List_Guest[i]) * 14.95
    print('Total of Ticket = {:,.2f}'.format(total))


def practicesSlide56():
    fullname = input('Please Enter your full name : ').split(' ')
    print('Yor Thai-Nichi student E-mail is \"{}\"'.format(
        (fullname[1][:2:] + '.' + fullname[0] + '@tni.ac.th\"').lower()))


if __name__ == '__main__':
    practicesSlide56()
