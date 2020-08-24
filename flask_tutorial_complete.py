class classTest:
   '''
        Isntance method is used when we need to peform any action inside the class. say need to connect to DB, reading data
        classMethod is used when we need to work on factory data
        Static Method : when the method need to have any thing from class. Static method is like a simple function and rarely used inside the class

   ''' 


    # Defining the instance method
    def instanceMethod(self):
        print(f'Calling the instance method of {self}')

    # Defining the class method
    @classmethod
    def classMethod(cls):
        print(f'calling class method of type {cls}')

    # Defining the static method
    @staticmethod
    def staticMethod():
        print(f'Calling the static functon')

#classTest.instanceMethod(classTest)
#classTest.classMethod()
#classTest.staticMethod()


class Book:
    type = ('Hardcover', 'Softcover')
    def __init__(self, name, booktype, price):
        self.name = name
        self.booktype = booktype
        self.price = price

    def __repr__(self):
        return (f'<Book {self.name} {self.booktype} is having price {self.price}')

    @classmethod
    def type1(cls, name, price):
        print(cls.type[0])
        return Book(name, cls.type[0], price)
    
    @classmethod
    def type2(cls, name, price):
        return Book(name, cls.type[1], price)


#book = Book('ABC', 'T1', '1500')
#print(book)

book = Book.type1('A', 1000)
book2 = Book.type2('B', 2000)
print(book)
print(book2)



######### Calling a class and add and return store details
class Store:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, name, price):
        self.items.append({
            'name': name,
            'price': price
        })

    def stock_price(self):
        total = 0
        for item in self.items:
            total += item['price']
        return total

    @classmethod
    def franchise(cls, store):
        # Return another store, with the same name as the argument's name, plus " - franchise"
        return Store(store.name, " - franchise")

    @staticmethod
    def store_details(store):
        # Return a string representing the argument
        # It should be in the format 'NAME, total stock price: TOTAL'
        return "{}, total stock price: {}".format(store.name, int(store.stock_price()))


# 4) CLASS INHERITANCE EXAMPLE

'''
CLASS INGERITANCE: Pass the list of the devices and paper, inherit class 2 from class1
'''

class Device():
    def __init__(self, name, connected_by):
        self.name = name
        self.connected_by = connected_by
        self.connected = True

    def __str__(self):
        return f"Device is {self.name} and connected by {self.connected_by}"

    def disconnected(self):
        self.connected = False       


class Printer(Device):
    def __init__(self, name, connected_by, capacity):
        super().__init__(name, connected_by)
        self.capacaity = capacity
        self.remaining = capacity

    def __str__(self):
        return f"{super().__str__()} (remaining pages are {self.remaining})"

    def remaining_pages(self, pages):
        if not self.connected:
            return
        print("Pages are {pages}")
        self.remaining -=  pages

print(Printer('A', 'B', 100))
Printer.remaining_pages(43)



#print(Device('A', 'B'))


'''
COMPONENT CLASS:- To call the content of one class and use in another class
'''
class Salary:
    def __init__(self, pay):
        self.pay = pay

    def total_salary(self):
        return self.pay * 12


class Employee:
    def __init__(self, pay, bonus):
        self.pay = pay
        self.bonus = bonus
        self.component_salary = Salary(self.pay)

    def annual_salary(self):
        return 'Total: ' + str(self.component_salary.total_salary() + self.bonus)

e1 = Employee(600, 500)
print(e1.annual_salary())


# Ex 2 ---- Use the book class to pass the multiple books and calculte the length of books using bookshelf class
class bookshelf:
    def __init__(self, *books):
        self.books = books

    def __str__(self):
        return f"count of books {len(self.books)}"


class book:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Name of the book {self.name}"

print(book('book1'))

book1 = book('ABC')
book2 = book('XYZ')

print(bookshelf(book1, book2))

# CUSTOM ERRORS
class totalPagesExceed(ValueError):
    pass


class book:
    def __init__(self, name : str, total_pages: int):
        self.name = name
        self.total_pages = total_pages
        self.pages_read = 0

    def __repl__(self):
        return(
            f"Book {self.name} is having {self.total_pages}"
        )

    def read_pages(self, pages: int):
        if self.pages_read + pages > self.total_pages:
            raise totalPagesExceed(f"Number of read pages are more than total pages in the book")
        self.pages_read = self.pages_read + pages
        print(f"{self.pages_read} reead out of {self.total_pages}")


book1 = book('A', 60)
book1.read_pages(23)
book1.read_pages(75)

    