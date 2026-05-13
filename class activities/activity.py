import json, uuid, datetime
 
class Base:
    def __init__(self):
        self.id         = str(uuid.uuid4())
        self.created_at = datetime.datetime.now().isoformat()
        self.updated_at = datetime.datetime.now().isoformat()
 
    def save(self): 
        self.updated_at = datetime.datetime.now().isoformat()
        with open(f"{self.name}.json", "w") as f:
            json.dump(vars(self), f, indent=4)
 
    def load(self):
        with open(f"{self.name}.json") as f:
            self.__dict__.update(json.load(f))
 
 
class Book(Base):
    def __init__(self, name, author, year, genre):
        super().__init__()
        self.name      = name
        self.author      = author
        self.year        = year      
        self.genre       = genre
        self.is_borrowed = False
 
 
class User(Base):
    def __init__(self, name, user_id):
        super().__init__()
        self.name    = name
        self.user_id = user_id
 
    def borrow_book(self, book):
        if not book.is_borrowed:
            book.is_borrowed = True
            book.save() 
            print(f"{book.name} borrowed by {self.name}")
        else:
            print(f"{book.name} is not available")
 
 
book1 = Book("Python","Ali", 2020, "Programming")
book2 = Book("C++", "Robert", 2008, "Programming")
user1 = User("Alice", "001")
user2 = User("Bob",   "002")
 
for obj in [book1, book2, user1, user2]:  
    obj.save()
 
user1.borrow_book(book1)
user2.borrow_book(book1)
user2.borrow_book(book2)

