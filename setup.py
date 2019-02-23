from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="7i96",
    version="0.0.1",
    author="John Thornton",
    author_email="<jt@gnipsel.com>",
    description="Mesa configuration tool for 7i96",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jethornton/7i96",
    download_url="https://github.com/jethornton/mct7i96/tarball/master",
    python_requires='>=3',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
    python3-pyqt5,
    libpci-dev
    ]
    entry_points={
        'gui_scripts': ['7i96=main.7i96:main',],
    },
)

