class Book:
    all_books = []

    def __init__(self, title):
        self.title = title
        self.authors_list = []
        self.all_books.append(self)

    def authors(self):
        return self.authors_list


class Author:
    all_authors = []

    def __init__(self, name):
        self.name = name
        self.all_contracts = []
        self.all_authors.append(self)

    def contracts(self):
        return self.all_contracts

    def books(self):
        return [contract.book for contract in self.all_contracts]

    def sign_contract(self, book, date, royalties):
        if not isinstance(book, Book):
            raise Exception("The book must be an instance of the Book class")
        contract = Contract(self, book, date, royalties)
        self.all_contracts.append(contract)
        book.authors_list.append(self)
        return contract

    def total_royalties(self):
        return sum(contract.royalties for contract in self.all_contracts)


class Contract:
    all_contracts = []

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise Exception("The author must be an instance of the Author class")
        if not isinstance(book, Book):
            raise Exception("The book must be an instance of the Book class")
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        self.all_contracts.append(self)

   
@classmethod
def contracts_by_date(cls, date):
    return sorted([contract for contract in cls.all_contracts if contract.date == date], key=lambda x: x.date)

# Example usage
author1 = Author("John Doe")
book1 = Book("Python Programming")
book2 = Book("Web Development")

contract1 = author1.sign_contract(book1, "2022-01-01", 10)
contract2 = author1.sign_contract(book2, "2022-02-01", 15)

print(book1.authors())
print(author1.total_royalties())
print(Contract.contracts_by_date("2022-01-01"))
