import os
import subprocess

import click


@click.command()
@click.option("--user", help="ssh user")
@click.option("--host", help="ssh host")
@click.option("--port", help="ssh port")
@click.option("--turn", required=True, help="options are: 'on' or 'off'")
def main(user, host, port, turn):
    if turn == 'off':
        turnoff()
        return

    if not user:
        user = click.prompt('Please enter a username', type=str)
    
    if not host:
        host = click.prompt('Please enter a host', type=str)
        
    if not port:
        port = click.prompt('Please enter a port', type=int)
    
    connect(user, host, port)

def connect(user, host, port):
    clear()
    click.echo(f"Connecting to: {user}@{host} -p{port}!")
    os.system(f'ssh -f -N -M -S /tmp/sshtunnel -D 1090 {user}@{host} -p{port}')
    os.system('networksetup -setsocksfirewallproxy wi-fi 127.0.0.1 1090')
    os.system('networksetup -setsocksfirewallproxystate wi-fi on')

def clear():
    if os.path.exists('/tmp/sshtunnel'):
        os.remove('/tmp/sshtunnel')
    try:
        output = subprocess.getoutput("lsof -nP -tiTCP:1090")
        for pid in output.split('\n'):
            if pid:
                os.system(f'kill -9 {pid}')
    except Exception:
        pass

def turnoff():
    click.echo(f"turning off proxy")
    clear()
    os.system('networksetup -setsocksfirewallproxystate wi-fi off')

if __name__ == '__main__':
    main()
