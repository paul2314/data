from pyspark import SparkConf, SparkContext
sc
def computeContribs(neighbors,rank):
	for neighbor in neighbors:yield(neighbor,rank/len(neighbors))
linkfile="file:/home/training/Desktop/PageLinks.txt"
links=sc.textFile(linkfile).map(lambda line:line.split())\
.map(lambda pages:(pages[0],pages[1]))\
.distinct()\
.groupByKey()\
.persist()
rank=links.map(lambda (page,neighbors) : (page,1.0))
n=10
for x in xrange(n):
	contribs=links\
	.join(ranks)\
	.flatMap(lambda(page,(neighbors,rank))):\
	computeContribs(neighbors,rank))
ranks=contribs\
reduceByKey(lambda v1,v2: v1+v2)\
.map(lambda(page,contrib)):\
(page,contrib*0.85+0.15))
print "Iteration ",x
for pair in ranks.take(10):
	print pair
