#! /usr/bin/python
# pagerank.py
import csv
import os
import constants
import teams
import weights
import pageRanks


def intify(word):
	if word == '1':
		return 1
	elif word == '2':
		return 2
	elif word == '3':
		return 3
	elif word == '4':
		return 4
	elif word == '5':
		return 5
	elif word == '6':
		return 6
	elif word == '7':
		return 7
	elif word == '8':
		return 8
	elif word == '9':
		return 9
	elif word == '10':
		return 10
	elif word == '11':
		return 11
	elif word == '12':
		return 12
	elif word == '13':
		return 13
	elif word == '14':
		return 14
	elif word == '15':
		return 15
	elif word == '16':
		return 16
	elif word == '17':
		return 17
	else: 
		return word

# Setup weight class
team = teams.Teams()
weight = weights.Weights(team)

# with open('Charts/overtime.csv', 'w+') as chart:
# 	chart.write('Years,')
# 	for i in range(31):
# 		chart.write(team.getTeamName(i) + ',')
# 	chart.write(team.getTeamName(31) + '\n')
# 	for filename in os.listdir('Results'):
# 		weight.refresh()
# 		with open('Results/' + filename) as results:
# 			reader = csv.reader(results)
# 			for row in reader:
# 				if len(row) == 0 or row[0] == 'Week' or row[0] == '':
# 					continue
# 				playoffs = (type(intify(row[0])) is int)
# 				if row[7] == row[8]:
# 					weight.recordGame(row[4], row[6], playoffs, True)
# 				else:
# 					weight.recordGame(row[4], row[6], playoffs)
# 		weight.reduce()
# 		pr = pageRanks.pageRanks(weight, team, True)
# 		chart.write(filename[:4] + ',' + pr.toCsv())

with open('Charts/rankingsRegSeason.csv', 'w+') as chart:
	chart.write('Years,')
	for i in range(31):
		chart.write(str(i + 1) + ',')
	chart.write(str(32) + '\n')
	for filename in os.listdir('Results'):
		weight.refresh()
		with open('Results/' + filename) as results:
			reader = csv.reader(results)
			for row in reader:
				if len(row) == 0 or row[0] == 'Week' or row[0] == '':
					continue
				playoffs = (type(intify(row[0])) is int)
				# Not counting playoff games!!
				if not playoffs:
					continue
				if row[7] == row[8]:
					weight.recordGame(row[4], row[6], playoffs, True)
				else:
					weight.recordGame(row[4], row[6], playoffs)
		weight.reduce()
		pr = pageRanks.pageRanks(weight, team, True)
		chart.write(filename[:4] + ',' + pr.toOrder())

# Things to remark on 
# Difference in 1 iteration vs. converging iteration - Difficulty of schedule/division
# Changes of a team year after year
# Try adjusting for playoffs
# The Question of adjusting for having more playoff games. Trouble of adjusting for games in general

# Things to do
# Add damping factor
# Generalize to allow for user input - For instance, checking by weeks/months
# adjust for number of games played







