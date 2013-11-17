
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
	wordSet = []
	blacklist = []

	with open('stopwords.txt') as f:
		for line in f:
			blacklist.append(line.rstrip())

	print ("printing first " + str(sys.argv[1]) + "sgm files")

	with open ("reuters.map",'w') as wrMap:
		articleNumber = 1000

		try:
		    numSmgs = int(sys.argv[1])
		except ValueError:
		    print("Invalid number passes as argument")
		    numSmgs = 1
		for i in range(0,numSmgs):
			filename = "reut2-%s.sgm" % ("%03d" % i)
			print (filename)
			sgm = RR(filename)
			for j in range(0,sgm.NumberOfReuters()-1):
				article = {}

				title = sgm.ExtractTagData(j,"TITLE")
				title = re.sub("\s", " ", title)

				wrMap.write("\n"+str(articleNumber)+":"+title)

				#get set of body words
				body = sgm.ExtractTagData(j,"BODY")
				body = re.sub("[\d]"," ", body)
				body = re.sub("[^\w]"," ", body)
				body = body.lower()
				for token in body.split():
					AddToDict(article, token, blacklist)
					if (token not in wordSet):
						wordSet.append(token)


				topics = sgm.ExtractTagData(j,"TOPICS")
				topics = re.sub("[\d]"," ", topics)
				topics = re.sub("[^\w]"," ", topics)
				topics = topics.lower()
				for token in topics.split():
					AddToDict(article, token, blacklist)
					if (token not in wordSet):
						wordSet.append(token)



		print ('Finished Parsing Files')
		print ('Generating .names and .data files')

		#generate .names and .data files
		with open('reuters.data','w') as wr, open("reuters.names", 'w') as wrNames:
			pass



if __name__ == '__main__':
    main()
