from setuptools import setup, find_packages

setup(
    name='Django Eventbrite',
    version='0.0.6',
    author='Caktus Consulting Group',
    author_email='solutions@caktusgroup.com',
    packages=find_packages(),
    install_requires=[
        'simplejson',
        'httplib2',
    ],
    include_package_data=True,
    exclude_package_data={
        '': ['*.sql', '*.pyc'],
    },
    url='http://bitbucket.org/copelco/django-eventbrite',
    license='LICENSE.txt',
    description='Basic Eventbrite integration with Django.',
    long_description=open('README.rst').read(),
)
