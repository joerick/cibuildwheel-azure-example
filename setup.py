from setuptools import setup, Extension

setup(
    name="cibuildwheel_azure_pipelines_example",
    ext_modules=[Extension('cibuildwheel_azure_pipelines_example', sources=['cibuildwheel_azure_pipelines_example.c'])],
    version="0.1.17",
)
