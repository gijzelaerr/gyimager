from setuptools import setup, Extension, find_packages
from gyimager import __version__

extensions = [Extension(name='_casaimwrap',
                        sources=['src/casaimwrap/casaimwrap.cc',
                                 'src/casaimwrap/VisBufferStub.cc'],
                        include_dirs=['src'],
                        extra_compile_args=['-fopenmp'],
                        libraries=['casa_tables', 'casa_images',
                                   'casa_coordinates', 'casa_ms',
                                   'casa_msfits', 'boost_python-py27', 'casa_synthesis', 'boost_thread', 'fftw',
                                   'python2.7', 'awimager2lib'],
                        )
              ]


setup(
    name="gyimager",
    version=__version__,
    author="Gijs Molenaar",
    author_email="gijs@pythonic.nl",
    description=("gyimager"),
    license="GPL2",
    keywords="radio astronomy",
    url="http://github.com/radio-astro/pyimager",
    packages=find_packages(),
    ext_modules=extensions,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
    ],
    scripts=['gyimager/bin/gyimager']
)
