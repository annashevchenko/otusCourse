from setuptools import setup, find_packages

setup(name='otus-qa',
      version='0.1',
      url='https://github.com/annashevchenko/otusCourse',
      license='MIT',
      author='Shevchenko S Anna ',
      author_email='shevchenko.anna.s@gmail.com',
      description='Otus qa homework',
      packages=find_packages(exclude=['tests']),
      long_description=open('README.md').read(),
      setup_requires=['pytest>=4.6.0'],
      zip_safe=False)
