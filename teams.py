import csv
import os

class Teams:
	# teams maps team Name -> team Number
	# oppTeams maps team Number -> team Name
	def __init__(self):
		self.teamNum = 0
		self.teams = {}
		self.oppTeams = {}
		self.mapTeams()

	def mapTeams(self):
		# for filename in os.listdir('Results'):
			# with open('Results/' + filename) as results:
		with open('Results/2007.csv') as results:
			reader = csv.reader(results)
			for row in reader: 
				if len(row) == 0 or row[0] == 'Week' or row[0] == '':
					continue
				if row[4] not in self.teams:
					self.addTeam(row[4])
				if row[6] not in self.teams:
					self.addTeam(row[6])
		# Adding old team names to mapping
		keys = self.teams.keys
		self.checkAdd(keys, 'Houston Oilers', 'Tennessee Titans')
		self.checkAdd(keys, 'Tennessee Oilers', 'Tennessee Titans')
		self.checkAdd(keys, 'St. Louis Cardinals', 'Arizona Cardinals')
		self.checkAdd(keys, 'Phoenix Cardinals', 'Arizona Cardinals')
		self.checkAdd(keys, 'Boston Patriots', 'New England Patriots')
		self.checkAdd(keys, 'Los Angeles Rams', 'St. Louis Rams')
		self.checkAdd(keys, 'Baltimore Colts', 'Indianapolis Colts')
		self.checkAdd(keys, 'Los Angeles Raiders', 'Oakland Raiders')
		return self.teamNum


	def addTeam(self, teamName):
		self.teams[teamName] = self.teamNum
		self.oppTeams[self.teamNum] = teamName
		self.teamNum += 1

	def checkAdd(self, keys, old, new):
		# if new in keys:
		self.teams[old] = self.teams[new]
		# else:
		# self.addTeam(old)

	def getTeamNum(self, name):
		return self.teams[name]

	def getTeamName(self, num):
		return self.oppTeams[num]

	def delTeam(self, name):
		del self.teams[name]