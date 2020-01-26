import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'README.rst')) as f:
    README = f.read()

with open(os.path.join(here, 'CHANGES.txt')) as f:
    CHANGES = f.read()

requires = ['pyramid>=1.7',  'simplejson', 'six', 'venusian']

entry_points = ""
package_data = {}


def get_version(pkg_name):
    """
    Reads the version string from the package __init__ and returns it

    This make version management a build-time action, rather than a
    run-time action, which is what pkg_resources does.
    """
    with open(os.path.join(pkg_name, "__init__.py")) as init_file:
        for line in init_file:
            parts = line.strip().partition("=")
            if parts[0].strip() == "__version__":
                return parts[2].strip().strip("'").strip('"')
    return None


setup(name='cornice',
      version=get_version('cornice'),
      description='Define Web Services in Pyramid.',
      long_description=README + '\n\n' + CHANGES,
      license='MPLv2.0',
      classifiers=[
          "Programming Language :: Python",
          "Programming Language :: Python :: 2.6",
          "Programming Language :: Python :: 2.7",
          "Programming Language :: Python :: 3",
          "Programming Language :: Python :: 3.5",
          "Programming Language :: Python :: 3.6",
          "Programming Language :: Python :: 3.7",
          "Framework :: Pylons",
          "Topic :: Internet :: WWW/HTTP",
          "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
          "License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)", ],
      entry_points=entry_points,
      author='Mozilla Services',
      author_email='services-dev@mozilla.org',
      url='https://github.com/mozilla-services/cornice',
      keywords='web pyramid pylons',
      packages=find_packages(exclude=("tests",)),
      package_data=package_data,
      include_package_data=True,
      zip_safe=False,
      install_requires=requires)
