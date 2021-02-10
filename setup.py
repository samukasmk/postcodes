import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


def test_suite():
    import unittest
    test_loader = unittest.TestLoader()
    test_suite = test_loader.discover('tests', pattern='test_*.py')
    return test_suite


setuptools.setup(
    name="postcodes",
    version="0.0.1",
    author="Samuel Sampaio",
    author_email="samukasmk@gmail.com",
    license="Apache 2.0",
    description="Library to parse postal code format.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/samukasmk/postcodes",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    scripts=["scripts/postcodes"],
    install_requires=[],
    test_suite='setup.test_suite',
)
