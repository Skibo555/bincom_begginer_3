import psycopg2


def connect():
    """ Connecting to the PostgreSQL database server """
    conn = None
    try:
        conn = psycopg2.connect(
            dbname="bincom_todo_list",
            # Postgres is my name, I made the mistake during the configuration
            user="julius",
            password="Jayboy",
            host=""
        )
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    return conn


def add_todo(description):
    conn = connect()
    cur = conn.cursor()
    cur.execute("INSERT INTO todo_l (description) VALUES (%s)", (description,))
    conn.commit()
    cur.close()
    conn.close()


def list_todos():
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT id, description, completed FROM todo_l ORDER BY id")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()


def complete_todo(task_id):
    conn = connect()
    cur = conn.cursor()
    cur.execute("UPDATE todo_l SET completed = TRUE WHERE id = %s", (task_id,))
    conn.commit()
    cur.close()
    conn.close()


def delete_todo(task_id):
    conn = connect()
    cur = conn.cursor()
    cur.execute("DELETE FROM todo_l WHERE id = %s", (task_id,))
    conn.commit()
    cur.close()
    conn.close()


# Example usage
if __name__ == '__main__':
    while True:
        print("\nTo-Do List:")
        list_todos()
        print("\nOptions:")
        print("1. Add a new to-do")
        print("2. Complete a to-do")
        print("3. Delete a to-do")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            description = input("Enter the to-do description: ")
            add_todo(description)
        elif choice == '2':
            todo_id = int(input("Enter the ID of the to-do to complete: "))
            complete_todo(todo_id)
        elif choice == '3':
            todo_id = int(input("Enter the ID of the to-do to delete: "))
            delete_todo(todo_id)
        elif choice == '4':
            break
        else:
            print("Invalid choice, please try again.")
