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
from utils.data_generation_utils import *

fake = Faker('en_US')

def generate_product_group_and_distributor():
    """
    Generates a list of product groups based on products.txt
    """
    product_groups = []
    distributors = []
    file = open("assets/products.txt", "r")
    products = file.read().split("\n")[:-1]


    end_range = 0
    while len(products) > 0:
        distributor_product_group_list = [] 
        fake_company = fake.company()
        product_group = None

        if len(products) >= 5:
            end_range = 5
        elif len(products) < 5:
            end_range = len(products)

        for _ in range(random.randint(1, end_range)):
            product_group = ProductGroup(
                product_name=products.pop(),
                inventory=random.randint(1, 10_000), 
                reviews=["Test!"],
                distributor=fake_company,
                distribution_center=fake.city())
            distributor_product_group_list.append(product_group)


        if distributor_product_group_list:
            distributors.append(Distributor(
                name = fake_company,
                products = distributor_product_group_list,
                rating = random.randint(0, 10),
                num_employees = random.randint(1, 100_000)
                ))
        if product_group is not None:
            product_groups.append(product_group)

    return product_groups, distributors


def gen_product_individual(productGroups: list[ProductGroup]) -> list[ProductIndividual]:
    """
    Generates a list of Individual Products based on the Product Group
    """
    productIndividuals = []
    for productGroup in productGroups:
        for _ in range(productGroup.inventory):
            productIndividuals.append(ProductIndividual(
                product_name=productGroup.product_name,
                upc=generate_random_upc(),
                distributor=productGroup.distributor,
                color=fake.color_name(),
                size=get_random_product_size(random.randint(0, 8))
                ))
    return productIndividuals

def gen_employees(distributors: list[Distributor]):
    employees = []
    for distributor in distributors:
        print(distributor.name)
        for _ in range(distributor.num_employees):
            employees.append(Employee(
                name=fake.name(),
                salary=fake.pyfloat(right_digits=2, positive=True, min_value=30_000, max_value=1_000_000),
                job_title=fake.job(),
                time_employed=time_worked(),
                employer=distributor.name,
                ))

    return employees


def gen_address():
    address = fake.address().split("\n")
    street_information = address[0]
    city = address[1][:address[1].find(',')]
    state = address[1][address[1].find(',')+2:address[1].rfind(' ')]
    zip_code = address[1][address[1].rfind(' '):]
    phone_number = fake.phone_number()

    return Address(
            street_information=street_information,
            zip_code= int(zip_code),
            state=state,
            city=city,
            phone_number=phone_number)




# class Cards(BaseModel):
#     card_holder: str
#     card_name: str
#     card_number: int
#     security_number: int
#     expiration_date: str

def gen_cards(purchaser: str):
    card = Cards(
            card_holder = purchaser,
            card_name = card_name(random.randint(0,8)),
            card_number = card_number(),
            security_number = security_code(),
            expiration_date = fake.date())
    return card

# class Purchaser(BaseModel):
#     name: str
#     purchase_history: list[ProductIndividual]
#     reviews: list[str]
#     shopping_cart: list[ProductIndividual]
#     shipping_information: list[Address]
#     cards: list[Cards]
#     billing_information: list[Address]
#     wishlist: list[ProductGroup]

def gen_purchaser(product_individuals: list, product_groups: list, employees: list):
    for _ in range(1_000_000):
        :




if __name__ == "__main__":
    # product_groups, distributors = generate_product_group_and_distributor()
    # product_individuals = gen_product_individual(product_groups)
    # employees = gen_employees(distributors)
    print(gen_cards("Colby"))
