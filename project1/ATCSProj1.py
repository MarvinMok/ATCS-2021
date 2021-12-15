#ATCS Project 1, Data Science
#Bpopularity: Marvin Mok

import pandas as pd 
#import numppopularity as np
#import random
#import seaborn as sns
import matplotlib.pyplot as plt

import csv

pd.set_option("display.max_columns", None)
#info = pd.read_csv("statistics.csv")
#playerCounts = pd.read_csv("Steam Games - OrderedCounts.csv")
data = pd.read_csv("finalstats.csv")
#print(len(df))
#t = info.to_dict(orient='index')


'''
Takes in DataFrame df 
Displays their popularity over time as a line graph.
'''
def displayPopularity(df):

	#months
	time = [5, 4, 3, 2, 1, 0]

	#loops through, plotting points 
	for i in range(0,50):
		popularity = [df['October 2021'].iloc[i], df['September 2021'].iloc[i], df['August 2021'].iloc[i], 
	df['July 2021'].iloc[i], df['June 2021'].iloc[i], df['May 2021'].iloc[i]]
		if popularity[0] > 200000:
			plt.plot(time, popularity)


	plt.show()

'''
Takes in DataFrame df.
Graphs price of a game vs. its popularity in a scatterplot, color-coded
based on price ranges. 
Returns: a list of numbers of games in certain price ranges
'''
def pricePopularity(df):
	
	prices = [0, 0, 0, 0, 0]
	names = []

	#labels
	plt.xlabel('Price')
	plt.ylabel('Player Count')

	#loops thrugh df, plotting points
	for i in range(6, 50):
		popularity = df.iloc[i]['countAverage']

		price = df.iloc[i]['initialprice'] / 100
		if price == 0:
			Color = "red"
			prices[0] += 1
		elif price <= 20:
			prices[1] += 1
			Color = "orange"
		elif price <= 40:
			prices[2] += 1
			Color = "green"
		elif price > 59 and price < 60:
			Color = "purple"
			prices[4] += 1
		else:
			Color = "blue"
			prices[3] += 1


		plt.plot(price, popularity, 'o', color=Color)
	

	return prices

'''
Takes in DataFrame df
Graphs the positive review percentage of a game vs popularity, color-coded 
based on different ranges of review percentage.
Returns: a list of the number of games in each review percent range
'''
def reviewPopularity(df):

	#labels
	plt.xlabel('Review Percentage')
	plt.ylabel('Player Count')
	
	ranges = [0, 0, 0, 0]

	#loops through df, placing points
	for i in range(6, 50):
		popularity = df.iloc[i]['countAverage']

		reviewPercent = df.iloc[i]['reviewPercent']
		if reviewPercent <= 0.7:
			pointColor = "red"
			ranges[0] += 1
		elif reviewPercent <= 0.8:
			pointColor = "orange"
			ranges[1] += 1
		elif reviewPercent <= 0.9:
			pointColor = "green"
			ranges[2] += 1
		else:
			pointColor = 'blue'
			ranges[3] += 1


		plt.plot(reviewPercent, popularity, 'o', color=pointColor)
		#else: 
			#plt.plot(reviewPercent, 200000, 'o', color="purple")
	return ranges

'''
Takes in DataFrame df
Displays an ordered bar graph based on a tag's popularity
Returns: A tuple with two values. The first is dictionary tagPopularity
with a tag as the key and the number of times it appears as its value.
The second is dictionary tagOccurences with a the number of games as the key
and the number of tags as its value.
'''
def tagsBar(df):

	#labesl
	plt.xlabel('Tags')
	plt.ylabel('# of Games')

	tagPopularity = {}

	#loops through df, creating tagPopularity
	for i in range(0, 50):
		for tag in df['tags'].iloc[i]:
			if tag not in tagPopularity.keys():
				tagPopularity[tag] = 1
			else:
				tagPopularity[tag] += 1
	tagPopularity = dict(sorted(tagPopularity.items(), key=lambda x: x[1], reverse=True))

	tagOccurences = {}

	#loops through tagPopularity, creating tag Occurences
	for value in tagPopularity.values():
		if value not in tagOccurences:
			tagOccurences[value] = 1
		else:
			tagOccurences[value] += 1
	
	#loops for tagPopulariyt, plots points
	for key, value in tagPopularity.items():
		if value >= 5:
			if value >= 30:
				pointColor = 'red'
			elif value >= 20:
				pointColor = 'orange'
			elif value >= 10:
				pointColor = 'green'
			elif value >= 5:
				pointColor = 'blue'
			else:
				pointColor = 'purple'

			plt.bar(key, value, color=pointColor)
	
	plt.xticks(rotation=90,fontsize=8)
	
	return tagPopularity, tagOccurences

