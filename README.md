# SSH-er
*Stop remembering all the hosts when using SSH*

SSH-er does all the remembering for you, just type `sssh --name=<sth>` and you're good to go.

# Installation
`sssh` is used in `pip` instead of `ssher` due to the name collision.
You can easily install using this command.

```
pip install sssh
```

# Usage
There are 4 options as follows:

* `--name` (version 0.7: or type the name without any option) use this to perform `ssh`, but instead of using username and host you can simply use an arbitrary name that you have given to the host.
* `--list` show all the hosts, names and usernames in the database.
* `--add` use this to add a new host and username into the database, you can give it a name during the process.
* (version 0.6) `--remove` use this to remove either a name or a username from the database.

# Example

## Adding
```
$ sssh --add
Enter name: test
Enter host: 192.168.1.1
Enter username: me  
Adding done!
$ sssh --add 
Enter name: test
Adding username to host 192.168.1.1
Enter username: you 
Adding done!
```

## Listing
```
$ sssh --list
name: test(192.168.1.1)
  users: me, you
```

## Connect
```
$ sssh --name=test
1. me@192.168.1.1
2. you@192.168.1.1
Choose the username: 1   
SSH to me@192.168.1.1
```

or (version 0.7)

```
$ sssh test
1. me@192.168.1.1
2. you@192.168.1.1
Choose the username: 1   
SSH to me@192.168.1.1
```

## Remove 
(added in version 0.6)

```
$ sssh --remove
name: test(192.168.1.1)
Enter name to remove: test
1. me@192.168.1.1
2. you@192.168.1.1
Choose the username (remove all leave blank): 1 
```