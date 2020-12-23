from setuptools import setup

setup(
  name='kanban',
  version='1.0.0',
  install_requires=[
    'django',
    'django-environ',
    'django-debug-toolbar',
  ],
  python_requires='>=3.6',
)
