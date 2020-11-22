from setuptools import setup, find_packages
setup(
    name = 'mixr',
    description = 'Generate an MP3 mix from the command line',
    url = 'https://github.com/soulprovidr/mixr',
    packages = find_packages(),
    entry_points ={ 
        'console_scripts': [ 
            'mixr = mixr.mixr:main'
        ] 
    }, 
    version = '2.0.0',
    author = 'Shola Anozie',
    author_email = 'shola@soulprovidr.fm',
    install_requires = ['pydub']
)