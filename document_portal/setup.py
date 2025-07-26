from setuptools import setup, find_packages
setup(
    name="document_portal",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "fastapi",
        "uvicorn",
        "python-dotenv",
    ],
)

