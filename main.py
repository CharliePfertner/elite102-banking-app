import mysql.connector
# Step 1: Connect to your MySQL database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="banking_app"
)
cursor = conn.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS accounts (
        id INT PRIMARY KEY,
        name VARCHAR(100),
        balance DECIMAL(10, 2),
        password VARCHAR(100)
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS transactions (
        id INTEGER PRIMARY KEY AUTO_INCREMENT,
        account_id INTEGER,
        type TEXT,
        amount REAL,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (account_id) REFERENCES accounts(id)
    )          
''')


cursor.execute("")
conn.commit()


cursor.execute("SELECT * FROM accounts")
rows = cursor.fetchall()

def input_name():
    name = input("\nEnter your name: ")
    for i in range(len(rows)):
        if rows[i][1] == name:
            global reference
            reference = i
            print("\nName found!\n")
            return True
    print("\nPlease enter a name already in the database")

def input_password():
    password = input("Enter your password: ")
    for i in range(len(rows)):
        if rows[i][3] == password:
            print("\nLogin successful!")
            return True
    print("\nIncorrect password, please try again.\n")
    return False

logged_in = False
while logged_in != True:
    print("\n1. Create Account\n2. Log in")
    try:
        use_account = int(input("\nEnter your choice: "))
    except ValueError:
        print("\nPlease enter an integer.\n")
        continue

    if use_account == 1:
        create_username = input("\nType in your name: ")
        create_password = input("Type in your password: ")
        initial_deposit = int(input("Type in your initial deposit: "))
        cursor.execute("INSERT INTO accounts (name, balance, password) VALUES (%s, %s, %s)",(create_username, initial_deposit, create_password))
        conn.commit()
        cursor.execute("SELECT * FROM accounts")
        rows = cursor.fetchall()
        print("\nNew account created!")

    elif use_account == 2:
        while logged_in != True:
            if input_name():
                if input_password():
                    logged_in = True

    else:
        print("\nPlease enter a valid choice.\n")
        continue

python_balance = rows[reference][2]
python_id = rows[reference][0]
status = None

if python_id == 10:
    while logged_in == True:
        print("\n=== Admin Panel ===")
        print("1. Remove Account")
        print("2. List Accounts in Database")
        print("3. Check Transaction History of All Accounts")
        print("4. Exit")
        try:
            choice = int(input("\nEnter your choice: "))
        except ValueError:
            print("\nPlease enter an integer.")
            continue
        if choice == 1:
            try:
                account_to_remove = int(input("\nEnter the ID of the account you want to remove: "))
            except ValueError:
                print("\nPlease enter an integer.")
                continue
            cursor.execute("DELETE FROM transactions WHERE account_id = %s;",(account_to_remove,))
            cursor.execute("DELETE FROM accounts WHERE id = %s;",(account_to_remove,))
            conn.commit()
            print("\nAccount deleted!")
        elif choice == 2:
            cursor.execute("SELECT * FROM accounts")
            rows = cursor.fetchall()
            for i in range(len(rows)):
                print(f"\nID: {rows[i][0]}\nName: {rows[i][1]}\n")
        elif choice == 3:
            cursor.execute("SELECT * FROM transactions")
            rows = cursor.fetchall()
            for i in range(len(rows)):
                print(f"\nAccount ID: {rows[i][1]}\nType: {rows[i][2]}\nAmount: ${rows[i][3]:.2f}\nDate: {rows[i][4]}\n")
        elif choice == 4:
            print("\nThank you for using the program!")
            logged_in = False
        else:
            print("\nPlease enter a valid choice.")
            continue

while logged_in == True:
    print("\n=== Banking App ===")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Transaction History")
    print("5. Exit")
    try:
        choice = int(input("\nEnter your choice: "))
    except ValueError:
        print("\nPlease enter an integer.\n")
        continue
    if choice == 1:
        print(f"\nAmount: ${python_balance}")
    elif choice == 2:
        status = "Deposit"
        try:
            deposit_amount = int(input("\nPlease enter your deposit amount: "))
        except ValueError:
            print("\nPlease enter an integer.\n")
            continue
        python_balance += deposit_amount
        cursor.execute("UPDATE accounts SET balance=%s WHERE id=%s",(python_balance, python_id))
        conn.commit()
        cursor.execute("INSERT INTO transactions (account_id, type, amount) VALUES (%s, %s, %s)",(python_id, status, deposit_amount))
        conn.commit()
        print(f"\nDone! Deposit added\nBalance now: ${python_balance}")
    elif choice == 3:
        status = "Withdrawal"
        try:
            withdraw_amount = int(input("\nPlease enter your withdraw amount: "))
        except ValueError:
            print("\nPlease enter an integer.\n")
            continue
        if withdraw_amount > python_balance:
            print("\nYour withdraw amount is too high! Please enter a lower withdraw amount.")
            continue
        python_balance -= withdraw_amount
        cursor.execute("UPDATE accounts SET balance=%s WHERE id=%s",(python_balance, python_id))
        conn.commit()
        cursor.execute("INSERT INTO transactions (account_id, type, amount) VALUES (%s, %s, %s)",(python_id, status, withdraw_amount))
        conn.commit()
        print(f"\nDone! Withdraw added\nBalance now: ${python_balance}")
    elif choice == 4:
        cursor.execute("SELECT type, amount, timestamp FROM transactions WHERE (account_id = %s)", (python_id,))
        rows = cursor.fetchall()
        for i in range(len(rows)):
            print(f"\nType: {rows[i][0]}\nAmount: ${rows[i][1]:.2f}\nDate: {rows[i][2]}\n")
    elif choice == 5:
        print("\nThank you for using the program! ")
        logged_in = False
    else:
        print("\nPlease enter a valid choice.\n")
        continue

conn.close()

