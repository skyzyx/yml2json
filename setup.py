import setuptools

def readme():
    with open('README.rst') as f:
        return f.read()

setuptools.setup(
    name='yml2json',
    license='MIT',
    author='Ryan Parman',
    author_email='ryan@ryanparman.com',
    url="https://github.com/skyzyx/yml2json",
    install_requires=['PyYAML==3.11'],
    version='1.0.1',
    packages=['yml2json'],
    description='Converts YAML input to JSON output.',
    long_description=readme(),
    keywords='yaml yml json',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7',
        'Topic :: Utilities',
    ],
    entry_points={
        'console_scripts': [
            'yml2json=yml2json:main',
        ],
    },
)
