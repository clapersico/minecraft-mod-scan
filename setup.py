"""Setup configuration for Minecraft Mod Scanner."""

from setuptools import setup, find_packages
from pathlib import Path

# Read README for long description
readme_path = Path(__file__).parent / "README.md"
long_description = readme_path.read_text(encoding="utf-8") if readme_path.exists() else ""

setup(
    name="minecraft-mod-scanner",
    version="0.1.0-dev",
    author="clapersico",
    description="Minecraft mod scan, check version & licenses",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/clapersico/minecraft-mod-scan",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: End Users/Desktop",
        "Topic :: Games/Entertainment",
        "Topic :: System :: Systems Administration",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        # Core dependencies will be added as they are needed
    ],
    extras_require={
        "dev": [
            "pytest>=6.2.0",
            "pytest-cov>=2.11.0",
            "black>=21.0.0",
            "flake8>=3.8.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "minecraft-mod-scan=main:main",
        ],
    },
    keywords="minecraft mods scanner version license",
    project_urls={
        "Bug Reports": "https://github.com/clapersico/minecraft-mod-scan/issues",
        "Source": "https://github.com/clapersico/minecraft-mod-scan",
    },
)