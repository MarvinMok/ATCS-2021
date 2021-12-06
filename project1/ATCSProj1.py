import pandas as pd 
import numpy as np
import random
#import seaborn as sns
import matplotlib.pyplot as plt

import csv

pd.set_option("display.max_columns", None)
#info = pd.read_csv("statistics.csv")
#playerCounts = pd.read_csv("Steam Games - OrderedCounts.csv")
data = pd.read_csv("finalstats.csv")
#print(len(df))
#t = info.to_dict(orient='index')
t1 = []
t2= []

'''final = info.merge(playerCounts, how='inner', left_on='name', right_on='Name')
finaldict = final.to_dict(orient='index')

for i in range(0, len(finaldict)):
	t1.append(finaldict[i]['name'])

for i in range(0, len(info)):
	t2.append(t[i]['name'])

for idk in t2:
	if idk not in t1:
		print(idk)
#print(len(finaldict))

#print(finaldict)
#print(finaldict[0].keys)'''
'''with open('finalstats.csv', 'w', newline='') as idk:
	spamwriter = csv.writer(idk)
	spamwriter.writerow(finaldict[0].keys())
	for i in range(0, 50):
		spamwriter.writerow(finaldict[i].values())
#print(final) 
plots = []
'''

def displayPopularity(df):
	x = [5, 4, 3, 2, 1, 0]
	[df['October 2021'], df['September 2021'], df['August 2021'], 
	df['July 2021'], df['June 2021'], df['May 2021']]
	#print(df['July 2021'].iloc[range(0,50)])
	for i in range(0,50):
		y = [df['October 2021'].iloc[i], df['September 2021'].iloc[i], df['August 2021'].iloc[i], 
	df['July 2021'].iloc[i], df['June 2021'].iloc[i], df['May 2021'].iloc[i]]
		if y[0] > 200000:
			plt.plot(x, y)

	print(df['October 2021'].iloc[range(0,50)])




	plt.show()

def pricePopularity(df):
	prices = [0, 0, 0, 0, 0]
	names = []

	plt.xlabel('Price')
	plt.ylabel('Player Count')

	for i in range(6, 50):
		y = df.iloc[i]['countAverage']

		x = df.iloc[i]['initialprice'] / 100
		if x == 0:
			Color = "red"
			prices[0] += 1
		elif x <= 20:
			prices[1] += 1
			Color = "orange"
		elif x <= 40:
			prices[2] += 1
			Color = "green"
		elif x > 59 and x < 60:
			Color = "purple"
			prices[4] += 1
		else:
			Color = "blue"
			prices[3] += 1


		plt.plot(x, y, 'o', color=Color)
		#else:
			#plt.plot(x, 200000 + random.randint(0, 20000), 'o', color="purple")
	

	return (prices)

def reviewPopularity(df):

	plt.xlabel('Review Percentage')
	plt.ylabel('Player Count')
	ranges = [0, 0, 0, 0]
	for i in range(6, 50):
		y = df.iloc[i]['countAverage']

		x = df.iloc[i]['reviewPercent']
		if x <= 0.7:
			Color = "red"
			ranges[0] += 1
		elif x <= 0.8:
			Color = "orange"
			ranges[1] += 1
		elif x <= 0.9:
			Color = "green"
			ranges[2] += 1
		else:
			Color = 'blue'
			ranges[3] += 1


		plt.plot(x, y, 'o', color=Color)
		#else: 
			#plt.plot(x, 200000, 'o', color="purple")
	return ranges
def tagsBar(df):

	plt.xlabel('Tags')
	plt.ylabel('# of Games')

	d = {}

	for i in range(0, 50):
		for tag in df['tags'].iloc[i]:
			if tag not in d.keys():
				d[tag] = 1
			else:
				d[tag] += 1
	d = dict(sorted(d.items(), key=lambda x: x[1], reverse=True))

	d2 = {}
	for v in d.values():
		if v not in d2:
			d2[v] = 1
		else:
			d2[v] += 1
	
	for k, v in d.items():
		if v >= 5:
			if v >= 30:
				c = 'red'
			elif v >= 20:
				c = 'orange'
			elif v >= 10:
				c = 'green'
			elif v >= 5:
				c = 'blue'
			else:
				c = 'purple'

			plt.bar(k, v, color=c)
	plt.xticks(rotation=90,fontsize=8)
	return d, d2
	
def genreBar(df):

	plt.xlabel('Genres')
	plt.ylabel('# of Games')

	d = {}

	for i in range(0, 50):
		for g in df['genre'].iloc[i]:
			if g not in d.keys():
				d[g] = 1
			else:
				d[g] += 1
	d = dict(sorted(d.items(), key=lambda x: x[1], reverse=True))

	d2 = {}
	for v in d.values():
		if v not in d2:
			d2[v] = 1
		else:
			d2[v] += 1
	

	plt.bar(d.keys(), d.values())
	plt.xticks(rotation=45,fontsize=10)
	return d, d2
	
