from setuptools import setup
import re

version = re.search(
    '^__version__\s*=\s*\'(.*)\'',
    open('sssh/ssher.py').read(),
    re.M
).group(1)

print('version = {}'.format(version))

setup(
    name = 'sssh',
    packages = ['sssh'],
    entry_points={
        "console_scripts": ['sssh = sssh.ssher:main']
    },
    version = version,
    description = 'Stop remembering all the hosts when using SSH',
    author = 'Konpat Preechakul',
    author_email = 'the.akita.ta@gmail.com',
    url = 'https://github.com/phizaz/ssher', # use the URL to the github repo
    download_url = 'https://github.com/phizaz/ssher/tarball/{}'.format(version), # I'll explain this in a second
    keywords = ['ssh'], # arbitrary keywords
    classifiers = [],
)