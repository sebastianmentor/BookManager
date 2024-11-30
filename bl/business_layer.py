from dal.data_access_layer import DataAccessLayer
class BusinessLayer:
    def __init__(self, data_access_layer:DataAccessLayer):
        self.dal = data_access_layer

    def add_book(self, title:str, author:str) -> None:
        data = self.dal.read_data()
        new_entry = f"{title}, {author}\n"
        self.dal.write_data(data + new_entry)

    def get_books(self) -> list[tuple[str,str]]:
        data = self.dal.read_data()
        books = data.strip().split('\n')
        return [book.split(', ') for book in books if book]
