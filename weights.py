import csv
import os
from constants import * 

class Weights:
	'''class to keep track of the weights from one team to another'''
	def __init__(self, teams):
		global NUM_TEAMS
		self.wins = [[0 for i in range(NUM_TEAMS)] for j in range(NUM_TEAMS)]
		self.norm = [[0 for i in range(NUM_TEAMS)] for j in range(NUM_TEAMS)]
		self.numGames = [0 for i in range(NUM_TEAMS)]
		self.teams = teams	

	def recordGame(self, winner, loser, playoffs, tie=False):
		numLos = self.teams.getTeamNum(loser)
		numWin = self.teams.getTeamNum(winner)
		if playoffs:
			self.numGames[numLos] += 1
		self.numGames[numWin] += 1
		if tie:
			self.wins[numLos][numWin] += 0.5
			self.wins[numWin][numLos] += 0.5
		else:
			self.wins[numLos][numWin] += 1

	def reduce(self):
		global NUM_TEAMS
		for i in range(NUM_TEAMS):
			totalLosses = 0
			for j in range(NUM_TEAMS):
				totalLosses += self.wins[i][j]
				if totalLosses == 0:
					totalLosses = 1
			for k in range(NUM_TEAMS): 
				self.norm[i][k] = float(self.wins[i][k]) / totalLosses

	def __str__(self):
		global NUM_TEAMS
		retString = "\n"
		for i in range(NUM_TEAMS):
			retString += str(self.norm[i]) + '\n\n'
		return retString

	def getNumGames(self, teamNum):
		return self.numGames[teamNum]

	def refresh(self):
		global NUM_TEAMS
		self.wins = [[0 for i in range(NUM_TEAMS)] for j in range(NUM_TEAMS)]
		self.norm = [[0 for i in range(NUM_TEAMS)] for j in range(NUM_TEAMS)]
		self.numGames = [0 for i in range(NUM_TEAMS)]

