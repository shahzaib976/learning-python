class Library:
    def __init__(self):
        self.books=[]

    def add_book(self,bookName,writerName):
        book = {
            "BookName" : bookName,
            "Written by" : writerName
        }
        if len(self.books)>0:
            book["id"] = self.books[-1]["id"]+1
        else:
            book["id"]=1
        self.books.append(book)
        print(f"Book added - {book.get("BookName")}")

    def remove_book(self,id):
        for book in self.books:
            if book["id"]==id:
                self.books.remove(book)
                print(f"Book removed - {book.get("BookName")}")

    def view_books_list(self):
        if len(self.books)==0:
            print("No Books In The List")
        else:
            # print(f"Book List = {self.books}")
         for list in self.books:
            print('Book = ', list)


quaid_library = Library()
quaid_library.add_book("Physics","Newton")
quaid_library.add_book("Urdu","Iqbal")
quaid_library.add_book("Maths","Quaid")
quaid_library.add_book("English","Israr")
quaid_library.add_book("Biology","Khalid")
quaid_library.add_book("Chemistry","Zakir")
quaid_library.remove_book(1)
quaid_library.view_books_list()
print(quaid_library.books)