'''
Takes in DataFrame df
Displays an ordered bar graph based on a genre's popularity
Returns: A tuple with two values. The first is dictionary genrePopularity
with a genre as the key and the number of times it appears as its value.
The second is dictionary genreOccurences with a the number of games as the key
and the number of genres as its value. 
'''
def genreBar(df):

	#labels
	plt.xlabel('Genres')
	plt.ylabel('# of Games')

	genrePopularity = {}

	#loops through df, creating genrePopularity
	for i in range(0, 50):
		for genre in df['genre'].iloc[i]:
			if genre not in genrePopularity.keys():
				genrePopularity[genre] = 1
			else:
				genrePopularity[genre] += 1
	genrePopularity = dict(sorted(genrePopularity.items(), key=lambda x: x[1], reverse=True))

	genreOccurences = {}

	#loops through genrePopularity, creating genreOccurences
	for value in genrePopularity.values():
		if value not in genreOccurences:
			genreOccurences[value] = 1
		else:
			genreOccurences[value] += 1
	
	#plots graph
	plt.bar(genrePopularity.keys(), genrePopularity.values())
	plt.xticks(rotation=45,fontsize=10)
	return genrePopularity, genreOccurences

'''
Takes in DataFrame df
Displays a bar graph of Player Count vs Name 

'''
def popularityBar(df):

	#labels
	plt.xlabel('Name')
	plt.ylabel('Player Count')

	#plots graph
	plt.bar(df['Name'], df['countAverage'])
	plt.xticks(rotation=90,fontsize=5)

'''
Takes in DataFrame df
Displays a scatterplot of isIndie vs Player Count
Returns: Number of Indie games
'''
def indiePopularity(df):

	#labels
	plt.xlabel('Player Count')

	indie = df['isIndie'][6:]
	playerCount = df['countAverage'][6:]
	
	#loops through indie, plotting points
	for i in range(0, len(indie)):
		if playerCount.iloc[i]:
			pointColor = 'red'
		else:
			pointColor = 'blue'
		plt.plot(indie.iloc[i], playerCount.iloc[i], 'o', color=pointColor)
	return sum(df['isIndie'])

'''
Takes in DataFrame df
Prints info on tags and genres regarding top 6 games

'''
def top6Analysis(data):
	df = data[:6]
	tagDict = {}

	#loops through top 6 games, creating dictionary tagDict
	# with key tags and value the number of games it appears on.
	for i in range(0, len(df)):
		for tag in df['tags'].iloc[i]:
			if tag not in tagDict.keys():
				tagDict[tag] = 1
			else:
				tagDict[tag] += 1
	tagDict = dict(sorted(tagDict.items(), key=lambda x: x[1], reverse=True))
	print(tagDict)

	genreDict = {}

	#loops through top 6 games, creating dictionary genreDict
	# with key genres and value the number of games it appears on.
	for i in range(0, len(df)):
		for genre in df['genre'].iloc[i]:
			if genre not in genreDict.keys():
				genreDict[genre] = 1
			else:
				genreDict[genre] += 1
	genreDict = dict(sorted(genreDict.items(), key=lambda x: x[1], reverse=True))
	
	print(genreDict)
	print(tagDict)

'''
Takes in DataFrame df
Diplays a bar graph of developers vs # of games
Returns: A tuple with two dictionaries. The first dictionary gameDict
has the developer as keys and their games in a list as values, sorted by value.
The second dictionary numDict has developer as keys and number of games
as values, sorted by value.
'''
def developerBar(df):
	
	#labels
	plt.xlabel('Developer')
	plt.ylabel('# of Games')

	#loops through df to create gameDict
	gameDict = {}
	for i in range(0, 50):
		e = df.iloc[i]
		if e['developer'] not in gameDict.keys():
			gameDict[e['developer']] = [e['name']]
		else:
			gameDict[e['developer']].append(e['name'])
	

	#loops through gameDict to create numDict	
	numDict = {key: len(value) for key, value in gameDict.items()}
	numDict = dict(sorted(numDict.items(), key=lambda x: x[1], reverse=True))
	
	gameDict = dict(sorted(gameDict.items(), key=lambda x: numDict[x[0]]))
	
	#plots bar graph of developers and # of games
	plt.bar(numDict.keys(), numDict.values())
	plt.xticks(rotation=90,fontsize=10)
	return gameDict, numDict

