# database.py

import psycopg2
from psycopg2 import sql
from config import DATABASE_CONFIG

def create_connection():
    conn = None
    try:
        conn = psycopg2.connect(
            dbname=DATABASE_CONFIG['dbname'],
            user=DATABASE_CONFIG['user'],
            password=DATABASE_CONFIG['password'],
            host=DATABASE_CONFIG['host'],
            port=DATABASE_CONFIG['port']
        )
        print("Connection to PostgreSQL DB successful")
    except Exception as e:
        print(f"The error '{e}' occurred")
    return conn

def insert_rule(conn, rule_text):
    cursor = conn.cursor()
    insert_query = sql.SQL("INSERT INTO rules (rule_text) VALUES (%s)")
    cursor.execute(insert_query, (rule_text,))
    conn.commit()
    cursor.close()
    print("Rule inserted successfully")

def get_all_rules(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM rules")
    rules = cursor.fetchall()
    cursor.close()
    return rules
