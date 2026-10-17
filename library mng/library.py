books = {
    "harry potter and the sorcerer's stone": {
        "stock": 11,
        "category": "science-fiction"
    },
    "harry potter and the chamber of secrets": {
        "stock": 13,
        "category": "science-fiction"
    },
    "wrong place wrong time": {
        "stock": 0,
        "category": "thriller"
    }
}

import functions

def menu():
    print("============= Menu =============")
    print("1. borrowing book")
    print("2. returning book")
    print("3. show categories")
    print("4. random suggestion")
    print("5. exit")
    print("================================")

while True:
    menu()
    choice = int(input("enter: "))

    if choice == 1:
        functions.borrow_book(books)
    elif choice == 2:
        delay = int(input("enter how many days delayed: "))
        functions.return_book(delay)
        functions.return_result(delay)
    elif choice == 3:
        print(functions.show_categories(books))
    elif choice == 4:
        functions.random_book(books)
    elif choice == 5:
        print("exited successfuly!")
        break