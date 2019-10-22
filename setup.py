# Always prefer setuptools over distutils
from setuptools import setup
from src.__init__ import __version__

with open('requirements.txt') as fp:
    reqs = fp.read()


setup(
    name='tufts_courses',
    author='',
    url='https://github.com/kedestin/CourseAPI',
    version=__version__,
    package_dir={'tufts_courses': 'src'},
    packages=['tufts_courses'],
    description="API to Query Tufts' Course Database",
    install_requires=reqs,
)
