from setuptools import setup, find_packages

setup(
    name="cdo-mcp",
    version="0.1.0",
    description="Local MCP server for Cisco Defense Orchestrator API",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Your Name",
    author_email="your.email@example.com",
    url="https://github.com/your-username/cdo-mcp",
    packages=find_packages(),
    install_requires=[
        "requests>=2.28.0",
        "pydantic>=2.0.0",
        "python-dotenv>=0.21.0",
    ],
    python_requires=">=3.8",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
