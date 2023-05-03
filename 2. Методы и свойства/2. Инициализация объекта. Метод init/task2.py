class SoccerPlayer:
    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname
        self.goals, self.assists = 0, 0

    def score(self, goals: int = 1):
        self.goals += goals

    def make_assist(self, assists: int = 1):
        self.assists += assists

    def statistics(self):
        print(f'{self.surname} {self.name} - goals: {self.goals}, assists: {self.assists}')


leo = SoccerPlayer('Leo', 'Messi')
leo.score(720)
leo.make_assist(500)
leo.statistics()

kokorin = SoccerPlayer('Alex', 'Kokorin')
kokorin.score()
kokorin.statistics()
kokorin.make_assist()
kokorin.statistics()
