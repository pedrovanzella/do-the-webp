import setuptools

setuptools.setup(
    name="do_the_webp",
    version="0.2.1",
    url="https://github.com/pedrovanzella/do-the-webp",

    author="Pedro Vanzella",
    author_email="pedro@pedrovanzella.com",

    description="Converts cbz/cbr comic files to webp",
    long_description=open('README.rst').read(),

    packages=setuptools.find_packages(),

    install_requires=[],

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.7',
    ],
)
