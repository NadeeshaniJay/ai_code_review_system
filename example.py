import os
import sys
import pickle
import sqlite3
import requests

API_KEY = "hardcodedapikey123"

def insecure_login():
    username = input("Username: ")
    password = input("Password: ")
    os.system(f"echo {username}:{password} >> users.txt")

def insecure_eval():
    expr = input("Enter a math expression: ")
    result = eval(expr)
    print("Result:", result)

def insecure_pickle():
    data = input("Enter data to pickle: ")
    obj = pickle.loads(bytes(data, 'utf-8'))
    print("Unpickled object:", obj)

def insecure_sql():
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    username = input("Enter username for lookup: ")
    cursor.execute(f"SELECT * FROM users WHERE username = '{username}'")
    print(cursor.fetchall())
    conn.close()

def insecure_request():
    url = input("Enter URL to fetch: ")
    response = requests.get(url)
    print(response.text)

def insecure_file_access():
    filename = input("Enter filename to read: ")
    with open(filename, 'r') as f:
        print(f.read())

if __name__ == "__main__":
    insecure_login()
    insecure_eval()
    insecure_pickle()
    insecure_sql()
    insecure_request()
    insecure_file_access()