# This is a database-oriented banking app that has account creation/login functionality.
#
# This app was created using Visual Studio Code and MySQL.
#
# Regular accounts can check their balance, withdraw, deposit, and check their transaction history.
# Specialized admin accounts can remove accounts, list accounts in the database, and check the transaction history of all accounts.
#
# Setup instructions:
#
# 1. Install Python 3.x, MySQL Server, and pip if you haven't already.
#
# 2. Have a MySQL instance running. The app expects the following credentials:
# Host: localhost
# User: root
# Password: root
# Database: banking_app
#
# If your MySQL password or username is different, you can update the connection string at the top of the Python file as shown here:
#
# conn = mysql.connector.connect(
#   host="localhost",
#   user="YOUR_USERNAME",
#   password="YOUR_PASSWORD",
#   database="banking_app"
# )
#
# 3. Python will automatically create the tables, but you need to create a database schema first. Run this in MySQL terminal or Workbench:
# CREATE DATABASE banking_app;
#
# 4. This app requires the mysql-connector-python library. Install it by using this command:
# pip install mysql-connector-python
#
# 5. Once the database is created and the library is installed, navigate to the folder containing your script and run this command to use the app:
# python main.py
#
# How to access admin panel:
#
# The admin panel is designated to an account with an ID of 10, so manual database intervention is required to set a designated account's ID to 10.
# Once this is completed, you can access the admin panel by logging in into the app as usual using the credentials of the account designated administrative access.