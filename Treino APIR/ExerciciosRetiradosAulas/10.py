def matchMaker():
	teams = ["FCP","SCP","SLB"]
	allMatches=[]
	for home in teams:
		for away in teams:
			if home!=teams:
				allMatches.append((home,away))
                
                
                
	return allMatches

print(matchMaker())
	