#!/usr/bin/env python


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
    name='python-magento',
    version='1.0.3',
    author='Vikram Oberoi',
    author_email='voberoi@gmail.com',
    maintainer='Bernard Kerckenaere',
    maintainer_email='bernieke@bernieke.com',
    packages=['magento'],
    install_requires=[],
    extras_require={
        'interactive_shell': ['ipython'],
    },
    entry_points={
        'console_scripts': [
            'magento-ipython-shell = '
            'magento.magento_ipython_shell:main [interactive_shell]',
        ],
    },
    url='https://github.com/bernieke/python-magento',
    license='MIT License',
    description='A Python wrapper to the Magento XML-RPC API.',
    long_description=open('README.rst').read(),
    classifiers=(
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    )
)