'''
Takes in DataFrame df
Diplays a bar graph of publishers vs # of games
Returns: A tuple with two dictionaries. The first dictionary gameDict
has the developer as keys and their games in a list as values, sorted by value.
The second dictionary numDict has developer as keys and number of games
as values, sorted by value.
'''
def publisherBar(df):

	#labels
	plt.xlabel('Publisher')
	plt.ylabel('# of Games')


	gameDict = {}

	#loops through df to create gameDict 
	for i in range(0, 50):
		e = df.iloc[i]
		if e['publisher'] not in gameDict.keys():
			gameDict[e['publisher']] = [e['name']]
		else:
			gameDict[e['publisher']].append(e['name'])
	

	#loops from gameDict to create numDict
	numDict = {key: len(value) for key, value in gameDict.items()}
	numDict = dict(sorted(numDict.items(), key=lambda x: x[1], reverse=True))
	
	gameDict = dict(sorted(gameDict.items(), key=lambda x: numDict[x[0]]))

	#plots bar grpah of publisher vs # of games
	plt.bar(numDict.keys(), numDict.values())
	plt.xticks(rotation=90,fontsize=10)

	return gameDict, numDict

'''
Takes in DataFrame df
Creates a boxplot based on Player Count
Returns: a dictionary of line data of the boxplot
'''

def popularityBoxplot(df):

	#creates the boxplot
	bPlot = plt.boxplot(df['countAverage'])
	
	#label
	plt.ylabel('Player Count')

	return {k : [v[i].get_ydata() for i in range(0, len(v))] for k, v in bPlot.items() if v}

'''
Takes in DataFrame df
Creates a pie graph of games, the total summing to the number of Steam Players

'''
def popularityPie(df):
	slices = []
	lab = []
	total = sum(df['countAverage'])
	otherSum = 0
	
	#loops through games, creating slices for the 6 most popular games
	for i in range(0, 50):
		n = df['countAverage'].iloc[i]
		if n / total > 0.03:
			slices.append(n)
			lab.append(df['name'].iloc[i])
		else:
			otherSum += n
	slices.append(otherSum)
	lab.append("Other Top 50 Games")

	slices.append(8000000 - sum(slices))
	lab.append("Other Games")
	print(slices)

	#plots the slices
	plt.pie(slices, labels=lab, autopct='%1.1f%%')

'''
Takes in DataFrame df
Creates a pie graph of games, the total summing to the number of Player in top 50 games.

'''

def popularityPie2(df):
	slices = []
	lab = []
	total = sum(df['countAverage'])
	otherSum = 0

	#loops through games, creating slices for the 6 most popular games
	for i in range(0, 50):
		n = df['countAverage'].iloc[i]
		if n / total > 0.03:
			slices.append(n)
			lab.append(df['name'].iloc[i])
		else:
			otherSum += n
	slices.append(otherSum)
	lab.append("Other Top 50 Games")

	#plots the slices
	plt.pie(slices, labels=lab, autopct='%1.1f%%')

#takes in my DataFrame and adds columns / reformats data
def clean(df):
	
	#replaces genre string w/ lists of genres
	df['genre'] = df['genre'].apply(lambda x: list(map(lambda y: y.strip(), x.split(','))))

	#replaces tags string w/ lists of tags
	df['tags'] = df['tags'].apply(lambda x: list(map(lambda y: y.split(':')[0].strip().strip('\''), 
		x.lstrip("{").rstrip("}").split(","))))

	#average plapyerCount over last 6 months
	df['countAverage'] = df.iloc[:, 21:].mean(axis=1)

	#positive reviews / total reviews
	df['reviewPercent'] = df['positive'] / (df['negative'] + df['positive'])
	
	#if a game is multiplayer
	df['isMultiplayer'] = df['tags'].apply(lambda Tags: 'Multiplayer' in Tags
		or 'Massively Multiplayer'  in Tags
		or 'Online Co-Op' in Tags
		or 'Co-op' in Tags)

	#if a game is an Indie title
	df['isIndie'] = df['tags'].apply(lambda Tags: 'Indie' in Tags)
	df.sort_values(by='countAverage', ascending=False, inplace=True)

	#number of languages
	df['languageNum'] = df['languages'].apply(lambda x: len(x.split(',')))



clean(data)
#print(data)

#print(data.iloc[2])


plt.figure(1)
priceVPopularity = pricePopularity(data)
print(priceVPopularity)

plt.figure(2)
reviewVPopularity = reviewPopularity(data)
print(reviewVPopularity)

plt.figure(3)
tagsDict = tagsBar(data)
print(tagsDict[1])

plt.figure(4)
genresDict = genreBar(data)
print(genresDict[1])

plt.figure(5)
popularityBar(data)

plt.figure(6)
indieNum = indiePopularity(data)
print(indieNum)

plt.figure(7)
devDict = developerBar(data)
print(devDict)

plt.figure(8)
pubDict = publisherBar(data)
print(pubDict)

plt.figure(9)
bplot = popularityBoxplot(data)
print(bplot)

plt.figure(10)
popularityPie(data)

plt.figure(11)
popularityPie2(data)
















top6Analysis(data)




print(data['name'])
plt.show()

