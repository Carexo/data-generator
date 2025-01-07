
import random
import string

from config.address_config import AddressConfig
from config.user_config import UserConfig
from utils.random_data import random_date

PHONE_NUMBER_LENGTH = 9
PERCENT_OF_COUNTRY_CODE_PHONE = 0.8
PERCENT_OF_ACTIVE_USERS = 0.9

class User:
    def __init__(self, user_id, first_name, last_name, email, personal_phone, date_of_birth, address_id, active):
        self.UserID = user_id
        self.FirstName = first_name
        self.LastName = last_name
        self.Email = email
        self.PersonalPhone = personal_phone
        self.DateOfBirth = date_of_birth
        self.AddressID = address_id
        self.Active = active


first_names = [
    "John", "Jane", "Alice", "Bob", "Charlie", "Diana", "Edward", "Fiona", "George", "Hannah",
    "Ivy", "Jack", "Karen", "Liam", "Mona", "Nina", "Oscar", "Paul", "Quinn", "Rachel",
    "Sam", "Tina", "Uma", "Victor", "Wendy", "Xander", "Yara", "Zane", "Aaron", "Bella",
    "Chris", "David", "Eve", "Frank", "Grace", "Helen", "Isaac", "Julia", "Kevin", "Laura",
    "Mike", "Nora", "Oliver", "Peter", "Queen", "Ron", "Steve", "Tom", "Ursula", "Vince",
    "Walter", "Xenia", "Yvonne", "Zach", "Abby", "Ben", "Cathy", "Dan", "Ellen", "Fred",
    "Gina", "Harry", "Iris", "James", "Kathy", "Leo", "Megan", "Nathan", "Olivia", "Patrick",
    "Quincy", "Rebecca", "Scott", "Tara", "Ulysses", "Violet", "Will", "Ximena", "Yosef", "Zara",
    "Adam", "Brenda", "Carl", "Derek", "Elena", "Felix", "Gloria", "Hank", "Isabel", "Jerry",
    "Kara", "Louis", "Molly", "Nick", "Opal", "Phil", "Queenie", "Ralph", "Sophie", "Trent",
    "Umar", "Vera", "Wes", "Xander", "Yvette", "Zack", "Aiden", "Brianna", "Cody", "Diana",
    "Ethan", "Faith", "Gabe", "Holly", "Ian", "Jill", "Kyle", "Lily", "Mason", "Nina",
    "Owen", "Paula", "Quinn", "Rita", "Sean", "Tina", "Uri", "Vince", "Wendy", "Xena",
    "Yara", "Zane", "Alex", "Brittany", "Connor", "Daisy", "Eli", "Fiona", "Gavin", "Hannah",
    "Isaiah", "Jade", "Kurt", "Lana", "Miles", "Nora", "Oscar", "Penny", "Quentin", "Rose",
    "Spencer", "Tess", "Ursula", "Victor", "Willow", "Xavier", "Yasmin", "Zoe", "Amber", "Blake",
    "Cameron", "Dylan", "Ella", "Finn", "Grace", "Henry", "Ivy", "Jake", "Kelsey", "Liam",
    "Mia", "Noah", "Olivia", "Parker", "Quinn", "Ryan", "Samantha", "Tyler", "Uma", "Violet",
    "Wyatt", "Xander", "Yvonne", "Zachary", "Ava", "Brody", "Chloe", "Derek", "Emma", "Felix",
    "Giselle", "Hudson", "Isla", "Jack", "Kylie", "Logan", "Maya", "Nolan", "Owen", "Piper",
    "Quinn", "Riley", "Sophia", "Tristan", "Ulysses", "Victoria", "Wesley", "Ximena", "Yara", "Zane"
]

