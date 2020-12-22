def basicList():
    height = [150, 170, 163, 167, 180, 192]
    print('{}'.format(height))
    print('{}'.format(type(height)))
    print('{}'.format(height[0]))
    height[0] = 168
    print('{}'.format(height))
    height.remove(170)
    print('{}'.format(height))
    height += [120, 130]
    print('{}'.format(height))
    height.append(188)
    print('{}'.format(height))
    print('{}'.format(height.__len__()))
    print('{}'.format(sorted(height)))
    print('{}'.format(sorted(height, reverse=True)))
    print('{}'.format(max(height)))
    print('{}'.format(min(height)))


def TraverseList():
    height = [150, 170, 163, 167, 180, 192]
    for i in height:
        print('--- {}'.format(i))
    for i in range(len(height)):
        print('>>> {}'.format(i))
    for i, v in enumerate(height):
        print('>>> {} {}'.format(i, v))


def SlicingList():
    height = [150, 170, 163, 167, 180, 192]
    print('{}'.format(height))
    print('{}'.format(height[2:3:2]))
    print('{}'.format(height[-1::-1]))


def List_Comperhension():
    ThaiBaht = [15000, 20000, 6500, 15241, 18754]
    UsDollar1 = [i / 30 for i in ThaiBaht]
    UsDollar2 = ['{:.2f}'.format(i / 30) for i in ThaiBaht]
    print('{}'.format(ThaiBaht))
    print('{}'.format(UsDollar1))
    print('{}'.format(UsDollar2))


if __name__ == '__main__':
    basicList()
    TraverseList()
    SlicingList()
    List_Comperhension()
