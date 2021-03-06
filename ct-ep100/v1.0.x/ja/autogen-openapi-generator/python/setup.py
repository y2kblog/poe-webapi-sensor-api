"""
    PoE対応 WebAPI CO2センサ API仕様

    \"Try it out\"機能は、API仕様を製品と同一ネットワーク上のローカルPCにダウンロードしブラウザで開くことで利用できます。   # noqa: E501

    The version of the OpenAPI document: 1.0.x
    Generated by: https://openapi-generator.tech
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "CT-EP100-python"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
  "urllib3 >= 1.25.3",
  "python-dateutil",
]

setup(
    name=NAME,
    version=VERSION,
    description="PoE対応 WebAPI CO2センサ API仕様",
    author="OpenAPI Generator community",
    author_email="team@openapitools.org",
    url="",
    keywords=["OpenAPI", "OpenAPI-Generator", "PoE対応 WebAPI CO2センサ API仕様"],
    python_requires=">=3.6",
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    license="MIT",
    long_description="""\
    \&quot;Try it out\&quot;機能は、API仕様を製品と同一ネットワーク上のローカルPCにダウンロードしブラウザで開くことで利用できます。   # noqa: E501
    """
)