def popularityBar(df):

	plt.xlabel('Name')
	plt.ylabel('Player Count')

	plt.bar(df['Name'], df['countAverage'])
	plt.xticks(rotation=90,fontsize=5)

def indiePopularity(df):

	plt.xlabel('Player Count')

	y = df['isIndie'][6:]
	x = df['countAverage'][6:]
	
	for i in range(0, len(x)):
		if y.iloc[i]:
			c = 'red'
		else:
			c = 'blue'
		plt.plot(x.iloc[i], y.iloc[i], 'o', color=c)
	return sum(df['isIndie'])

def top6analysis(data):
	df = data[:6]
	dt = {}

	for i in range(0, len(df)):
		for tag in df['tags'].iloc[i]:
			if tag not in dt.keys():
				dt[tag] = 1
			else:
				dt[tag] += 1
	dt = dict(sorted(dt.items(), key=lambda x: x[1], reverse=True))
	print(dt)

	dg = {}

	for i in range(0, len(df)):
		for g in df['genre'].iloc[i]:
			if g not in dg.keys():
				dg[g] = 1
			else:
				dg[g] += 1
	dg = dict(sorted(dg.items(), key=lambda x: x[1], reverse=True))
	print(dg)

	print(df)


def developerBar(df):
	
	plt.xlabel('Developer')
	plt.ylabel('# of Games')

	d = {}
	for i in range(0, 50):
		e = df.iloc[i]
		if e['developer'] not in d.keys():
			d[e['developer']] = [e['name']]
		else:
			d[e['developer']].append(e['name'])
	dnum = {k: len(v) for k, v in d.items()}
	dnum = dict(sorted(dnum.items(), key=lambda x: x[1], reverse=True))
	d = dict(sorted(d.items(), key=lambda x: dnum[x[0]]))
	

	plt.bar(dnum.keys(), dnum.values())
	plt.xticks(rotation=90,fontsize=10)
	return dnum, d

def publisherBar(df):

	plt.xlabel('Publisher')
	plt.ylabel('# of Games')

	d = {}
	for i in range(0, 50):
		e = df.iloc[i]
		if e['publisher'] not in d.keys():
			d[e['publisher']] = [e['name']]
		else:
			d[e['publisher']].append(e['name'])
	dnum = {k: len(v) for k, v in d.items()}
	dnum = dict(sorted(dnum.items(), key=lambda x: x[1], reverse=True))
	d = dict(sorted(d.items(), key=lambda x: dnum[x[0]]))
	

	plt.bar(dnum.keys(), dnum.values())
	plt.xticks(rotation=90,fontsize=10)

	return dnum, d

def PopularityBoxplot(df):
	bplot = plt.boxplot(df['countAverage'])
	plt.ylabel('Player Count')
	return {k : [v[i].get_ydata() for i in range(0, len(v))] for k, v in bplot.items() if v}

def popularityPie(df):
	slices = []
	lab = []
	total = sum(df['countAverage'])
	otherSum = 0
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
	plt.pie(slices, labels=lab, autopct='%1.1f%%')

def popularityPie2(df):
	slices = []
	lab = []
	total = sum(df['countAverage'])
	otherSum = 0
	for i in range(0, 50):
		n = df['countAverage'].iloc[i]
		if n / total > 0.03:
			slices.append(n)
			lab.append(df['name'].iloc[i])
		else:
			otherSum += n
	slices.append(otherSum)
	lab.append("Other Top 50 Games")

	plt.pie(slices, labels=lab, autopct='%1.1f%%')

#takes in my DataFrame and adds columns / reformats data
def clean(df):
	
	#replaces genre string w/ lists of genres
	df['genre'] = df['genre'].apply(lambda x: list(map(lambda y: y.strip(), x.split(','))))

	#replaces tags string w/ lists of tags
	df['tags'] = df['tags'].apply(lambda x: list(map(lambda y: y.split(':')[0].strip().strip('\''), 
		x.lstrip("{").rstrip("}").split(","))))

	#average playerCount over last 6 months
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
'''
plt.figure(4)
gd = genreBar(data)
print(gd[1])

plt.figure(8)
dev = publisherBar(data)
print(dev)

plt.figure(6)
i = indiePopularity(data)
print(i)

plt.figure(7)
dev = developerBar(data)



'''


'''
plt.figure(1)
p = pricePopularity(data)
print(p)

plt.figure(9)
bplot = PopularityBoxplot(data)
print(bplot)

plt.figure(5)
popularityBar(data)



plt.figure(2)
r = reviewPopularity(data)
print(r)

plt.figure(2)
r = reviewPopularity(data)
print(r)

plt.figure(3)
td = tagsBar(data)
print(td[1])

plt.figure(11)
popularityPie2(data)

top6analysis(data)

plt.figure(8)
pub = publisherBar(data)
print(pub)
'''

plt.figure(10)
popularityPie(data)

print(data['name'])
plt.show()

