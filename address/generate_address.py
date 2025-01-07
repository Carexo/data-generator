import random

class Address:
    def __init__(self, address_id, city_id, address, postal_code):
        self.AddressID = address_id
        self.CityID = city_id
        self.Address = address
        self.PostalCode = postal_code


def random_address(city_id):
    street_names = {
        "Poland": ["ul. Marszałkowska", "ul. Floriańska", "ul. Piotrkowska", "ul. Świdnicka", "ul. Półwiejska", "ul. Długa", "ul. Wojska Polskiego", "ul. Gdańska", "ul. Lubelska", "ul. Chorzowska"],
        "Germany": ["Alexanderplatz", "Reeperbahn", "Marienplatz", "Königsallee", "Kurfürstendamm", "Zeil", "Schildergasse", "Mönckebergstraße", "Tauentzienstraße", "Maximilianstraße"],
        "France": ["Rue de Rivoli", "Avenue des Champs-Élysées", "Boulevard Saint-Germain", "Rue de la Paix", "Rue du Faubourg Saint-Honoré", "Avenue Montaigne", "Boulevard Haussmann", "Rue de Rennes", "Rue de la République", "Cours Mirabeau"],
        "Italy": ["Via del Corso", "Via Condotti", "Via Montenapoleone", "Via della Spiga", "Via Veneto", "Via Nazionale", "Via Garibaldi", "Via Roma", "Corso Buenos Aires", "Via Toledo"],
        "Spain": ["Gran Vía", "La Rambla", "Paseo de Gracia", "Calle de Alcalá", "Calle de Serrano", "Calle de Preciados", "Calle de Atocha", "Calle de Fuencarral", "Calle de Goya", "Calle de Velázquez"]
    }

    if 1 <= city_id <= 10:
        country = "Poland"
    elif 11 <= city_id <= 20:
        country = "Germany"
    elif 21 <= city_id <= 30:
        country = "France"
    elif 31 <= city_id <= 40:
        country = "Italy"
    elif 41 <= city_id <= 50:
        country = "Spain"
    else:
        country = "Poland"  # Default to Poland if city_id is out of range

    return f"{random.choice(street_names[country])} {random.randint(1, 100)}"

def random_postal_code():
    return f"{random.randint(10, 99)}-{random.randint(100, 999)}"

def generate_address(addresses_number):
    addresses = []
    for i in range(1, addresses_number + 1):
        city_id = random.randint(1, 50)
        address = random_address(city_id)
        postal_code = random_postal_code()
        addresses.append(vars(Address(i, city_id, address, postal_code)))

    return addresses