last_names = [
    "Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez",
    "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson", "Thomas", "Taylor", "Moore", "Jackson", "Martin",
    "Lee", "Perez", "Thompson", "White", "Harris", "Sanchez", "Clark", "Ramirez", "Lewis", "Robinson",
    "Walker", "Young", "Allen", "King", "Wright", "Scott", "Torres", "Nguyen", "Hill", "Flores",
    "Green", "Adams", "Nelson", "Baker", "Hall", "Rivera", "Campbell", "Mitchell", "Carter", "Roberts",
    "Gomez", "Phillips", "Evans", "Turner", "Diaz", "Parker", "Cruz", "Edwards", "Collins", "Reyes",
    "Stewart", "Morris", "Morales", "Murphy", "Cook", "Rogers", "Morgan", "Peterson", "Cooper", "Reed",
    "Bailey", "Bell", "Gomez", "Kelly", "Howard", "Ward", "Cox", "Diaz", "Richardson", "Wood",
    "Watson", "Brooks", "Bennett", "Gray", "James", "Reyes", "Cruz", "Hughes", "Price", "Myers",
    "Long", "Foster", "Sanders", "Ross", "Morales", "Powell", "Sullivan", "Russell", "Ortiz", "Jenkins",
    "Gutierrez", "Perry", "Butler", "Barnes", "Fisher", "Henderson", "Coleman", "Simmons", "Patterson", "Jordan",
    "Reynolds", "Hamilton", "Graham", "Kim", "Gonzales", "Alexander", "Ramos", "Wallace", "Griffin", "West",
    "Cole", "Hayes", "Chavez", "Gibson", "Bryant", "Ellis", "Stevens", "Murray", "Ford", "Marshall",
    "Owens", "Mcdonald", "Harrison", "Ruiz", "Kennedy", "Wells", "Alvarez", "Woods", "Mendoza", "Castillo",
    "Olson", "Webb", "Washington", "Tucker", "Freeman", "Burns", "Henry", "Vasquez", "Snyder", "Simpson",
    "Crawford", "Jimenez", "Porter", "Mason", "Shaw", "Gordon", "Wagner", "Hunter", "Romero", "Hicks",
    "Dixon", "Hunt", "Palmer", "Robertson", "Black", "Holmes", "Stone", "Meyer", "Boyd", "Mills",
    "Warren", "Fox", "Rose", "Rice", "Moreno", "Schmidt", "Patel", "Ferguson", "Nichols", "Herrera",
    "Medina", "Ryan", "Fernandez", "Weaver", "Daniels", "Stephens", "Gardner", "Payne", "Kelley", "Dunn",
    "Pierce", "Arnold", "Tran", "Spencer", "Peters", "Hawkins", "Grant", "Hansen", "Castro", "Hoffman",
    "Hart", "Elliott", "Cunningham", "Knight", "Bradley", "Carroll", "Hudson", "Duncan", "Armstrong", "Berry",
    "Andrews", "Johnston", "Ray", "Lane", "Riley", "Carpenter", "Perkins", "Aguilar", "Silva", "Richards",
    "Willis", "Matthews", "Chapman", "Lawrence", "Garza", "Vargas", "Watkins", "Wheeler", "Larson", "Carlson",
    "Harper", "George", "Greene", "Burke", "Guzman", "Morrison", "Munoz", "Jacobs", "Obrien", "Lawson",
    "Franklin", "Lynch", "Bishop", "Carr", "Salazar", "Austin", "Mendez", "Gilbert", "Jensen", "Williamson",
    "Montgomery", "Harvey", "Oliver", "Howell", "Dean", "Hanson", "Weber", "Garrett", "Sims", "Burton",
    "Fuller", "Soto", "Mccoy", "Welch", "Chen", "Schultz", "Walters", "Reid", "Fields", "Walsh",
    "Little", "Fowler", "Bowman", "Davidson", "May", "Day", "Schneider", "Newman", "Brewer", "Lucas",
    "Holland", "Wong", "Banks", "Santos", "Curtis", "Pearson", "Delgado", "Valdez", "Pena", "Rios",
    "Douglas", "Sandoval", "Barrett", "Hopkins", "Keller", "Guerrero", "Stanley", "Bates", "Alvarado", "Beck",
    "Ortega", "Wade", "Estrada", "Contreras", "Barnett", "Caldwell", "Santiago", "Lambert", "Powers", "Chambers",
    "Nunez", "Craig", "Leonard", "Lowe", "Rhodes", "Byrd", "Gregory", "Shelton", "Frazier", "Becker",
    "Maldonado", "Fleming", "Vega", "Sutton", "Cohen", "Jennings", "Parks", "Mcdaniel", "Watts", "Barker",
    "Norris", "Vaughn", "Vazquez", "Holt", "Schwartz", "Steele", "Benson", "Neal", "Dominguez", "Horton",
    "Terry", "Wolfe", "Hale", "Lyons", "Graves", "Haynes", "Miles", "Park", "Warner", "Padilla",
    "Bush", "Thornton", "Mccarthy", "Mann", "Zimmerman", "Erickson", "Fletcher", "Mckinney", "Page", "Dawson",
    "Joseph", "Marquez", "Reeves", "Klein", "Espinoza", "Baldwin", "Moran", "Love", "Robbins", "Higgins",
    "Ball", "Cortez", "Le", "Griffith", "Bowen", "Sharp", "Cummings", "Ramsey", "Hardy", "Swanson",
    "Barber", "Acosta", "Luna", "Chandler", "Blair", "Daniel", "Cross", "Simon", "Dennis", "Oconnor",
    "Quinn", "Gross", "Navarro", "Moss", "Fitzgerald", "Doyle", "Mclaughlin", "Rojas", "Rodgers", "Stevenson",
    "Singh", "Yang", "Figueroa", "Harmon", "Newton", "Paul", "Manning", "Garner", "Mcgee", "Reese",
    "Francis", "Burgess", "Adkins", "Goodman", "Curry", "Brady", "Christensen", "Potter", "Walton", "Goodwin",
    "Mullins", "Molina", "Webster", "Fischer", "Campos", "Avila", "Sherman", "Todd", "Chang", "Blake",
    "Malone", "Wolf", "Hodges", "Juarez", "Gill", "Farmer", "Hines", "Gallagher", "Duran", "Hubbard",
    "Cannon", "Miranda", "Wang", "Saunders", "Tate", "Mack", "Hammond", "Carrillo", "Townsend", "Wise",
    "Ingram", "Barton", "Mejia", "Ayala", "Schroeder", "Hampton", "Rowe", "Parsons", "Frank", "Waters",
    "Strickland", "Osborne", "Maxwell", "Chan", "Deleon", "Norman", "Harrington", "Casey", "Patton", "Logan",
    "Bowers", "Mueller", "Glover", "Floyd", "Hartman", "Buchanan", "Cobb", "French", "Kramer", "Mccormick",
    "Clarke", "Tyler", "Gibbs", "Moody", "Conner", "Sparks", "Mcguire", "Leon", "Bauer", "Norton",
    "Pope", "Flynn", "Hogan", "Robles", "Salinas", "Yates", "Lindsey", "Lloyd", "Marsh", "Mcbride",
    "Owen", "Solis", "Pham", "Lang", "Pratt", "Lara", "Brock", "Ballard", "Trujillo", "Shaffer",
    "Drake", "Roman", "Aguirre", "Morton", "Stokes", "Lamb", "Pacheco", "Patrick", "Cochran", "Shepherd",
    "Cain", "Burnett", "Hess", "Li", "Cervantes", "Olsen", "Briggs", "Ochoa", "Cabrera", "Velasquez",
    "Montoya", "Roth", "Meyers", "Cardenas", "Fuentes", "Weiss", "Hoover", "Wilkins", "Nicholson", "Underwood",
    "Short", "Carson", "Morrow", "Colon", "Holloway", "Summers", "Bryan", "Petersen", "Mckenzie", "Serrano",
    "Wilcox", "Carey", "Clayton", "Poole", "Calderon", "Gallegos", "Greer", "Rivas", "Guerra", "Decker",
    "Collier", "Wall", "Whitaker", "Bass", "Flowers", "Davenport", "Conley", "Houston", "Huff", "Copeland",
    "Hood", "Monroe", "Massey", "Roberson", "Combs", "Franco", "Larsen", "Pittman", "Randall", "Skinner",
    "Wilkinson", "Kirby", "Cameron", "Bridges", "Anthony", "Richard", "Kirk", "Bruce", "Singleton", "Mathis",
    "Bradford", "Boone", "Abbott", "Charles", "Allison", "Sweeney", "Atkinson", "Horn", "Jefferson", "Rosales",
    "York", "Christian", "Phelps", "Farrell", "Castaneda", "Nash", "Dickerson", "Bond", "Wyatt", "Foley",
    "Chase", "Gates", "Vincent", "Mathews", "Hodge", "Garrison", "Trevino", "Villarreal", "Heath", "Dalton",
    "Valencia", "Callahan", "Hensley", "Atkins", "Huffman", "Roy", "Boyer", "Shields", "Lin", "Hancock",
    "Grimes", "Glenn", "Cline", "Delacruz", "Camacho", "Dillon", "Parrish", "Oneill", "Melton", "Booth",
    "Kane", "Berg", "Harrell", "Pitts", "Savage", "Wiggins", "Brennan", "Salas", "Marks", "Russo",
    "Sawyer", "Baxter", "Golden", "Hutchinson", "Liu", "Walter", "Mcdowell", "Wiley", "Rich", "Humphrey",
    "Johns", "Koch", "Suarez", "Hobbs", "Beard", "Gilmore", "Ibarra", "Keith", "Macias", "Khan",
    "Andrade", "Ware", "Stephenson", "Henson", "Wilkerson", "Dyer", "Mcclure", "Blackwell", "Mercado", "Tanner",
    "Eaton", "Clay", "Barron", "Beasley", "Oneal", "Preston", "Small", "Wu", "Zamora", "Macdonald",
    "Vance", "Snow", "Mcclain", "Stafford", "Orozco", "Barry", "English", "Shannon", "Kline", "Jacobson",
    "Woodard", "Huang", "Kemp", "Mosley", "Prince", "Merritt", "Hurst", "Villanueva", "Roach", "Nolan",
    "Lam", "Yoder", "Mccullough", "Lester", "Santana", "Valenzuela", "Winters", "Barrera", "Leach", "Orr",
    "Berger", "Mckee", "Strong", "Conway", "Stein", "Whitehead", "Bullock", "Escobar", "Knox", "Meadows",
    "Solomon", "Velez", "Odonnell", "Kerr", "Stout", "Blankenship", "Browning", "Kent", "Lozano", "Bartlett",
    "Pruitt", "Buck", "Barr", "Gaines", "Durham", "Gentry", "Mcintyre", "Sloan", "Melendez", "Rocha",
    "Herman", "Sexton", "Moon", "Hendricks", "Rangel", "Stark", "Lowery", "Hardin", "Hull", "Sellers",
    "Ellison", "Calhoun", "Gillespie", "Mora", "Knapp", "Mccall", "Morse", "Dorsey", "Weeks", "Nielsen",
    "Livingston", "Leblanc", "Mclean", "Bradshaw", "Glass", "Middleton", "Buckley", "Schaefer", "Frost", "Howe",
    "House", "Mcintosh", "Ho", "Pennington", "Reilly", "Hebert", "Mcfarland", "Hickman", "Noble", "Spears",
    "Conrad", "Arias", "Galvan", "Velazquez", "Huynh", "Frederick", "Randolph", "Cantu", "Fitzpatrick", "Mahoney",
    "Peck", "Villa", "Michael", "Donovan", "Mcconnell", "Walls", "Boyle", "Mayer", "Zuniga", "Giles",
    "Pineda", "Pace", "Hurley", "Mays", "Mcmillan", "Crosby", "Ayers", "Case", "Bentley", "Shepard",
    "Everett", "Pugh", "David", "Mcmahon", "Dunlap", "Bender", "Hahn", "Harding", "Acevedo", "Raymond",
    "Blackburn", "Duffy", "Landry", "Dougherty", "Bautista", "Shah", "Potts", "Arroyo", "Valentine", "Meza",
    "Gould", "Vaughan", "Fry", "Rush", "Avery", "Herring", "Dodson", "Clements", "Sampson", "Tapia",
    "Bean", "Lynn", "Crane", "Farley", "Cisneros", "Benton", "Ashley", "Mckay", "Finley", "Best",
    "Blevins", "Friedman", "Moses", "Sosa", "Blanchard", "Huber", "Frye", "Krueger", "Bernard", "Rosario",
    "Rubio", "Mullen", "Benjamin", "Haley", "Chung", "Moyer", "Choi", "Horne", "Yu", "Woodward",
    "Ali", "Nixon", "Hayden", "Rivers", "Estes", "Mccarty", "Richmond", "Stuart", "Maynard", "Brandt",
    "Oconnell", "Hanna", "Sanford", "Sheppard", "Church", "Burch", "Levy", "Rasmussen", "Coffey", "Ponce",
    "Faulkner", "Donaldson", "Schmitt", "Novak", "Costa", "Montes", "Booker", "Cordova", "Waller", "Arellano",
    "Maddox", "Mata", "Bonilla", "Stanton", "Compton", "Kaufman", "Dudley", "Mcpherson", "Beltran", "Dickson",
    "Mccann", "Villegas", "Proctor", "Hester", "Cantrell", "Daugherty", "Cherry", "Bray", "Davila", "Rowland",
    "Levine", "Madden", "Spence", "Good", "Irwin", "Werner", "Krause", "Petty", "Whitney", "Baird",
    "Hooper", "Pollard", "Zavala", "Jarvis", "Holden", "Haas", "Hendrix", "Mcgrath", "Bird", "Lucero",
    "Terrell", "Riggs", "Joyce", "Mercer", "Rollins", "Galloway", "Duke", "Odom", "Andersen", "Downs",
    "Hatfield", "Benitez", "Archer", "Huerta", "Travis", "Mcneil", "Hinton", "Zhang", "Hays", "Mayo",
    "Fritz", "Branch", "Mooney", "Ewing", "Ritter", "Esparza", "Frey", "Braun", "Gay", "Riddle",
    "Haney", "Kaiser", "Holder", "Chaney", "Mcknight", "Gamble", "Vang", "Cooley", "Carney"]


