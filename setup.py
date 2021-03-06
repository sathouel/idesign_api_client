import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="idesign-api-client",
    version="0.0.5",
    author="Steven Athouel",
    author_email="sathouel@gmail.com",
    description="A simple api client for Idesign Clients and Suppliers",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sathouel/idesign_api_client",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)