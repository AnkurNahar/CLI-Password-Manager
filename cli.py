from cryptography.fernet import Fernet
import click
import requests
import base64

API_URL = "API_Gateway_URL"
fernet = Fernet('secret_key_here')

@click.group()
def cli():
    pass

@cli.command()
@click.option("--service", prompt="Service", help="The name of the service.")
@click.option("--username", prompt="Username", help="Your username.")
@click.option("--password", prompt="Password", hide_input=True, help="Your password.")
def store(service, username, password):
    
    encrypted_password = base64.b64encode(fernet.encrypt(password.encode())).decode('utf-8')

    data = {
        "service": service,
        "username": username,
        "password": encrypted_password
    }

    response = requests.post(f"{API_URL}", json=data)
    click.echo(response.json())

@cli.command()
@click.option("--service", prompt="Service", help="The name of the service.")
def retrieve(service):
    response = requests.get(f"{API_URL}/service", params={"service": service})
    result = response.json()
    encrypted_password_base64 = result.get('password_hash')
    byte_pass = base64.b64decode(encrypted_password_base64)
    decrypted_password = fernet.decrypt(byte_pass).decode()
    result['password'] = decrypted_password
    del result['password_hash']
    click.echo(result)

if __name__ == "__main__":
    cli()
