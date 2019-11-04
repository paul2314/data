rdd1 = sc.textFile("file:/home/cloudera/Desktop/startI.txt")
>>> rdd2 = rdd1.flatMap(lambda line:line.split())
>>> rdd3 = rdd2.filter(lambda word :word[0]=="i" or word[0]=="I" )
>>> rdd4 = rdd3.map(lambda word:(word,1))
>>> rdd5 = rdd4.reduceByKey(lambda v1,v2:(v1+v2))
>>> rdd5.collect()
[(u'iqbaal', 1), (u'indu', 1), (u'ishq', 1), (u'illinois', 1)]
