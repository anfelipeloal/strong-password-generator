from cgi import print_arguments
import click

from src.strong_password_generator.sqlite import start_database
from src.strong_password_generator.password import Password

@click.command()
@click.option("--site", prompt="Site or Application name", help="Site or application name.")
@click.option("--url", prompt="Site RUL", default="",help="Site URL.")
@click.option("--email", prompt="Email",help="Email associated with the password.")
def generate_password(site, url, email):
    start_database()

    password = Password()
    strong_password = password.create_password(site, url, email)
    print(f"The password for site: {site} and email: {email} is:")
    print(strong_password)

@click.command()
@click.option("--value", prompt="Site, Application or URL", help="Site, application or URL to search the password.")
def searhc_password(value):
    start_database()

    password = Password()
    results = password.search_password(value)

    print(f"We found {len(results)} passwords:")
    print("----------------------------------------")

    for password in results:
        print(f"Site: {password[1]}")
        print(f"Site URL: {password[2]}")
        print(f"Email: {password[3]}")
        print(f"Password: {password[4]}")
        print("----------------------------------------")
