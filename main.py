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

def input_name():
    name = input("Enter your name: ")
    for i in range(len(rows)):
        if rows[i][1] == name:
            global reference
            reference = i
            print("Name found")
            return True
    print("Please enter a name already in the database")

def input_password():
    password = input("Enter your password: ")
    for i in range(len(rows)):
        if rows[i][3] == password:
            print("Login successful!")
            return True
    print("Incorrect password, please try again.")
    return False

logged_in = False

while logged_in != True:
    if input_name():
        if input_password():
            logged_in = True

python_balance = rows[reference][2]
python_id = rows[reference][0]


while logged_in == True:
    print("=== Banking App ===")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        print(f"Amount: ${python_balance}")
    if choice == 2:
        deposit_amount = int(input("Please enter your deposit amount: "))
        python_balance += deposit_amount
        cursor.execute("UPDATE accounts SET balance=%s WHERE id=%s",(python_balance, python_id))
        conn.commit()
        print(f"Done! Deposit added\nBalance now: ${python_balance}")
    if choice == 3:
        withdraw_amount = int(input("Please enter your withdraw amount: "))
        python_balance -= withdraw_amount
        cursor.execute("UPDATE accounts SET balance=%s WHERE id=%s",(python_balance, python_id))
        conn.commit()
        print(f"Done! Withdraw added\nBalance now: ${python_balance}")
    if choice == 4:
        print("Thank you for using the program! ")
        logged_in = False
    

# Always close when done
conn.close()

