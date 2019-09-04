from setuptools import setup, find_packages
setup(
    name = 'mixr',
    description = 'CLI tool to concatenate a series of .mp3 files into a mix.',
    url = 'https://github.com/soulprovidr/mixr',
    packages = find_packages(),
    entry_points ={ 
        'console_scripts': [ 
            'mixr = mixr.mixr:main'
        ] 
    }, 
    version = '1.0',
    author = 'Shola Anozie',
    author_email = 'shola@soulprovidr.fm',
    install_requires = ['pydub']
)