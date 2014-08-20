from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='binario',
      version='0.0.2',
      description='Package that lets an application read/write primitive data ' +
                  'types from an underlying input/output stream as binary data.',
      long_description=readme(),
      url='http://github.com/asaskevich/binario',
      keywords='io input output file binary binario data',
      author='Alex Saskevich',
      author_email='bwatas@gmail.com',
      license='MIT',
      packages=['binario'],
      zip_safe=False)