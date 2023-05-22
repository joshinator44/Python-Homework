#! usr/bin/env python3
from objects import Product, Book, Movie

def show_products(products):
    print("PRODUCTS")
    for i in range(len(products)):
        product = products[i]
        print(str(i+1) + ". " + product.get_description())
    print()
def show_product(product):
    print("PRODUCT DATA")
    print("Name:         ", product.name)
    if isinstance(product, Book):
        print("Author:        ", product.author)
    if isinstance(product, Movie):
        print("Uear:          ", product.year)
    print("Discount price:     {:.2f}".format(product.get_discount_price()))
    print()


def main():
    print("The Product Viewer program")
    print()


    products = (Product('King of Tokyo', 31.99, 10),
                Book('The Hobbit', 10.63, 34, "J.R.R. Tolkien"),
                Movie('The Holy Grail - DVD', 14.99, 68, 1975))
    show_products(products)
    while True:
        selection = int(input("Enter product number: "))
        print()

        product = products[selection-1]
        show_product(product)

        choice = input("Continue? (y/n): ")
        print()
        if choice != "y":
            break
if __name__ == "__main__":
    main()
    
