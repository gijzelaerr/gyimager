from setuptools import setup, Extension
from gyimager import __version__


extensions = [Extension(name='_casaimwrap',
                        sources=['src/casaimwrap/casaimwrap.cc',
                                 'src/casaimwrap/VisBufferStub.cc'],
                        include_dirs=['src'])]



setup(
    name="pyimager",
    version=__version__,
    author="Gijs Molenaar",
    author_email="gijs@pythonic.nl",
    description=("pyimager"),
    license="GPL2",
    keywords="radio astronomy",
    url="http://github.com/radio-astro/pyimager",
    packages=['gyimager'],
    ext_modules=extensions,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
    ],
    scripts=['gyimager/bin/gyimager']
)