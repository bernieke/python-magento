try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

packages = ['magento']
requires = []

setup(
    name='python-magento',
    version='0.2.5',
    author='Vikram Oberoi',
    author_email='voberoi@gmail.com',
    packages=['magento'],
    install_requires=requires,
    entry_points={
        'console_scripts': [
            'magento-ipython-shell = magento.magento_ipython_shell:main'
        ]
    },
    url='https://github.com/voberoi/python-magento',
    license="MIT License",
    description='A Python wrapper to Magento\'s XML-RPC API.',
    long_description=open('README.rst').read(),
    classifiers=(
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',        
    )
)
