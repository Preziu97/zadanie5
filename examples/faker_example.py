from faker import Faker

# Tworzymy generator danych dla języka polskiego
fake = Faker('pl_PL')

# Generujemy fikcyjne dane osobowe
full_name = fake.name()
email = fake.email()
address = fake.address()
phone = fake.phone_number()

print("Imię i nazwisko:", full_name)
print("E-mail:", email)
print("Adres:", address)
print("Telefon:", phone)

# Generujemy dane firmowe
company = fake.company()
nip = fake.vat_id()
iban = fake.iban()

print("\nFirma:", company)
print("NIP:", nip)
print("IBAN:", iban)

# Tworzymy login i dane internetowe
username = fake.user_name()
ip = fake.ipv4()
domain = fake.domain_name()

print("\nLogin:", username)
print("Adres IP:", ip)
print("Domena:", domain)

# Generujemy datę urodzenia i dzisiejszą datę
birth_date = fake.date_of_birth(minimum_age=18, maximum_age=65)
today = fake.date()

print("\nData urodzenia:", birth_date)
print("Dzisiejsza data:", today)

# Tworzymy krótką notkę o użytkowniku (bio)
bio = fake.text(max_nb_chars=100)
print("\nOpis użytkownika (bio):", bio)

# Tworzymy listę 3 fikcyjnych użytkowników
print("\nLista użytkowników:")
for i in range(3):
    name = fake.name()
    mail = fake.email()
    print(f"- {name} ({mail})")
