#! /usr/bin/python
# pagerank.py
import csv
import os
import constants
import teams
import weights
import pageRanks


# Setup weight class
team = teams.Teams()
weight = weights.Weights(team)

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

# Update the rows and end up with the final weights for each edge
for filename in os.listdir('Results'):
	with open('Results/' + filename) as results:
		reader = csv.reader(results)
		for row in reader:
			if len(row) == 0 or row[0] == 'Week' or row[0] == '':
				continue
			playoffs = (type(intify(row[0])) is int)
			print(playoffs)
			if row[7] == row[8]:
				weight.recordGame(row[4], row[6], playoffs, True)
			else:
				weight.recordGame(row[4], row[6], playoffs)
weight.reduce()

pr = pageRanks.pageRanks(weight, team, True)

print(pr)

# Things to remark on 
# Difference in 1 iteration vs. converging iteration - Difficulty of schedule/division
# Changes of a team year after year
# Try adjusting for playoffs

# Things to do
# Add damping factor
# Generalize to allow for user input - For instance, checking by weeks/months
# adjust for number of games played







