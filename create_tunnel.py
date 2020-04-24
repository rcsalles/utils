import os
import subprocess

import click


@click.command()
@click.option("--user", help="ssh user")
@click.option("--host", help="ssh host")
@click.option("--port", help="ssh port")
def create(user, host, port):
    if not user:
        user = click.prompt('Please enter a username', type=str)
    
    if not host:
        host = click.prompt('Please enter a host', type=str)
        
    if not port:
        port = click.prompt('Please enter a port', type=int)
    
    click.echo(f"Connection to: {user}@{host} -p{port}!")
    clear()
    connect(user, host, port)

def connect(user, host, port):
    os.system(f'ssh -f -N -M -S /tmp/sshtunnel -D 1090 {user}@{host} -p{port}')
    os.system('networksetup -setsocksfirewallproxy wi-fi 127.0.0.1 1090')
    os.system('networksetup -setsocksfirewallproxystate wi-fi on')

def clear():
    if os.path.exists('/tmp/sshtunnel'):
        os.remove('/tmp/sshtunnel')
    try:
        output = subprocess.check_output("lsof -nP -tiTCP:1090", shell=True)
        if output:
            os.system(f'kill -9 {output}')
    except Exception:
        pass

if __name__ == '__main__':
    create()
