premier_league_2017_2018 = [["Manchester City", (32, 4, 2)], ["Manchester United", (25, 6, 7)],
                            ["Tottenham", (23, 8, 7)], ["Liverpool", (21, 12, 5)],
                            ["Chelsea", (21, 7, 10)], ["Arsenal", (19, 6, 13)], ["Burnley", (14, 12, 12)],
                            ["Everton", (13, 10, 15)], ["Leicester", (12, 11, 15)], ["Newcastle", (12, 8, 18)],
                            ["Crystal Palace", (11, 11, 16)], ["Bournemouth", (11, 11, 16)], ["WestHam", (10, 12, 16)],
                            ["Watford", (11, 8, 19)], ["Brighton", (9, 13, 16)],
                            ["Huddersfield", (9, 10, 19)], ["Southampton", (7, 15, 16)], ["Swansea", (8, 9, 21)],
                            ["Stoke", (7, 12, 19)], ["West Bromwich", (6, 13, 19)]]


# ชนะ 3 คะแนน เสมอ 1

def line():
    print("-" * 30)


def show_final_result(list):
    premier_league_win_score = []
    for i in range(list.__len__()):
        premier_league_win_score.append([i + 1, list[i][0], (list[i][1][0] * 3) + (list[i][1][1])])
    for i in range(premier_league_win_score.__len__()):
        if i == 4 or i == 17:
            line()
        print('{:<3} {:<20} {:>3}'.format(premier_league_win_score[i][0], premier_league_win_score[i][1],
                                          premier_league_win_score[i][2]))


def lose_morethan_draw(list):
    premier_league_lose_morethan_draw = []
    for i in range(list.__len__()):
        if list[i][1][2] - list[i][1][1] > 0:
            premier_league_lose_morethan_draw.append([list[i][0], list[i][1][2] - list[i][1][1]])
    for i in range(premier_league_lose_morethan_draw.__len__()):
        print('{:<20} {:>3}'.format(premier_league_lose_morethan_draw[i][0], premier_league_lose_morethan_draw[i][1]))


if __name__ == '__main__':
    show_final_result(premier_league_2017_2018)
    lose_morethan_draw(premier_league_2017_2018)
