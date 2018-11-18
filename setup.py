import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='questrade-api',
    version='1.0.0',
    description='Questrade API Wrapper',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/tgardiner/questrade_api',
    author='Tom Gardiner',
    author_email='tom@teppen.io',
    license='MIT',
    packages=setuptools.find_packages(),
    package_data={
        'questrade_api': ['questrade.cfg'],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
