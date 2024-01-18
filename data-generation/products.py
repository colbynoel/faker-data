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
from utils.product_utils import *

fake = Faker()

def genProductGroups():
    """
    Generates a list of product groups based on products.txt
    """
    productGroups = []
    file = open("assets/products.txt", "r")
    products = file.read().split("\n")[:-1]

    while len(products) > 0:
        end_range = 0
        fake_company = fake.company()
        print(fake_company)
        print(len(products))
        if len(products) >= 5:
            end_range = 5
        elif len(products) < 5:
            end_range = len(products)
        for _ in range(random.randint(1, end_range)):
            productGroups.append(ProductGroup(
                product_name=products.pop(),
                inventory=random.randint(1, 10_000), 
                reviews=["Test!"],
                distributor=fake_company,
                distribution_center=fake.city()))

    return productGroups


def genProductIndividual(productGroups: list[ProductGroup]) -> list[ProductIndividual]:
    """
    Generates a list of Individual Products based on the Product Group
    """
    productIndividuals = []
    for productGroup in productGroups:
        for _ in range(productGroup.inventory):
            productIndividuals.append(ProductIndividual(
                product_name=productGroup.product_name,
                upc=generate_random_upc(),
                distributor=productGroup.distribution_center,
                color=fake.color_name(),
                size=get_random_product_size(random.randint(0, 8))
                ))
    return productIndividuals


# class Distributor(BaseModel):
#     name: str
#     products: list[ProductGroup]
#     rating: int
#     num_employees: int
#
# class Employee(BaseModel):
#     name: str
#     salary: float
#     job_title: str
#     time_employed: int
#     employer: str

# def genDistributor(productGroups: list[ProductGroup]):




if __name__ == "__main__":
    productGroups = genProductGroups()
    productIndividuals = genProductIndividual(productGroups)
