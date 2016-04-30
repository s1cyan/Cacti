import os
from setuptools import setup, find_packages

from friendship import VERSION


f = open(os.path.join(os.path.dirname(__file__), 'README.rst'))
readme = f.read()
f.close()

setup(
    name='django-django_friendship',
    version=".".join(map(str, VERSION)),
    description='django-django_friendship provides an easy extensible interface for following and django_friendship',
    long_description=readme,
    author='Frank Wiles',
    author_email='frank@revsys.com',
    url='https://github.com/revsys/django-django_friendship/',
    include_package_data=True,
    packages=find_packages(),
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Framework :: Django',
    ],
    test_suite='django_friendship.tests.runtests.runtests'
)
