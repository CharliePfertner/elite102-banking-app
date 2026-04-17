import mysql.connector

# Step 1: Connect to your MySQL database
conn = mysql.connector.connect(
    host="localhost",
    user="root",           # your MySQL username
    password="root",  # the password you set during MySQL install
    database="banking_app"
)
cursor = conn.cursor()

# Step 2: Create a table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS accounts (
        id INT PRIMARY KEY,
        name VARCHAR(100),
        balance DECIMAL(10, 2)
    )
''')

# Step 3: Insert data
cursor.execute("")
conn.commit()   # IMPORTANT: saves your changes!

# Step 4: Query data
cursor.execute("SELECT * FROM accounts")
rows = cursor.fetchall()
for row in rows:
    print(row)

print(rows[1][1])

def input_name():
    name = input("Enter your name: ")
    for i in range(len(rows)):
        if rows[i][1] == name:
            print("Name found")
            return True
    print("Please enter a name already in the database")

def input_password():
    password = input("Enter your password: ")
    for i in range(len(rows)):
        if rows[i][3] == password:
            print("Login successful!")
            return True
    print("Please try again.")
    return False

logged_in = False

while logged_in != True:
    if input_name():
        if input_password():
            logged_in = True

# Always close when done
conn.close()

