import os
from setuptools import setup

path = os.path.dirname(__file__)
long_desc_fd = os.path.join(path, 'README.md')

long_description = ''

with open(long_desc_fd) as f:
    long_description = f.read()

setup(
    name='twitch-clip-compiler',
    version='0.0.1',
    packages=['twitch-clip-compiler'],
    url='https://github.com/benjaminhubbell/twitch-clip-compiler',
    license='MIT',
    author='Benjamin Hubbell',
    author_email='benjamin.d.hubbell@gmail.com',
    description='An application to generate a compilation video of top twitch clips of streamers of your choosing.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords=['TWITCH', 'CLIP', 'CLIPS', 'COMPILER'],
    download_url='https://github.com/sillyfatcat/twitch-clip-compiler/archive/v0.1.tar.gz',
    install_requires=[
    ],
    include_package_data=True,
    entry_points={
        'console_scripts': []
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Intended Audience :: Developers',
        'Topic :: Games/Entertainment',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)