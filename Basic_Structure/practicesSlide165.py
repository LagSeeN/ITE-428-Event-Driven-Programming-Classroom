area = [(2, 4), (5, 10), (7, 1)]

print('Area = 1/2 | {}({}-{})-{}({}-{})-{}({}-{}) |'.format(area[0][0], area[1][1], area[2][1],
                                                            area[1][0], area[0][1], area[2][1],
                                                            area[2][0], area[0][1], area[1][1]))
print('Area = {}'.format(1 / 2 * (int(area[0][0]) * int((area[1][1]) - int(area[2][1])) -
                                  int(area[1][0]) * int((area[0][1]) - int(area[2][1])) -
                                  int(area[2][0]) * int((area[0][1]) - int(area[1][1])))))
