from setuptools import setup, find_packages

<<<<<<< HEAD
from dreammud import meta
=======
from dreamssh import meta
from dreamssh.util import dist
>>>>>>> 4149a93215343dbae0b7eb8062a76a88146a5e4f


setup(
    name=meta.display_name,
    version=meta.version,
    description=meta.description,
<<<<<<< HEAD
=======
    long_description=meta.long_description,
>>>>>>> 4149a93215343dbae0b7eb8062a76a88146a5e4f
    author=meta.author,
    author_email=meta.author_email,
    url=meta.url,
    license=meta.license,
<<<<<<< HEAD
    packages=find_packages(),
    long_description=meta.long_description,
    install_requires=meta.requires
    )
=======
    packages=find_packages() + ["twisted.plugins"],
    package_data={
        "twisted": ['plugins/dreamssh.py']
        },
    install_requires=meta.requires,
    zip_safe=False
    )


dist.refresh_plugin_cache()
>>>>>>> 4149a93215343dbae0b7eb8062a76a88146a5e4f
