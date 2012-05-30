from os import urandom
from binascii import hexlify, unhexlify
from pbkdf2 import PBKDF2

defaults = {
        'charset': 'utf-8',
        'admin_salt_length': 32,
        'admin_key_length': 32,
        'admin_key_iters': 10000,
        'admin_key_hash': 'sha256',
        'admin_admins': {
            'testadmin': 'e74f48de88648e7996c568de855efbb1e74ef2196e0b226bc5ccf0226fd0c98220e75e888c18e2a274d118d0fec6ed2f72616fff7f4b53dafbcc5c3419224198'
            },
        }

class Message():
    def __init__(self, nick, password, charset):
        self.nick = nick
        self.content_raw = b'-auth ' + password.encode(charset)

class Conf():
    def __init__(self):
        self.conf = defaults

class Admin():
    def __init__(self, conf):
        self.conf = conf
        exec('from hashlib import ' + self.conf.conf['admin_key_hash'])
        self.key_length = self.conf.conf['admin_key_length']
        self.salt_length = self.conf.conf['admin_salt_length']
        self.key_hash = locals()[self.conf.conf['admin_key_hash']]

    def check_pass(self, message, args):
        try:
            pword_conf = self.conf.conf['admin_admins'][message.nick]
        except KeyError:
            print('grr')
            return

        pword_msg = b' '.join(message.content_raw.split(b' ')[1:])
        key = pword_conf[:self.key_length*2]
        salt = unhexlify(pword_conf[self.key_length*2:self.key_length*2 + self.salt_length*2].encode('us-ascii'))
        gen_key = PBKDF2(pword_msg, salt, iterations=self.conf.conf['admin_key_iters'], digestmodule=self.key_hash).hexread(self.key_length)
        if gen_key == key:
            print('woof')
        else:
            print('grr')

    def make_pass(self, message, args):
        pword_msg = b' '.join(message.content_raw.split(b' ')[1:])
        salt = urandom(self.salt_length)
        key = PBKDF2(pword_msg, salt, iterations=self.conf.conf['admin_key_iters'], digestmodule=self.key_hash).hexread(self.key_length)
        print(key + hexlify(salt).decode('us-ascii'))


nick = input('test nick : ')
password = input('test password : ')
conf = Conf()
message = Message(nick, password, conf.conf['charset'])
admin = Admin(conf)

admin.check_pass(message, None)
admin.make_pass(message, None)
