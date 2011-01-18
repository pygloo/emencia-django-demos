# setuptools import
from setuptools import setup, find_packages

VERSION = '0.1'

setup(name='emencia-django-demos',
      version=VERSION,
      description='Simple django demo app for emencia.',
      long_description='Simple django demo app for emencia.',
      author='florent.pigout@gmail.com',
      author_email='florent.pigout@gmail.com',
      url='',
      license='MIT',
      install_requires=[
          'pysqlite',
          # 'pil'
          'django',
          'django-blog-zinnia',
          'geopy',
          'django-reploc',
          'django_gmapsfield',
          ],
      packages=find_packages(),
      package_data={},
      include_package_data=True,
      zip_safe=False,
      classifiers=[
          'Framework :: Django',
          'Development Status :: 5 - Production/Stable',
          'Environment :: Web Environment',
          'Programming Language :: Python',
          'Intended Audience :: Developers',
          'Operating System :: OS Independent',
          'License :: OSI Approved :: BSD License',
          'Topic :: Software Development :: Libraries :: Python Modules',
          ],
 )

