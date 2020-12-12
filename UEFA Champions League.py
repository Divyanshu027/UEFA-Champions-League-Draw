import random

Others=['Arsenal (ENG)','Astana (KAZ)','Atlético (ESP)','BATE (BLR)','CSKA Moskva (RUS)','Dinamo Zagreb (CRO)','Dynamo Kyiv (UKR)','Galatasaray (TUR)','Gent (BEL)','Leverkusen (GER)','Lyon (FRA)','M. Tel-Aviv (ISR)','Malmö (SWE)','Man. City (ENG)','Man. United (ENG)','Mönchengladbach (GER)','Olympiacos (GRE)','Porto (POR)','Real Madrid (ESP)','Roma (ITA)','Sevilla (ESP)','Shakhtar Donetsk (UKR)','Valencia (ESP)','Wolfsburg (GER)']
DomesticLeagueChampions=['Barcelona (ESP)','Bayern (GER)','Benfica (POR)','Chelsea (ENG)','Juventus (ITA)','Paris (FRA)','PSV (NED)','Zenit (RUS)'] 
Group=[]
s=65
while len(Others)> 0:
    if len(Group)==0:
        a=random.randint(0,len(DomesticLeagueChampions)-1)
        Group.append(DomesticLeagueChampions[a])
        DomesticLeagueChampions.remove(DomesticLeagueChampions[a])
    b=random.randint(0,len(Others)-1)
    team=Others[b]    
    team_arr=team.split(" ")
    count=0 
    for i in Group:
      d=team_arr[-1]
      if d in i:
        count=1
        break
    if count==0:
      Group.append(team)
      Others.remove(team)
    if len(Group)==4 or len(Others)==0 :
      print("Group" + chr(s))
      s=s+1
      for k in Group:
        print(k)
      print("\n")
      Group.clear()        
