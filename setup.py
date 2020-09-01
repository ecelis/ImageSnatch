import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="image_snatch-pkg-ecelis",
    version="0.0.1",
    author="Ernesto Celis",
    author_email="ernesto@celisdelafuente.net",
    description="Extract images from PDF files",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ecelis/ImageSnatch",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Affero General Public License version 3",
        "Operating System :: Linux/Unix",
    ],
    python_requires='>=3.6',
)
