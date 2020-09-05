import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="translatePO",  # Replace with your own username
    version="1.0.0dev1",
    author="Erlend Eelmets",
    author_email="erlend.eelmets@gmail.com",
    description="Automatic PO file translator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    keywords='po translate automatic google',
    project_urls={
        'Source': 'http://www.erlend.ee',
        'Documentation': 'http://www.erlend.ee',
        'Author': 'http://www.erlend.ee',
    },
)
