from setuptools import setup

setup(
  name='kanban',
  version='1.0.0',
  install_requires=[
    'django>=3.1',
    'djangorestframework>=3.9',
    'django-debug-toolbar',
    'django-environ',
    'djoser>=2.1.0',
  ],
  python_requires='>=3.6',
)
