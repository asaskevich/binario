from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()


setup(name='binario',
      version='0.0.3',
      description='Package that lets an application read/write primitive data ' +
                  'types from an underlying input/output stream as binary data.',
      long_description=readme(),
      url='http://github.com/asaskevich/binario',
      keywords='io input output file binary binario data',
      author='Alex Saskevich',
      author_email='bwatas@gmail.com',
      license='MIT',
      packages=['binario'],
      test_suite='nose.collector',
      tests_require=['nose'],
      download_url="https://pypi.python.org/pypi/binario",
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.0',
          'Programming Language :: Python :: 3.1',
          'Programming Language :: Python :: 3.2',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Topic :: Software Development :: Libraries',
          'Topic :: Software Development :: Libraries :: Python Modules',
          'Topic :: System',
          'Topic :: System :: Filesystems',
          'Topic :: Utilities',
      ],
      zip_safe=False)