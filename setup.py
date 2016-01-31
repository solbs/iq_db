from setuptools import setup, find_packages


setup(
    name="IQ_Builder",
    include_package_data=True,
    version="0.0.1",
    packages=find_packages(),
    description="database IQ levels",
    author="Shawn Solberg",
    author_email="shawnyboy02@hotmail.com",
    requires=['nose', 'flask', 'sqlalchemy']
)
