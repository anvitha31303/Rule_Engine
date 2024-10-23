# main.py

from database import create_connection, insert_rule, get_all_rules

def main():
    conn = create_connection()
    if conn is not None:
        # Insert a sample rule
        insert_rule(conn, "age > 30 AND department = 'Sales'")

        # Fetch and print all rules
        rules = get_all_rules(conn)
        print("Fetched rules:", rules)

        conn.close()  # Close the connection

if __name__ == "__main__":
    main()
