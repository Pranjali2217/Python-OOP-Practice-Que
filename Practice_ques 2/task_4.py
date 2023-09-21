class book:
    def __init__(self,title,author):
        self.title=title
        self.author=author

    def books_details(self):
        print("enter books title: ",self.title)
        print("enter books author: ",self.author)

obj=book('harry potter','jack')
obj.books_details()