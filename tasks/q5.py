#Python

class EntryManager:
    def __init__(self):
        self.entries = {}

    def add_entry(self, entry_id, name, email):
        if entry_id not in self.entries.keys():
            self.entries[entry_id] = {"name": name, "email": email}
            print(f"Entry {entry_id} added successfully.")
        else:
            print("SORRY! CANNOT ADD ITEM")

    def search_entry(self, entry_id):
        if entry_id in self.entries:
            entry = self.entries[entry_id]
            print(f"Entry {entry_id}: Name - {entry['name']}, Email - {entry['email']}")
        else:
            print(f"Entry with ID {entry_id} not found.")

    def update_entry(self, entry_id, name, email):
        if entry_id in self.entries.keys():
            self.entries[entry_id] = {"name": name, "email": email}
            print(f"Entry {entry_id} updated successfully.")
        else:
            print(f"Entry with ID {entry_id} not found. Use add to create a new entry.")

    def delete_entry(self, entry_id):
        if entry_id in self.entries:
            del self.entries[entry_id]
            print(f"Entry {entry_id} deleted successfully.")
        else:
            print(f"Entry with ID {entry_id} not found.")

def main():
    entry_manager = EntryManager()

    while True:
        print("\nOptions:")
        print("1. Add Entry")
        print("2. Search Entry")
        print("3. Update Entry")
        print("4. Delete Entry")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            entry_id = input("Enter unique ID for the entry: ")
            name = input("Enter name: ")
            email = input("Enter email: ")
            entry_manager.add_entry(entry_id, name, email)

        elif choice == "2":
            entry_id = input("Enter ID to search: ")
            entry_manager.search_entry(entry_id)

        elif choice == "3":
            entry_id = input("Enter ID to update: ")
            name = input("Enter updated name: ")
            email = input("Enter updated email: ")
            entry_manager.update_entry(entry_id, name, email)

        elif choice == "4":
            entry_id = input("Enter ID to delete: ")
            entry_manager.delete_entry(entry_id)

        elif choice == "5":
            print("Exiting the program. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

        

if __name__ == "__main__":
    main()
