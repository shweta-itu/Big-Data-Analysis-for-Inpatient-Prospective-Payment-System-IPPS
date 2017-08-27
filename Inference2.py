def parser(line): #parser to extract key, value pair
	line = line.strip().split(",")
	key = line[5] # key is state, col 6
	value = float(line[9]) #avg cov chgs, forcing to float
	return (key,value)
fileIn = sc.textFile("proj/input.csv")
parsed_data = fileIn.map(parser)
parsed_data.take(2)
#[(u'AL', 32963.07), (u'AL', 15131.85)]

summedByStateAvgCovCharges =
parsed_data.reduceByKey(lambda x,y : x + y) #Summing
values for given key using reduceByKey function
summedByStateAvgCovCharges.take(2)
#[(u'WA', 96436142.259999648), (u'DE', 10666249.659999996)]

top5States = summedByStateAvgCovCharges.takeOrdered(5,
lambda(k,v): -v) #Creating an ordered list by sorting with maximum value
for p in top5States: print " {0} : ${1}".format(p[0],p[1])