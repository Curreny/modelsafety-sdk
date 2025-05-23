from setuptools import setup, find_packages

setup(
    name="modelsafety",
    version="0.1.2",
    description="ModelSafety SDK",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="ModelSafety Team",
    author_email="sun_jinzhou@126.com",
    url="https://github.com/Curreny/modelsafety-sdk",
    packages=find_packages(),
    install_requires=[
        "requests>=2.25.0",
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    keywords="ai, llm, safety, evaluation, audit",
    python_requires=">=3.7",
) 