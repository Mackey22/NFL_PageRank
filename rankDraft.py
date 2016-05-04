#! /usr/bin/python
# rankDraft.py
import csv
import os
import constants
import teams
import weights
import pageRanks
import rankOverTime

# Setup weight class
team = teams.Teams()
weight = weights.Weights(team)

def noEmptyStrings(item):
	return type(item) is int

with open('Charts/draft.csv', 'w+') as chart:
	chart.write('Years,')
	for i in range(31):
		chart.write(str(i + 1) + ',')
	chart.write(str(32) + '\n')
	for filename in os.listdir('Results'):
		weight.refresh()
		with open('Results/' + filename) as results:
			reader = csv.reader(results)
			teamsInPlayoffs = [False for i in range(32)]
			confChamp = []
			div = []
			wc = []
			notInPlayoffs = []
			numInPlayoffs = 0
			for row in reader:
				if len(row) == 0 or row[0] == 'Week' or row[0] == '':
					continue
				week = row[0]
				winner = team.getTeamNum(row[4])
				winnerName = row[4]
				loser = team.getTeamNum(row[6])
				loserName = row[6]
				if (type(rankOverTime.intify(week)) is int):				
					if row[7] == row[8]:
						weight.recordGame(winnerName, loserName, True, True)
					else:
						weight.recordGame(winnerName, loserName, True)
				elif week == "SuperBowl":
					weight.orderTeams([winner], 0, 0)
					weight.orderTeams([loser], 1, 1)
					teamsInPlayoffs[winner] = True
					teamsInPlayoffs[loser] = True
				elif week == "ConfChamp":
					teamsInPlayoffs[loser] = True
					confChamp.append(loser)
				elif week == "Division":
					teamsInPlayoffs[loser] = True
					div.append(loser)
				elif week == "WildCard":
					teamsInPlayoffs[loser] = True
					wc.append(loser)
			for i in range(32):
				if teamsInPlayoffs[i]:
					numInPlayoffs += 1
				else: 
					notInPlayoffs.append(i)
			weight.orderTeams(confChamp, 2, 3)
			weight.orderTeams(div, 4, 7)
			weight.orderTeams(wc, 8, 11)
			weight.orderTeams(notInPlayoffs, numInPlayoffs, 31)
		chart.write(filename[:4] + ',' + weight.toDraftOrder())













