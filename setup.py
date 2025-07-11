from setuptools import setup

setup(
    name='my-telegram-miniapp',
    version='0.1.0',
    packages=['.'],  # Include all packages under the root
    install_requires=[
        'Flask==2.3.2',
    ],
)