from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize
import numpy

ext_modules = [
    Extension(
        "core",
        ["core.pyx"],
        extra_compile_args=['-O3'],
        extra_link_args=['-O3'],#, '-lgomp'],
    )
]

setup(
    ext_modules = cythonize(ext_modules),
    include_dirs = [numpy.get_include()]
)
