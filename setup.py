"""Setup script."""
from setuptools import setup


setup(name="Nordic44",
      version="0.1",
      description="Python package for generating N44 cases",
      packages=["nordic44"],
      package_data={"nordic44": ["models/*sav"]},
      include_package_data=True,
      scripts=['bin/nordic44_script.py'],)
