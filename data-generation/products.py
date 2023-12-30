from faker import Faker
import random
from schema import (
        Employee,
        Purchaser,
        ProductGroup,
        ProductIndividual,
        Address,
        Cards,
        Distributor
        )
fake = Faker()

# class ProductGroup(BaseModel):
#     product_name: str
#     inventory: int
#     reviews: list[str]
#     distributor: str
#     distribution_center: str

def generateProducts():
    productGroups = productGroups()
        
def productGroups():
    productGroups = []
    file = open("assets/products.txt", "r")
    products = file.read().split("\n")[:-1]
    for product in products:
        productGroups.append(ProductGroup(
            product_name=product,
            inventory=random.randint(1, 10_000), 
            reviews=["Test!"],
            distributor=fake.company(),
            distribution_center=fake.city()))

if __name__ == "__main__":
    generateProducts()
