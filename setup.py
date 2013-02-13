try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='python-magento',
    version='0.1.0',
    author='Vikram Oberoi',
    author_email='voberoi@gmail.com',
    packages=['magento'],
    url='http://pypi.python.org/pypi/python-magento/',
    license='LICENSE.txt',
    description='A Python wrapper to Magento\'s XML-RPC API.',
    long_description=open('README.txt').read(),
)
