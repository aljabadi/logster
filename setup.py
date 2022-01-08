from setuptools import setup

setup(
    name="logster",
    version="0.9.0",
    description="Easy python console logging with colourful formatting",
    long_description=(
        "logster is the one-liner console logging solution for development environments."
        + "See example usage at\n"
        + "https://github.com/aljabadi/logster/blob/master/README.md"
        + "\nThis is a development project. Feedback/enhancements are welcome."
    ),
    url="https://github.com/aljabadi/logster",
    download_url="https://github.com/aljabadi/logster/archive/refs/tags/v0.9.0.tar.gz",
    author="Al J Abadi",
    author_email="al.jal.abadi@gmail.com",
    license="MIT",
    packages=["logster"],
    python_requires=">=3.5",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    zip_safe=False,
)
