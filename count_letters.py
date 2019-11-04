rdd1 = sc.textFile("file:/home/cloudera/Desktop/4letter.txt")
>>> rdd2 = rdd1.flatMap(lambda line:line.split())
>>> rdd3 = rdd2.filter(lambda word:len(word)==4)
>>> rdd4 = rdd3.map(lambda word:(word,1))
>>> rdd5 = rdd4.reduceByKey(lambda v1,v2:(v1+v2))
>>> rdd5.collect()
[(u'hell', 1), (u'diva', 1), (u'juhi', 1), (u'till', 1)]
