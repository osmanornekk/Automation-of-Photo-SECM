from setuptools import setup, find_packages

setup(
name="TabbedMeasurementApp",
version="0.1.0",
author="Osman",
description="A PyQt5 application combining AFM, CV, and CA GUIs in a tabbed interface",
py_modules=["main", "gui_main", "CVp2p", "CAp2p", "lnet_main"],
install_requires=[
"PyQt5>=5.15,<6.0",
"matplotlib>=3.6",
"numpy>=1.24",
],
# If you'd like an entry-point, ensure 'main' defines a main() function:
# entry_points={
#     "console_scripts": [
#         "main-app=main:main",
#     ],
# },
# Alternatively, install the script directly:
scripts=["main.py"],
python_requires=">=3.7",
classifiers=[
"Programming Language :: Python :: 3",
"License :: OSI Approved :: MIT License",
"Operating System :: OS Independent",
],
)