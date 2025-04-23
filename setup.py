from setuptools import setup, find_packages

setup(
    name="efb-keyword-replace",
    packages=find_packages(),
    version="0.1.0",
    description="keyword replace",
    author="jiz4oh",
    author_email="me@jiz4oh.com",
    url="https://github.com/jiz4oh/efb-keyword-replace.git",
    include_package_data=True,
    install_requires=[
        "ehforwarderbot>=2.0.0",
        "PyYaml",
    ],
    entry_points={
        "ehforwarderbot.middleware": "jiz4oh.keyword_replace=efb_keyword_replace:KeywordReplaceMiddleware",
    },
)
