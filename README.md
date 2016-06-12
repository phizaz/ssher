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
There are 3 options as follows:

* `--name` use this to perform `ssh`, but instead of using username and host you can simply use an arbitrary name that you have given to the host.
* `--list` show all the hosts, names and usernames in the database.
* `--add` use this to add a new host and username into the database, you can give it a name during the process.

# Example

## Adding
```
$ sssh --add
Enter name: test
Enter host: 192.168.1.1
Enter username: me  
Adding done!
```

## Listing
