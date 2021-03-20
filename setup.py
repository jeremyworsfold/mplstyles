from setuptools import setup

setup(name='mplstyles',
      version='0.0.1',
      description='Custom matplotlib styles for various uses',
      author='Jeremy Worsfold',
      author_email='jw3286@bath.ac.uk',
      packages=['mplstyles'],
      install_requires=['matplotlib'],
      package_data ={
          '':['notebook.mplstyle','website.mplstyle','paper.mplstyle','presentation.mplstyle']
          },
      include_package_data=True,
      zip_safe=False)