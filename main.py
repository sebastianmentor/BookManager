from bl.business_layer import BusinessLayer
from dal.data_access_layer import DataAccessLayer
from pl.presentations_layer import PresentationLayer

def main():
    dal = DataAccessLayer(f'.\\data\\books.txt')
    bl = BusinessLayer(dal)
    pl = PresentationLayer(bl)

    pl.run()

if __name__ == "__main__":
    main()
