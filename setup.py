import pathlib
from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

setup(
    name='the_trivia_api_library',
    version='0.0.5',
    description='A Python library for The Trivia API',
    long_description=README,
    long_description_content_type="text/markdown",
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
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13'
    ],
    test_suite='tests'
)



