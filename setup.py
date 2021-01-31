import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="path4gmns", 
    version="0.3.2",
    author="Dr. Xuesong Zhou, Dr. Peiheng Li",
    author_email="xzhou74@asu.edu, jdlph@hotmail.com",
    description="dev",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jdlph/PATH4GMNS",
    packages=['path4gmns'],
    package_dir={'path4gmns': 'path4gmns'},
    package_data={'path4gmns': ['bin/*']},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3.0",
        "Operating System :: OS Independent",
    ],
)
