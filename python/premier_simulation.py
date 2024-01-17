from random import randint


DISPLAY_MESSAGE = """
Welcome to the Premier League's "Big Six" classification simulation
"""


class PremierLeague:
    points = {
        'Manchester United' : 0,
        'Liverpool' : 0,
        'Arsenal' : 0,
        'Chelsea' : 0,
        'Manchester City' : 0,
        'Tottenham Hotspur' : 0,
    }

    def __play_game(self, team1, team2):
        points_team1 = randint(0, 5)
        points_team2 = randint(0, 5)

        if points_team1 > points_team2:
            self.points[team1] += 3
        elif points_team1 == points_team2:
            self.points[team1] += 1
            self.points[team2] += 1
        else:
            self.points[team2] += 3


    def __simulate(self):
        teams = list(self.points.keys())
        teams2 = teams.copy()

        for team in teams:
            teams2.remove(team)
            if len(teams2) == 0:
                break
            for team2 in teams2:
                self.__play_game(team, team2)
                self.__play_game(team, team2)
                self.__play_game(team, team2)

    def __sort_teams(self):
        teams = [{'name': team, 'points': points} for team, points in self.points.items()]
        teams.sort(key=lambda d: d['points'], reverse=True)
        self.__result = teams

    def __display_result(self):
        print(DISPLAY_MESSAGE)
        for index, team in enumerate(self.__result):
            if index == 0:
                print(f"AND THE WINNER, WITH {team['points']} POINTS, IS:")
                print(f"{'*'*10} {team['name']} {'*'*10}")
                print('Classification:')
            else:
                print(f"{index + 1}.- {team['name']}, {team['points']} points")


    def main(self):
        self.__simulate()
        self.__sort_teams()
        self.__display_result()

def run():
    premier = PremierLeague()
    premier.main()


if __name__ == '__main__':
    run()
