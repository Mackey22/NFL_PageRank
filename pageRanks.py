from constants import *
import copy
import os
import operator

class pageRanks:
	def __init__(self, weights, teams, normalize):
		self.vals = [1.0 / NUM_TEAMS for i in range(NUM_TEAMS)]
		self.teams = teams
		self.weights = weights
		self.rank()
		if normalize:
			self.normalize()

	def normalize(self):
		total = 0
		for teamNum in range(32):
			nGames = self.weights.getNumGames(teamNum)
			if nGames == 0: 
				nGames = -1
			val = self.vals[teamNum] / nGames
			if nGames == 0: 
				val = 0;
			self.vals[teamNum] = val
			total += val
		for teamNum in range(32):
			self.vals[teamNum] = round(self.vals[teamNum] / total, 7)

	def rank(self):
		for i in range(40):
			self.step()

	def step(self):
		global NUM_TEAMS
		currRanks = copy.deepcopy(self.vals)
		for j in range(NUM_TEAMS):
			jsRank = 0.0
			for k in range(NUM_TEAMS):
				jsRank += currRanks[k] * self.weights.norm[k][j]
			self.vals[j] = jsRank

	def __str__(self):
		global NUM_TEAMS
		print self.toOrder()
		string = '' 
		cop = copy.deepcopy(self.vals)
		valDict = {}
		for i in range(NUM_TEAMS):
			valDict[self.teams.getTeamName(i)] = self.vals[i]
		sortedDict = sorted(valDict.items(), key=operator.itemgetter(1), reverse=True)
		total = 0.0
		for (key, val) in sortedDict:
			numGames = self.weights.getNumGames(self.teams.getTeamNum(key))
			string += key + ': \t' + str(val) + '\t ' + str(numGames) + '\n'
			total += val
		return string + str(total)

	def toOrder(self):
		global NUM_TEAMS		
		ranks = ""
		valDict = {}
		for i in range(NUM_TEAMS):
			valDict[self.teams.getTeamName(i)] = self.vals[i]
		sortedDict = sorted(valDict.items(), key=operator.itemgetter(1), reverse=True)
		for (key, val) in sortedDict:
			ranks += key + ","
		ranks = ranks[0 : -1]
		return ranks



	def toCsv(self):
		ranks = ""
		for i in range(NUM_TEAMS - 1):
			ranks += str(self.vals[i]) + ','
		ranks += str(self.vals[NUM_TEAMS - 1]) + '\n'
		return ranks

