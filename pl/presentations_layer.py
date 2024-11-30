from bl.business_layer import BusinessLayer
class PresentationLayer:
    def __init__(self, business_layer:BusinessLayer) -> None:
        self.bl = business_layer

    def add_book_ui(self) -> None:
        title = input("Ange bokens titel: ")
        author = input("Ange författarens namn: ")
        self.bl.add_book(title, author)
        print("Bok tillagd.")

    def show_books_ui(self) -> None:
        books = self.bl.get_books()
        for title, author in books:
            print(f"Titel: {title}, Författare: {author}")

    def run(self) -> None:
        while True:
            choice = input("1. Lägg till bok\n2. Visa böcker\n3. Avsluta\nVälj ett alternativ: ")
            if choice == '1':
                self.add_book_ui()
            elif choice == '2':
                self.show_books_ui()
            elif choice == '3':
                break
            else:
                print("Ogiltigt val, försök igen.")
