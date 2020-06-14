import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="kaggle_ieee_cis_fraud_detection",
    version="0.0.1",
    author="Dan Ringwald",
    author_email="dan.ringwald12@gmail.com@gmail.com",
    description="Working on kaggle ieee cis fraud detection challenge.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/biggoron/kaggle-ieee-cis-fraud-detection",
    packages=['kaggle_ieee_cis_fraud_detection'],
    scripts=['bin/hello_world', 'bin/setup_data'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
