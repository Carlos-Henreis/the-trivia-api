from setuptools import setup, find_packages

setup(
    name='the_trivia_api_library',
    version='0.0.1',
    description='A Python library for The Trivia API',
    author='Carlos Henrique Reis',
    author_email='cahenre@gmail.com',
    url='https://github.com/Carlos-Henreis/the-trivia-api',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    tests_require=[
        'pytest',
        'pytest-cov'
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    test_suite='tests'
)



