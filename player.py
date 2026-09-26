class player:
    def __init__(self,position,strengths,weaknesses):
        self.position=position
        self.strengths=strengths
        self.weaknesses=weaknesses
position1="lw"
strengths1=["areial ability","accuracy"]
weaknesses1=["weak defence"," weak during counter attack"]
pl=player(position1,strengths1,weaknesses1)
print("postion:",pl.position)
print("strengths:",pl.strengths)
print("weaknesses:",pl.weaknesses)
