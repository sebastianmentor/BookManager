class BusinessLayer:
    def __init__(self, data_access_layer):
        self.dal = data_access_layer

    def add_book(self, title, author):
        data = self.dal.read_data()
        new_entry = f"{title}, {author}\n"
        self.dal.write_data(data + new_entry)

    def get_books(self):
        data = self.dal.read_data()
        books = data.strip().split('\n')
        return [book.split(', ') for book in books if book]
