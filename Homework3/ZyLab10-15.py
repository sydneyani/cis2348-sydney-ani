#Sydney Ani PID: 1869076

class Team:
    def __init__(self):
        self.name = 'none'
        self.team_wins = 0
        self.team_losses = 0

    def get_win_percentage(self):
        win_percentage = 0
        if self.team_wins + self.team_losses != 0:
            win_percentage = self.team_wins / (self.team_wins + self.team_losses)
        return win_percentage

    def print_standing(self):
        if self.get_win_percentage() >= 0.5:
            print('Congratulations, Team', self.name, 'has a winning average!')
        else:
            print('Team', self.name, 'has a losing average.')


if __name__ == '__main__':
    student_team = Team()
    student_team.name = input()
    student_team.team_wins = int(input())
    student_team.team_losses = int(input())

    student_team.print_standing()

    # Perform the tests for get_win_percentage()
    test1_result = student_team.get_win_percentage() == 0.8125 and student_team.team_wins == 13 and student_team.team_losses == 3
    test2_result = student_team.get_win_percentage() == 0.4 and student_team.team_wins == 80 and student_team.team_losses == 120
