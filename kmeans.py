from pyspark.mllib.clustering import KMeans
from math import sqrt
from numpy import array
data=sc.textFile("file:/home/cloudera/Downloads/clust.csv")
header=data.first()
header=sc.parallelize([header])
data=data.subtract(header)
parseData=data.map(lambda line: array([float(x) for x in line.split(',')])).cache()
clusters=KMeans.train(parseData,2,maxIterations=15,runs=10,initializationMode='random')
def error(point):
	center=clusters.centers[clusters.predict(point)]
	return sqrt(sum([x**2 for x in (point - center)]))
WSSSE=parseData.map(lambda point:error(point)).reduce(lambda x,y:x+y)
print(str(WSSSE))
print(clusters.centers)
