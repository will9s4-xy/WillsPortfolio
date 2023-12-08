database = {
    1: 'Alex',
    2: 'Bob',
    3: 'Charlie'
}

def get_user_id(user_id):
    return database.get(user_id)

def count_items():
    return len(database)

def add_user():
    user_id = len(database) + 1
    username = input("Enter the username: ")
    database[user_id] = username
    print(f"User '{username}' added to the database with ID {user_id}.")

def remove_user():
    if not database:
        print("Database is empty. No users to remove.")
        return

    username_to_remove = input("Enter the username to remove: ")

    user_ids_to_remove = [user_id for user_id, username in database.items() if username == username_to_remove]

    if user_ids_to_remove:
        for user_id in user_ids_to_remove:
            removed_username = database.pop(user_id, None)
            print(f"User '{removed_username}' (ID: {user_id}) removed from the database.")
        
        # Update user IDs to ensure consecutive numbering
        updated_database = {new_id: username for new_id, username in enumerate(database.values(), start=1)}
        database.clear()
        database.update(updated_database)
    else:
        print(f"No user with the username '{username_to_remove}' found in the database.")

def read_database():
    print("Current Database:")
    for user_id, username in database.items():
        print(f"User ID: {user_id}, Username: {username}")

def main():
    while True:
        print("\nOptions:")
        print("1. Add a user")
        print("2. Remove a user")
        print("3. Read the database")
        print("4. Exit")

        choice = input("Enter your choice (1, 2, 3, or 4): ")

        try:
            if choice == '1':
                add_user()
            elif choice == '2':
                remove_user()
            elif choice == '3':
                read_database()
            elif choice == '4':
                print("Exiting the program.")
                break
            else:
                print("Invalid choice. Please enter 1, 2, 3, or 4.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()
