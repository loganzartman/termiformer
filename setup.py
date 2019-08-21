import setuptools

requirements = []
with open("requirements.txt", "r") as f:
    requirements += f.readlines()

setuptools.setup(
    name="termiformer",
    version="0.0.1",
    author="Logan Zartman",
    author_email="logan.zartman@utexas.edu",
    description="Create interactive input forms in the terminal",
    url="https://github.com/loganzartman/termiformer",
    packages=setuptools.find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
