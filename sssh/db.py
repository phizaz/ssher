from os.path import join, exists, dirname

DB_PATH = join(dirname(__file__), 'ssher_db.txt')

class DB:
    def __init__(self):
        self.db = self.read_db()

    def get_name(self, name):
        names = list(map(lambda x: x[0], self.db))
        if name not in names:
            return False
        return self.db[names.index(name)]

    def apply_usernames(self, name, usernames):
        row = self.get_name(name)
        if not row:
            print('name not found')
            return False

        row[2] = usernames
        self.apply_db()
        return True

    def add_row(self, name, host, usernames):
        row = self.get_name(name)
        if row:
            print('duplicate name')
            return False
        self.db.append([name, host, usernames])
        self.apply_db()
        return True

    def remove_name(self, name):
        row = self.get_name(name)
        if not row:
            print('name not found')
            return False
        self.db.remove(row)
        self.apply_db()
        return True

    def read_db(self):
        # name host username(s)
        if not exists(DB_PATH):
            with open(DB_PATH, 'w') as _:
                pass

        db = []
        with open(DB_PATH, 'r') as handle:
            for line in handle:
                name, host, user = line.strip().split(' ')
                usernames = user.split(',')
                db.append([name, host, usernames])
        return db

    def apply_db(self):
        with open(DB_PATH, 'w') as handle:
            for name, host, usernames in self.db:
                handle.write('{}\n'.format(
                    ' '.join([name, host, ','.join(usernames)])
                ))