rdd1 = sc.textFile("file:/home/cloudera/Desktop/average.txt")
>>> rdd2 = rdd1.map(lambda word:(word.split()[0],(int(word.split()[1]),1)))
>>> rdd3 = rdd2.reduceByKey(lambda v1,v2:((v1[0]+v2[0]),(v1[1]+v2[1])))
>>> rdd3.collect()[(u'pune', (80, 1)), (u'delhi', (100, 2)), (u'mumbai', (90, 2))]
>>> rdd4 = rdd3.map(lambda word:(word[0],word[1][0]/word[1][1]))
>>> rdd4.collect()
[(u'pune', 80), (u'delhi', 50), (u'mumbai', 45)]
