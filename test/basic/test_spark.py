def test_context():
    "Test spark context."

    from pyspark.sql import SparkSession, SQLContext

    session = SparkSession.builder \
        .master('local') \
        .appName('myAppName') \
        .config('spark.executor.memory', '5gb') \
        .config("spark.cores.max", "6") \
        .getOrCreate()

    sc = session.sparkContext
    sqlContext = SQLContext(sc)
    assert sqlContext
