import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="zcribe",  # Replace with your own username
    version="0.0.1",
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
    keywords='',
    project_urls={
        'Source': 'http://www.erlend.ee',
        'Documentation': 'http://www.erlend.ee',
        'Author': 'http://www.erlend.ee',
    },
)
