# Implement a custom transformation operation on an RDD to compute the average of all numbers in the RDD.
#  Use Python to define a funtion that takes an RDD as input, applies the map transformation to convert the RDD elements intop tuples of (value, 1), reduces the tuples using the reduceByKey transformation,
#  and computes the average using ther mapValues tranformation. Use ther funtion to calculater the average of a sample RDD of integers.

from pyspark import SparkContext

def compute_average(sc, numbers):
    # Parallelize the input list into an RDD
    rdd = sc.parallelize(numbers)
    
    # Map each number to a (number, 1) pair for sum and count
    rdd_mapped = rdd.map(lambda x: (1, (x, 1)))
    
    # Reduce by summing up the values and counts
    reduced_rdd = rdd_mapped.reduceByKey(lambda x, y: (x[0] + y[0], x[1] + y[1]))
    
    # Compute the average by dividing sum by count
    avg = reduced_rdd.mapValues(lambda x: x[0] / x[1])
    
    # Collect the result
    result = avg.collect()
    return result

# Example usage
if __name__ == "__main__":
    sc = SparkContext.getOrCreate()
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = compute_average(sc, numbers)
    print(result)
