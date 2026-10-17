import random

def show_categories(lib):
    category_set = set()
    for key, value in lib.items():
        category_set.add(value["category"])
    return category_set

def return_book(days_late):
    if days_late <= 0:
        return (True, 0)
    else:
        fine = 2000 * days_late
        return (False, fine)

def borrow_book(library):
    book = input("enter book name: ")
    if book in library:
        if library[book]["stock"] > 0:
            library[book]["stock"] -= 1
            print("success!")
        else:
            print("book not available!")
    else:
        print("book does not exist!")

def return_result(days_late):
    status, penalty = return_book(days_late)
    print(f"book returned: {status}")
    print(f"your fine is {penalty} toman!")

def random_book(library):
        book_lst = list(library.keys())
        suggestion = random.choice(book_lst)
        print(f"you should definitely read this book: {suggestion}")