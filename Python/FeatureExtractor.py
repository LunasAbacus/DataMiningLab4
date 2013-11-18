
#!/usr/bin/env python

from TagExtractor import ReuterRooter as RR
import re
import sys
import operator
import collections

def AddToDict(daDic, word, blacklist):
    if (len(word) > 2) and (word not in blacklist):
        if word in daDic:
            daDic[word] += 1
        else:
            daDic[word] = 1

def main():
	articleMap = {} # Map of Article -> Map of Keyword and Number
	answerMap = {} # Map of Articles -> Topic
	titleSet = []
	wordSet = []
	topicSet = []
	blacklist = []

	with open('stopwords.txt') as f:
		for line in f:
			blacklist.append(line.rstrip())

	print ("printing first " + str(sys.argv[1]) + " sgm files")

	with open ("reuters.map",'w') as wrMap:
		articleNumber = 1000

		try:
		    numSmgs = int(sys.argv[1])
		except ValueError:
		    print("Invalid number passed as argument")
		    numSmgs = 1
		for i in range(0,numSmgs):
			filename = "reut2-%s.sgm" % ("%03d" % i)
			print (filename)
			sgm = RR(filename)
			for j in range(0,sgm.NumberOfReuters()-1):
				article = {}

				topicsTemp = sgm.ExtractTagData(j,"TOPICS")
				topicsTemp = re.sub("D", " ", topicsTemp)
				topicsTemp = re.sub("[\d]"," ", topicsTemp)
				topicsTemp = re.sub("[^\w]"," ", topicsTemp)
				numTopics = topicsTemp.split()

				#print(topicsTemp + str(len(numTopics)))

				if (len(numTopics) > 0):
					print(numTopics)

					title = sgm.ExtractTagData(j,"TITLE")
					title = re.sub("\s", " ", title)

					titleSet.append(articleNumber)
					wrMap.write(str(articleNumber)+":"+title+"\n")

					#get set of body words
					body = sgm.ExtractTagData(j,"BODY")
					body = re.sub("[\d]"," ", body)
					body = re.sub("[^\w]"," ", body)
					body = body.lower()
					for token in body.split():
						AddToDict(article, token, blacklist)
						if (token not in wordSet):
							wordSet.append(token)

					title2 = re.sub("[\d]"," ", title)
					title2 = re.sub("[^\w]"," ", title2)
					title2 = title2.lower()
					for token in title2.split():
						AddToDict(article, token, blacklist)
						if (token not in wordSet):
							wordSet.append(token)




					topics = sgm.ExtractTagData(j,"TOPICS")
					topics = re.sub("D"," ", topics)
					topics = re.sub("[\d]"," ", topics)
					topics = re.sub("[^\w]"," ", topics)
					topics = topics.lower()
					temp = []
					for token in topics.split():
						#temp.append(token)
						if(token not in topicSet):
							topicSet.append(token)
						answerMap[articleNumber] = token
					if (articleNumber not in answerMap):
						answerMap[articleNumber] = " "

					articleMap[articleNumber] = article

					articleNumber += 1



		print ('Finished Parsing Files')
		print ('Generating .names and .data files')

		#generate .names and .data files
		with open("reuters.names", 'w') as wr:
			first = True
			for topic in topicSet:
				if (not first):
					wr.write(", " + topic)
				else:
					wr.write(topic)
					first = False
			wr.write(" |classes\n")

			for word in wordSet:
				wr.write(word + ": y,n.\n")

		with open('reuters.data','w') as wr:
			#iterate through each article title
			#for each word in wordset, write number times appears
			# then write the class it is defined as

			print (answerMap)

			for title in titleSet:
				print ("articleNumber: " + str(title))
				for word in wordSet:
					if (word in articleMap[title]):
						wr.write("y,")
					else:
						wr.write("n,")
				wr.write(answerMap[title]+".\n")

if __name__ == '__main__':
    main()
