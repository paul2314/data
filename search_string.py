rdd1 = sc.textFile("file:/home/cloudera/Desktop/search.txt")
>>> searchTerm = "Divya"
>>> rdd2 = rdd1.filter(lambda line:(searchTerm in line)).collect()
>>> print rdd2
[u'Divya']
