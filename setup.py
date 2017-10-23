from setuptools import find_packages, setup


setup(
    name='remote-config-lqn',
    description='This Module get the config for LQN.',
    author='Cristian Duque',
    author_email='cristian@loquenecesito.com',
    license='UNLICENSE',
    keywords='lqn',
    packages=find_packages(exclude=['docs', 'tests*']),
    install_requires=[
        'boto3',
    ],
    extras_require={
        'test': ['unittest'],
    }
)