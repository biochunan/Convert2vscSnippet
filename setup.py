from setuptools import setup, find_packages

setup(
    name='convert2snippet',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'convert2snippet=convert2snippet.app:main'
        ]
    },
    # Add other necessary information
    author='Chu\'nan Liu',
    author_email='chunan.liu@ucl.ac.uk',
    description='A tool to convert text to a vscode snippet',
    url='https://github.com/biochunan/Convert2vscSnippet',
)
