from setuptools import setup, find_packages

setup(
	name = "yyjscanner",
	version = "0.1",
	packages = find_packages(),
	entry_points = {"console_scripts": [
            "yyjscanner = yyjscanner.scanner:main",
        ]}
)