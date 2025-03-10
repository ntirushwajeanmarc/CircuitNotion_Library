from setuptools import setup, find_packages

setup(
    name="CircuitNotionAI",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "requests>=2.25.0",
    ],
    author="Ntirushwajean Marc",
    author_email="ntirushwajeanmarc@gmail.com",
    description="A Python client for the CircuitNotion AI API",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/ntirushwajeanmarc/CircuitNotion_Library",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
