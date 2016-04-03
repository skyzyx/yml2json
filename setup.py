import setuptools

long_description = ""
try:
    with open("'requirements.txt'") as f:
        requirements = [x for x in [y.strip() for y in f.readlines()] if x]
except IOError:
    requirements = []

setuptools.setup(
    name='yml2json',
    license='MIT',
    author='Ryan Parman',
    author_email='ryan@ryanparman.com',
    url="https://github.com/skyzyx/yaml2json",
    install_requires=requirements,
    version='1.1.0',
    packages=setuptools.find_packages(),
    description='Converts YAML input to JSON output.',
    long_description=long_description,
    entry_points={
        'console_scripts': [
            'yaml2json=yaml2json:main',
        ],
    },
)
