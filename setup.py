from setuptools import setup, find_packages

setup(
    name='guessing_game',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'guessing_game=guessing_game:GuessingGame.main',
        ],
    },
    extras_require={
        "dev": [
            "pytest>=3.7",
        ],
    },
)
