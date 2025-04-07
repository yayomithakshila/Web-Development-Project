import pymysql

# Database connection details
DB_HOST = "localhost"
DB_USER = "robotuser"
DB_PASSWORD = "password"
DB_NAME = "rpacourse"

try:
    # Establish connection
    connection = pymysql.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )
    
    with connection.cursor() as cursor:
        cursor.execute("SELECT DATABASE();")
        result = cursor.fetchone()
        print(f"Connected to database: {result[0]}")

    connection.close()

except pymysql.MySQLError as e:
    print(f"Error: {e}")