domains = [
    "example.com", "mail.com", "test.com", "domain.com", "email.com", "webmail.com", "inbox.com", "mailbox.com",
    "post.com", "internet.com", "online.com", "site.com", "web.com", "net.com", "org.com", "co.com",
    "biz.com", "info.com", "pro.com", "name.com", "me.com", "us.com", "uk.com", "ca.com",
    "eu.com", "asia.com", "africa.com", "australia.com", "america.com", "world.com", "global.com", "planet.com",
    "earth.com", "universe.com", "galaxy.com", "star.com", "moon.com", "sun.com", "sky.com", "cloud.com",
    "space.com", "cosmos.com", "nebula.com", "comet.com", "asteroid.com", "meteor.com", "satellite.com", "orbit.com",
    "rocket.com", "shuttle.com", "station.com", "mission.com", "explore.com", "discover.com", "adventure.com", "journey.com",
    "voyage.com", "expedition.com", "quest.com", "search.com", "find.com", "seek.com", "look.com", "view.com",
    "watch.com", "observe.com", "monitor.com", "track.com", "trace.com", "follow.com", "pursue.com", "chase.com",
    "hunt.com", "capture.com", "catch.com", "grab.com", "hold.com", "keep.com", "store.com", "save.com",
    "protect.com", "guard.com", "defend.com", "shield.com", "secure.com", "lock.com", "key.com", "code.com",
    "cipher.com", "encrypt.com", "decrypt.com", "decode.com", "encode.com", "translate.com", "interpret.com", "understand.com"
]



def random_phone():
    if random.random() < PERCENT_OF_COUNTRY_CODE_PHONE:
        return f"+{random.randint(1, 99)}{''.join(random.choices(string.digits, k=PHONE_NUMBER_LENGTH))}"
    else:
        return ''.join(random.choices(string.digits, k=PHONE_NUMBER_LENGTH))

def generate_users():
    users_number = UserConfig.get_total_users()
    users = []

    for i in range(1, users_number + 1):
        first_name = random.choice(first_names)
        last_name = random.choice(last_names)
        email = f"{first_name.lower()}.{last_name.lower()}{random.randint(1, 1000)}@{random.choice(domains)}"
        personal_phone = random_phone()
        date_of_birth = random_date().strftime("%Y-%m-%d")
        address_id = random.randint(1, AddressConfig.get_total_addresses())
        active = 1 if random.random() < PERCENT_OF_ACTIVE_USERS else 0


        users.append(vars(User(i, first_name, last_name, email, personal_phone, date_of_birth, address_id, active)))

    return users
