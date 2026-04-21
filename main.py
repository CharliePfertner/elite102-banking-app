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
    print("1. Create Account\n2. Log in")

    use_account = int(input("\nEnter your choice: "))

    if use_account == 1:
        create_username = input("Type in your name: ")
        create_password = input("Type in your password: ")
        initial_deposit = int(input("Type in your initial deposit: "))
        cursor.execute("INSERT INTO accounts (name, balance, password) VALUES (%s, %s, %s)",(create_username, initial_deposit, create_password))
        conn.commit()
        cursor.execute("SELECT * FROM accounts")
        rows = cursor.fetchall()
        print("New account created!")
        

    if use_account == 2:
        while logged_in != True:
            if input_name():
                if input_password():
                    logged_in = True

python_balance = rows[reference][2]
python_id = rows[reference][0]

if python_id == 10:
    while logged_in == True:
        print("\n=== Admin Panel ===")
        print("1. Remove Account")
        print("2. List Accounts in Database")
        print("3. Exit")
        choice = int(input("\nEnter your choice: "))
        if choice == 1:
            account_to_remove = int(input("\nEnter the ID of the account you want to remove: "))
            cursor.execute("DELETE FROM accounts WHERE id = %s;",(account_to_remove,))
            conn.commit()
            print("\nAccount deleted!")
        if choice == 2:
            cursor.execute("SELECT * FROM accounts")
            rows = cursor.fetchall()
            for i in range(len(rows)):
                print(f"\nID: {rows[i][0]}\nName: {rows[i][1]}\n")
        if choice == 3:
            print("\nThank you for using the program!")
            logged_in = False

while logged_in == True:
    print("\n=== Banking App ===")
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
        if withdraw_amount > python_balance:
            print("\nYour withdraw amount is too high! Please enter a lower withdraw amount.")
            continue
        python_balance -= withdraw_amount
        cursor.execute("UPDATE accounts SET balance=%s WHERE id=%s",(python_balance, python_id))
        conn.commit()
        print(f"Done! Withdraw added\nBalance now: ${python_balance}")
    if choice == 4:
        print("Thank you for using the program! ")
        logged_in = False
    

# Always close when done
conn.close()

