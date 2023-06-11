from custom_exceptions import MustContainAtSymbolError, InvalidDomainError, NameTooShortError

valid_domains = ("com", "bg", "org", "net")

def valid_email(email):
    try:
        name, domain = email.split("@")
    except ValueError:
        raise MustContainAtSymbolError("Email must contain @")

    try:
        name, extension = domain.split(".")
    except ValueError:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    if extension not in valid_domains:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    if len(name) < 4:
        raise NameTooShortError("Name must be more than 4 characters")

    return True


email = input()

while email != "End":
    if valid_email(email):
        print("Email is valid")
    email = input()

