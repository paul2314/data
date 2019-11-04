users = sc.parallelize([(0,"divya"),(1,"Khushboo"),(2,"Karishma")])
>>> hobbies = sc.parallelize([(0,"ghumna"),(0,"pareshani"),(1,"padhna")])
>>> users.join(hobbies).collect()
[(0, ('divya', 'ghumna')), (0, ('divya', 'pareshani')), (1, ('Khushboo', 'padhna'))]
>>> users.leftOuterJoin(hobbies).collect()
[(0, ('divya', 'ghumna')), (0, ('divya', 'pareshani')), (2, ('Karishma', None)), (1, ('Khushboo',
'padhna'))]
>>> users.join(hobbies).map(lambda x:x[1][0]+" likes "+x[1][1]).collect()
['divya likes ghumna', 'divya likes pareshani', 'Khushboo likes padhna']
