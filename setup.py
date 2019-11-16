from setuptools import find_packages, setup

# Package meta-data.
NAME = 'RePoE'
DESCRIPTION = 'Repository of Path of Exile resources for tool developers'
URL = 'https://github.com/brather1ng/RePoE'
EMAIL = ''
AUTHOR = 'brather1ng'
REQUIRES_PYTHON = '>=3.6.0'
VERSION = '1.0.0'

# What packages are required for this module to be executed?
REQUIRED = [
   'PyPoE'
]

# What packages are optional?
EXTRAS = {
    # 'fancy feature': ['django'],
}

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    py_modules=find_packages(),
    install_requires=REQUIRED,
    extras_require=EXTRAS,
    include_package_data=True,
    license='proprietary',
)