AllMatches=[]
teams=["A", "B"]
def allMatches(teams):
   assert len(teams) >= 2, "Requires two or more teams!"
   for casa in teams:
      for fora in teams:
         if casa==fora:
            continue
         else:
            AllMatches.append((casa, fora))
   return AllMatches
print(allMatches(teams))