from pyspark import SparkContext
from pyspark.mllib.linalg.distributed import *
import numpy as np
sc = SparkContext("local", "Matrix Vector Multiplication")
matrix = [[1, 2, 3],
[4, 5, 6],
[7, 8, 9]]
vector = np.array([17, 18, 19])
mat_rdd = sc.parallelize(matrix)
mul_rdd = mat_rdd.map(lambda x: x * vector)\
.map(lambda x: sum(x))\
.collect()
print(mul_rdd)
