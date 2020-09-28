import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="translate-po",  # Replace with your own username
    version="1.0.7",
    author="Erlend Eelmets",
    author_email="erlend.eelmets@gmail.com",
    description="Automatic PO file translator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/zcribe/translate-po",
    packages=setuptools.find_packages(exclude=['docs', 'tests', 'translated', 'untranslated']),
    package_data={'', ['LICENSE']},
    include_package_data=True,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Internationalization',
    ],
    python_requires='>=3.6',
    keywords='po translate automatic google',
    project_urls={
        'Source': 'https://github.com/zcribe/translate-po',
        'Documentation': 'https://github.com/zcribe/translate-po/docs/main.html',
        'Author': 'http://www.erlend.ee',
    },
    entry_points={
        'console_scripts': [
            'sample=sample:main',
        ],
    },
    install_requires=[
        'polib>=1.1.0',
        'googletrans>=3.0.0'
    ],
    setup_requires=[
        'polib>=1.1.0',
        'googletrans>=3.0.0'
    ],
)
