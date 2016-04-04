import setuptools

setuptools.setup(
    name='yml2json',
    license='MIT',
    author='Ryan Parman',
    author_email='ryan@ryanparman.com',
    url="https://github.com/skyzyx/yml2json",
    install_requires=['argparse', 'yaml'],
    version='1.0.0',
    packages=['yml2json'],
    description='Converts YAML input to JSON output.',
    long_description="",
    license='MIT',
    keywords='yaml yml json',
    classifiers=[
        'Development Status :: 4 - Beta'
        'Environment :: Console'
        'Intended Audience :: Developers'
        'License :: OSI Approved :: MIT License'
        'Natural Language :: English'
        'Programming Language :: Python :: 2.7'
        'Topic :: Utilities'
    ],
    entry_points={
        'console_scripts': [
            'yml2json=yml2json:main',
        ],
    },
)
