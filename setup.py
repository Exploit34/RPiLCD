from setuptools import setup

readme = open("README.rst").read()

setup (
    name="RPiLCD",
    version="0.1.0",
    description="Librería para controlar LCD en Raspberry Pi",
    long_description=readme,
    long_description_content_type="text/x-rst",
    author="Esteban",
    author_email="herrerazanecheverry@gmail.com",
    license="LGPLv3",
    url = "https://github.com/Exploit34/RPiLCD",
    keywords='raspberry, raspberry pi, lcd, liquid crystal, rpi, i2c, displayScreen',
    packages=["RPiLCD"]
)
