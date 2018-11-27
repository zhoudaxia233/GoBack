import os
import sys
import io
import re
import goback
from setuptools import setup


# "setup.py publish" shortcut.
if sys.argv[-1] == 'publish':
    os.system('python3 setup.py sdist')
    os.system('twine upload dist/*')
    os.system('rm -rf dist goback.egg-info')
    sys.exit()

setup(
    name='goback',
    version=goback.__version__,
    description="It helps you to navigate to the first few commits of a project on GitHub.",
    keywords='github-helper',
    author='Zheng Zhou',
    author_email='yootaoo@gmail.com',
    url='https://github.com/zhoudaxia233/GoBack',
    license='MIT',
    packages=['goback'],
    include_package_data=True,
    zip_safe=False,
    install_requires=['requests', 'lxml'],
    dependency_links=[],
    entry_points={
        'console_scripts': [
          'goback=goback.main:main',
      ]
    }

)
