import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="spotify-client-okjuan",
    version="0.0.1",
    author="okjuan",
    author_email="jcgallegdup@gmail.com",
    description="HTTP client for Spotify's Web API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/okjuan/spotify",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
