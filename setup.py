try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

from gpiomock import __version__

with open("README.md") as f:
    ldesc = f.read()

config = {
    'name': 'gpiomock',
    'author': 'Bartlomiej Osinski',
    'author_email': 'osinskibartlomiej@gmail.com',
    'version': __version__,
    'py_modules': ['gpiomock'],
    'license': 'MIT',
    'install_requires': [
    ],
    'extras_require': {
    },
    'description': "gpio access via the standard linux sysfs interface",
    'long_description': ldesc,
    'url': "https://github.com/cloudformdesign/gpio",
    'classifiers': [
        # 'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Embedded Systems',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
}

setup(**config)
