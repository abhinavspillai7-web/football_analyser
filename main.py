import validation
import team
import player
while True:
    inp1=input("enter team formation(format:defenders–midfielders–forwards):")
    inp1=inp1.strip()
    result=validation.validate_formations(inp1)
    if result==True:
        print("valid formation")
        break
    else:
        print("invalid formation")
strengths=input("enter strengths:")
strengths=strengths.split(",")
new_strengths=[]
for i in strengths:
    new_strengths.append(i.strip())
print(new_strengths)
weaknesses=input("enter weaknesses:")
weaknesses=weaknesses.split(",")
new_weaknesses=[]
for i in weaknesses:
    new_weaknesses.append(i.strip())
print(new_weaknesses)
players=[]
jersey_numbers=set()
for i in range(11):
    player_name=input("enter player name:")
    while True:
        jerseyno=int(input("enter jersey no:"))
        if jerseyno<=99 and jerseyno>=1 and jerseyno not in jersey_numbers:
            jersey_numbers.add(jerseyno)
            break
        else:
            print("invalid jersey number")
    player_position=input("enter player position:")
    new_player=player.Player(jerseyno,player_name,player_position)
    players.append(new_player)
key_players=set()
for i in range(3):
    while True:
        key_jersey=int(input("enter jersey no:"))
        if key_jersey in jersey_numbers and key_jersey not in key_players:
            key_players.add(key_jersey)
            break
        else:
            print("invalid")
key_players_attribute=[]
for i in players:
    if i.jersey_no in key_players:
        key_players_attribute.append(i)
for i in key_players_attribute:
    strengths=input("enter strengths:")
    strengths=strengths.split(",")
    processed_strengths=[]
    for j in strengths:
        processed_strengths.append(j.strip())
    i.strengths=processed_strengths
    weaknesses=input("enter weaknesses:")
    weaknesses=weaknesses.split(",")
    processed_weaknesses=[]
    for k in weaknesses:
        processed_weaknesses.append(k.strip())
    i.weaknesses=processed_weaknesses
our_team=team.Team(inp1,new_strengths,new_weaknesses,players)
