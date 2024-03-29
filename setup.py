import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="plottymcplotface",
    version="0.0.0",
    author="Geoff Williams",
    author_email="None",
    description="I'll add this later...",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/GeoffWilliams/plottymcplotface.git",
    packages=setuptools.find_packages(),
    # pick from https://pypi.org/classifiers/
    classifiers=[
        "Development Status :: 1 - Planning",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    entry_points={
        "console_scripts": (['plottymcplotface=plottymcplotface.cli:main'],)
    },
    include_package_data=True,
    install_requires=[]
)
