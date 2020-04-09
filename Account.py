
import random
from faker import Faker
from faker.providers import BaseProvider

import random

from faker import Factory
fake = Factory.create()
fake.name()

fake = Faker()

# Merchant Category 
class Category(BaseProvider):
    def merch_category(self):
        merch_category = ['Tours & Travels', 'Hotel', 'Airlines', 'Clothing Store', 'Dept Stores']

        # We select a random destination from the list and return it
        return random.choice(merch_category)

# Add the TravelProvider to our faker object
fake.add_provider(Category)


# Merchant Group
class Group(BaseProvider):
    def merch_group(self):
        merch_group = ['Travels', 'Shopping', 'Petrol', 'Lifestyle', 'Health', 'Groceries', 'Dining']

        # We select a random destination from the list and return it
        return random.choice(merch_group)

# Add the TravelProvider to our faker object
fake.add_provider(Group)

# Merchant Name
class Merchant(BaseProvider):
    def merch_name(self):
        merch_name = ['123 EasyPoint',
						'1Way',
						'Abbey Travel',
						'Advance-eStore',
						'Adya Tours',
						'Aeroticket',
						'AIA Financial',
						'AirAsia',
						'Alat2kantor',
						'Alfa Online',
						'Allhotelsindo',
						'Allianz',
						'Amway',
						'Aqindo',
						'Asia Wisata',
						'Bhinneka.com',
						'BIG TV',
						'Bilna.com',
						'Biznet Networks',
						'Blackspex',
						'Blanja.com',
						'Blibli.com',
						'Blibur.com',
						'Bolt Super 4G',
						'Borobodur Herbal',
						'Braga Music',
						'Bukalapak',
						'CAF Life',
						'Cantik.com',
						'CBN',
						'CBN Cloud',
						'CheapnClick.com',
						'Cipika',
						'Citilink',
						'Cititrans.co.id',
						'CNI',
						'Cognitix',
						'Danareksa.com',
						'Datangya.com',
						'DCSindo.com',
						'DealGoing',
						'GSShop.co.id',
						'Gudang Voucher',
						'Happyholiday',
						'Harga Hot',
						'Jaco TV Shopping',
						'Jakartacamera',
						'Jakartanotebook']



        # We select a random destination from the list and return it
        return random.choice(merch_name)

# Add the TravelProvider to our faker object
fake.add_provider(Merchant)

# Merchant Group
class City(BaseProvider):
    def city_group(self):
        city_group = ['Bandung', 'Jakarta', 'Surabaya', 'Palembang', 'Purwokerto', 'Banjar', 'Tasik']

        # We select a random destination from the list and return it
        return random.choice(city_group)

# Add the TravelProvider to our faker object
fake.add_provider(City)


# Our custom provider inherits from the BaseProvider
class TravelProvider(BaseProvider):
    def destination(self):
        destinations = ['NY', 'CO', 'CA', 'TX', 'RI']

        # We select a random destination from the list and return it
        return random.choice(destinations)

# Add the TravelProvider to our faker object
fake.add_provider(TravelProvider)

# Product Type
class ProductType(BaseProvider):
    def ProductType(self):
        ProductType = ['Platinium', 'Gold', 'Classic', 'Cashback']

        # We select a random destination from the list and return it
        return random.choice(ProductType)

# Add the TravelProvider to our faker object
fake.add_provider(ProductType)

# Currency 
class Currency(BaseProvider):
    def Currency(self):
        Currency = ['IDR', 'USD', 'IPY']

        # We select a random destination from the list and return it
        return random.choice(Currency)

# Add the TravelProvider to our faker object
fake.add_provider(Currency)

# Transaction Date
class TransDate(BaseProvider):
    def TransDate(self):
        TransDate = ['010118', '010218', '010318']

        # We select a random destination from the list and return it
        return random.choice(TransDate)

# Add the TravelProvider to our faker object
fake.add_provider(TransDate)

# Transaction Type
class TransType(BaseProvider):
    def TransType(self):
        TransType = ['Retail Domestic', 'Retail Foreign', 'Online Transaction']

        # We select a random destination from the list and return it
        return random.choice(TransType)

# Add the TravelProvider to our faker object
fake.add_provider(TransType)

'''
Field   Format  Len Example
CardNumber  Char    16  5500909090912563
CustomerNumber  Char    10  1234533433
Gender  Char    2   F/M
Date of Birth   Char    DDMMYY  
Age Char    3   
Occupation  Char    100 Employee, Entrepreneur, Housewife, etc
Customer Address    Char    100 
City    Char    100 City Name (Jakarta Barat, Bandung, Semarang,etc)
ZIP CODE    Char    10  11570, 12190, etc
Country     Char    100 Indonesia, Singapore, Malaysia, US, etc
Marital Status  Char    10  Single, Married, Divorce, Widowed
Credit Limit    Numeric 10  5,000,000 ; 10,0000,0000 , etc
Card Open Date  Char    DDMMYY  
Cards Tenure (in Years) Char        Today- Card Open date
'''

# We can now use the destination method:
f = open("Account.txt","w") #opens file with name of "test.txt"
for i in range(500000):
    print(fake.credit_card_number()+ "," +fake.ssn()+ "," 
    	 +fake.city()+ "," +fake.zipcode()+ "," +fake.country() 
    	 )
    
    f.write(fake.credit_card_number()+ "," +fake.ssn()+ "," 
    	 +fake.city()+ "," +fake.zipcode()+ "," +fake.country() 
    	 )

f.close()

