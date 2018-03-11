import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='bedubs-veepian',
    version='0.0.1',
    packages=find_packages(),
    include_package_data=True,
    license='BSD License',
    description='A Django app to provide VPN services to frontend clients.',
    long_description=README,
    url='http://bedubs.com',
    author='Billy Williamson',
    author_email='billy@bedubs.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 2.0',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
    ],
)
