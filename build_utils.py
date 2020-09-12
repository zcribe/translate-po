import argparse
import os


def generate_docs():
    os.system("pdoc --html translate_po.main --force --output-dir ./docs")


def build_dist():
    os.system("python setup.py sdist")
    os.system("python setup.py bdist_wheel --universal")


def upload_to_pypi(live=False):
    with open('.env', "r") as file:
        if live:
            file.readline()
            token = file.readline()[6:]
        else:
            token = file.readline()[10:]
    if live:
        os.system(f"twine upload dist/* -u __token__ -p {token}")
    else:
        os.system(f"twine upload -r testpypi dist/* -u __token__ -p {token}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-live', type=bool, default=False)
    arguments = parser.parse_args()

    generate_docs()
    build_dist()
    upload_to_pypi(live=arguments.live)
