from os.path import join, exists
from argparse import ArgumentParser
import sys

DB_PATH = 'ssher_db.txt'

def read_db():
    # name host username(s)
    if not exists(DB_PATH):
        with open(DB_PATH, 'w') as handle:
            pass

    db = []
    with open(DB_PATH, 'r') as handle:
        for line in handle:
            name, host, user = line.strip().split(' ')
            usernames = user.split(',')
            db.append([name, host, usernames])
    return db

def apply_db(db):
    with open(DB_PATH, 'w') as handle:
        for name, host, usernames in db:
            handle.write(' '.join([
                name,
                host,
                ','.join(usernames)
            ]))

DB = read_db()

def get_name(name):
    names = list(map(lambda x: x[0], DB))
    if name not in names:
        return False
    return DB[names.index(name)]

def get_host(host):
    hosts = list(map(lambda x: x[0], DB))
    if host not in hosts:
        return False
    return DB[hosts.index(host)]

def add_username(row, username):
    row[2].append(username)

def add(name=None, host=None, username=None):
    if name:
        row = get_name(name)
    elif host:
        row = get_host(host)
    else:
        print('either name or host must be entered')
        return False

    if not username:
        print('username must be entered')
        return False

    if not row:
        # create a new row
        row = [name, host, [username]]
        DB.append(row)
    else:
        # add to the existing row
        add_username(row, username)

    apply_db(DB)
    return True

def run_command(command, verbose=False):
    """
    Run the given command using the system shell
    *fix this to print output as it goes
    """
    import subprocess
    error = False

    if verbose == True:
        print(command)

    job = subprocess.Popen(command, bufsize=0, shell=True, stdout=sys.stdout, stderr=sys.stderr, stdin=sys.stdin)
    result = job.wait()

def ssh_explicit(host, username):
    print('SSH to {}@{}'.format(username, host))
    run_command('ssh {}@{}'.format(username, host))

def ssh(name):
    row = get_name(name)
    if not row:
        print('name not found')
        return
    name, host, usernames = row
    if len(usernames) == 1:
        ssh_explicit(host, usernames[0])
    else:
        for i, username in enumerate(usernames, 1):
            print('{}. {}@{}'.format(i, username, host))
        print('Choose the username: ', end='')
        choice = int(input())
        ssh_explicit(host, usernames[choice - 1])

def main():
    parser = ArgumentParser(description='SSHER')
    parser.add_argument('--name', action='store')
    parser.add_argument('--add', action='store_true')
    parser.add_argument('--list', action='store_true')
    args = parser.parse_args()

    if args.add:
        # adding a new record
        print('Enter name: ', end='')
        name = input()
        row = get_name(name)

        if row:
            name, host, usernames = row
            print('Adding username to host {}'.format(host))
        else:
            print('Enter host: ', end='')
            host = input()

        print('Enter username: ', end='')
        username = input()

        if add(name, host, username):
            print('Adding done!')
    elif args.list:
        # list all the records in database
        print('List databse: ')
        for name, host, usernames in DB:
            print('name: {}({})'.format(name, host))
            print('  users: {}'.format(', '.join(usernames)))
    elif args.name:
        # perform ssh according to the name
        ssh(args.name)
        print('Goodbye...')
    else:
        print('doing nothing..')