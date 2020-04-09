
import random
from faker import Faker
from faker.providers import BaseProvider

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

# We can now use the destination method:
#print(fake.destination())
f = open("Merchant.txt","w") #opens file with name of "test.txt"
for i in range(500000):
    print(fake.merch_category()+ "," +fake.merch_group()+ "," +fake.merch_name()+ "," +fake.city_group() )
    f.write(fake.merch_category()+ "," +fake.merch_group()+ "," +fake.merch_name()+ "," +fake.city_group()+"\n" ) 

f.close()

