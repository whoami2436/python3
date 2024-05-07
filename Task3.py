class Book :
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        self.current_page = 1

    def get_title(self):
        return self.title
    def get_author(self):
        return self.author
    def get_pages(self):
        return self.pages
    def get_current_page(self):
        return self.current_page
    
    def turn_page(self):
        if self.current_page < self.pages:
            self.current_page += 1
            print(f"Moved to page {self.current_page}.")
        else:
            print("you have reaced the last page.")

Sapiens = Book("Sapiens", "Yuval Noah Harari", 456)

print("Title:", Sapiens.get_title())
print("Author:", Sapiens.get_author())
print("Pages:", Sapiens.get_pages())

Sapiens.turn_page()
print("Current page:", Sapiens.get_current_page())
    



       