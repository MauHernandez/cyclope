# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
from setuptools.dist import Distribution

setup(
    name='django-cyclope',
    version=__import__('cyclope').__version__,
    description="CMS for pythonistas who like to code instead of using a web UI for every task.",
    long_description=__import__('cyclope').__doc__,
    author='Nicolás Echániz & Santiago Hoerth',
    author_email='nicoechaniz@codigosur.org',
    url='http://bitbucket.org/nicoechaniz/django-cyclope/',
    license='GPL v3',
    platforms=['OS Independent'],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: GPL v3",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
    ],

    # revision number is indicated in the dependency_links for packages
    # that are downloaded from source to ensure a tested revision is used.
    dependency_links=[
        'git+http://github.com/matthiask/feincms.git#egg=feincms-dev',
        'git+http://github.com/matthiask/django-mptt.git#egg=django-mptt-3.0-pre',
        'hg+http://bitbucket.org/ubernostrum/django-registration#egg=django-registration-dev',
        'git+http://github.com/alexvasi/django-filebrowser-no-grappelli-and-uploadify.git#egg=django-filebrowser-dev',
        'hg+http://bitbucket.org/diegom/django-contact-form#egg=django-contact-form-dev',
    ],

    install_requires=[
        'Django>=1.2',
        'FeinCms>=1.0.99,==dev',
        'django-autoslug>=1.4.1',
        'django-mptt>=0.3-pre,==dev',
        'PIL>=1.1.7',
        'django-simple-captcha>=0.1.7',
        'django-tagging>=0.3.1',
        'django-tagging-autocomplete>=0.3.1',
        'django-filebrowser>=3.0,==dev',
        'South>=0.7.1',
        'django-registration>=0.8-alpha-1,==dev',
        'django-profiles>=0.2',
        'django-admin-tools>=0.3.0',
        'django-contact-form>=0.4a1',
    ],

    packages=find_packages(),

    include_package_data=True,
    zip_safe=False,
)
