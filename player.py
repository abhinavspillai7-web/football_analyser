class Player:
    def __init__(self,jersey_no,name,position,strengths=None,weaknesses=None):
        self.position=position
        if strengths is None:
            self.strengths=[]
        else:
            self.strengths=strengths
        if weaknesses is None:
            self.weaknesses=[]
        else:
            self.weaknesses=weaknesses
        self.name=name
        self.jersey_no=jersey_no

