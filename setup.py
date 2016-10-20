from setuptools import setup


setup(name="Nordic44",
        version="0.1",
        description="Python package for generating N44 cases",
        packages=["nordic44", "examples"],
        package_data={"nordic44": ["models/*sav"],
            "examples": ["N44_20150101/*xlsx"]},
        include_package_data=True,
        )

