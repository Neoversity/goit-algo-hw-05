import os

def run_hash_table_task():
    print("Running Hash Table task...")
    import hash_table
    hash_table.main()

def run_binary_search_task():
    print("Running Binary Search task...")
    import binary_search
    binary_search.main()

def run_boyer_moore_task():
    print("Running Boyer-Moore task...")
    import boyer_moore
    boyer_moore.main()

def main():
    while True:
        print("\nSelect a task to run:")
        print("1. Hash Table")
        print("2. Binary Search")
        print("3. Boyer-Moore Search Comparison")
        print("4. Exit")

        choice = input("Enter the number of the task to run: ")

        if choice == '1':
            run_hash_table_task()
        elif choice == '2':
            run_binary_search_task()
        elif choice == '3':
            run_boyer_moore_task()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()
