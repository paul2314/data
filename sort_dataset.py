rdd1 = sc.textFile("file:/home/cloudera/Desktop/sort.txt")
>>> rdd2 = rdd1.flatMap(lambda line:line.split())
>>> rdd3 = rdd2.map(lambda word:(word,1)).reduceByKey(lambda v1,v2:(v1+v2))
>>> print rdd2.sortBy(lambda a:a[0]).collect()
[u'all', u'are', u'divya', u'hii', u'how', u'i', u'kaise', u'you']
