from setuptools import setup, Extension
from Cython.Build import cythonize

extensions = [
    Extension("gui_component", ["gui_component.py"]),
]

setup(
    name="GreetingCardApp",
    ext_modules=cythonize(extensions, compiler_directives={'language_level': "3"}),
)
