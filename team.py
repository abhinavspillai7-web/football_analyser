import player
class Team:
    def __init__(self,formation,strengths,weaknesses,players):
        self.formation=formation
        self.strengths=strengths
        self.weaknesses=weaknesses
        self.players=players
player1=player.Player("lw",["aerial ability","positioning"],["defence","dribbling"])
player2=player.Player("rw",["set-pieces","positioning"],["defence","shooting"])
player3=player.Player("lb",["speed","passing"],["defence","dribbling"])
players=[player1,player2,player3]
team=Team("4-3-3",["High pressing","Quick counter-attacks"],["Vulnerable to counter-attacks","Weak against high press"],players)
print("formation:",team.formation)
print("strengths:",team.strengths)
print("weaknesses:",team.weaknesses)
print("postion:",team.players[0].position)