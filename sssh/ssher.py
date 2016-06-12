from os.path import join, exists, dirname
from argparse import ArgumentParser
from .db import DB
import sys
import subprocess

__version__ = '0.6'

db = DB()

def add(name, host, username):
    row = db.get_name(name)
    if not row:
        # create a new row
        db.add_row(name, host, [username])
    else:
        # add to the existing row
        _, _, usernames = row
        usernames.append(username)
        db.apply_usernames(name, usernames)
    return True

def remove(name, username=None):
    row = db.get_name(name)
    if not row:
        print('name not found')
        return False

    if not username:
        db.remove_name(name)
    else:
        name, host, usernames = row
        if username not in usernames:
            print('username not found')
            return False
        db.apply_usernames(name, list(set(usernames) - {username}))
    return True

def run_command(command, verbose=False):
    job = subprocess.Popen(command, bufsize=0, shell=True, stdout=sys.stdout, stderr=sys.stderr, stdin=sys.stdin)
    job.wait()

def ssh(host, username):
    print('SSH to {}@{}'.format(username, host))
    run_command('ssh {}@{}'.format(username, host))

def main():
    parser = ArgumentParser(description='SSHER')
    parser.add_argument('--name', action='store')
    parser.add_argument('--add', action='store_true')
    parser.add_argument('--list', action='store_true')
    parser.add_argument('--remove', action='store_true')
    args = parser.parse_args()

    print('SSH-er (sssh) version: {}'.format(__version__))

    if args.add:
        # adding a new record
        print('Enter name: ', end='')
        name = input()
        row = db.get_name(name)

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
        if len(db.db) == 0:
            print('nothing in database...')
            return

        # list all the records in database
        print('List database: ')
        for name, host, usernames in db.db:
            print('name: {}({})'.format(name, host))
            print('  users: {}'.format(', '.join(usernames)))

    elif args.name:
        # perform ssh according to the name
        row = db.get_name(args.name)
        if not row:
            print('name not found')
            return
        name, host, usernames = row
        if len(usernames) == 1:
            ssh(host, usernames[0])
        else:
            for i, username in enumerate(usernames, 1):
                print('{}. {}@{}'.format(i, username, host))
            while True:
                print('Choose the username: ', end='')
                choice = int(input())
                if choice not in range(1, len(usernames) + 1):
                    print('Wrong option, try again..')
                    continue
                ssh(host, usernames[choice - 1])
                break

        print('Goodbye...')

    elif args.remove:
        # remove a record or a username
        # show names in DB
        if len(db.db) == 0:
            print('nothing in database...')
            return

        for name, host, usernames in db.db:
            print('name: {}({})'.format(name, host))

        print('Enter name to remove: ', end='')
        name = input()
        row = db.get_name(name)
        if not row:
            print('name not found')
            return
        name, host, usernames = row

        for i, username in enumerate(usernames, 1):
            print('{}. {}@{}'.format(i, username, host))

        while True:
            print('Choose the username (remove all leave blank): ', end='')
            raw_choice = input()
            if not raw_choice:
                # remove all
                remove(name)
                break
            else:
                choice = int(raw_choice)
                if choice not in range(1, len(usernames) + 1):
                    print('Wrong option, try again..')
                    continue
                remove(name, usernames[choice - 1])
                break

    else:
        print('doing nothing..')