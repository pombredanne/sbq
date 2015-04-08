from setuptools import setup
setup(
    name="sbq",
    packages=["sbq"],
    version="0.1.0",
    description="Low-dependency package for automating bigquery queries.",
    author="Colin Fuller",
    author_email="colin@khanacademy.org",
    url="github.com/cjfuller/sbq",
    keywords=["bigquery"],
    classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    requires=['requests']
)