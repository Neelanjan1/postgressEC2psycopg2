import psycopg2

# Connect to the PostgreSQL database
conn = psycopg2.connect(
    dbname="dbtest",
    user="dbuser",
    password="dbuserpass@1",
    host="DNS.amazonaws.com",
    port="5432"
)

# Create a cursor object
cur = conn.cursor()

# Create a table
cur.execute("""
CREATE TABLE IF NOT EXISTS dbtable (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50),
    age INT
);
""")

# Insert data into the table
cur.execute("INSERT INTO dbtable (name, age) VALUES (%s, %s)", ("Some Name", 34))
conn.commit()

# Query the table
cur.execute("SELECT * FROM dbtable;")
rows = cur.fetchall()

for row in rows:
    print(row)

# Close the cursor and connection
cur.close()
conn.close()
