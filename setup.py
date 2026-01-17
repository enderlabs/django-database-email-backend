from setuptools import setup, find_packages
version = __import__('database_email_backend').__version__

setup(
    name = "django-database-email-backend",
    version = version,
    url = 'http://github.com/enderlabs/django-database-email-backend',
    license = 'BSD',
    platforms=['OS Independent'],
    description = "A django EmailBackend for debugging that saves Emails in the database instead of delivering them.",
    long_description = open('README.rst').read(),
    author = 'Stefan Foulis',
    author_email = 'stefan.foulis@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    python_requires='>=3.10',
    install_requires=[
        'Django>=5.2.10',
    ],
    classifiers = [
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Framework :: Django :: 5.2',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Topic :: Internet :: WWW/HTTP',
    ]
)
