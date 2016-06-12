from setuptools import setup

setup(
    name = 'sssh',
    packages = ['sssh'],
    entry_points={
        "console_scripts": ['sssh = sssh.ssher:main']
    },
    version = '0.4',
    description = 'Stop remembering all the hosts when using SSH',
    author = 'Konpat Preechakul',
    author_email = 'the.akita.ta@gmail.com',
    url = 'https://github.com/phizaz/ssher', # use the URL to the github repo
    download_url = 'https://github.com/phizaz/ssher/tarball/0.4', # I'll explain this in a second
    keywords = ['ssh'], # arbitrary keywords
    classifiers = [],
)