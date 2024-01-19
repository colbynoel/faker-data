from pydantic import BaseModel

class ProductGroup(BaseModel):
    product_name: str
    inventory: int
    reviews: list[str]
    distributor: str
    distribution_center: str
    
class ProductIndividual(BaseModel):
    product_name: str
    upc: str
    distributor: str
    color: str
    size: str

class Address(BaseModel):
    street_information: str
    zip_code: int
    state: str
    city: str
    phone_number: str

class Cards(BaseModel):
    card_holder: str
    card_name: str
    card_number: int
    security_number: int
    expiration_date: str

class Distributor(BaseModel):
    name: str
    products: list[ProductGroup]
    rating: int
    num_employees: int

class Employee(BaseModel):
    name: str
    salary: float
    job_title: str
    time_employed: str
    employer: str

class Purchaser(BaseModel):
    name: str
    purchase_history: list[ProductGroup]
    reviews: list[str]
    shopping_cart: list[ProductIndividual]
    shipping_information: list[Address]
    cards: list[Cards]
    billing_information: list[Address]
    wishlist: list[ProductIndividual]
