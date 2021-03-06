"""
This file installs linien.client as well as linien.gui.
It assumes that all dependencies were already installed.
"""
import setuptools

import linien
assert linien.__version__ != 'dev'

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name="linien",
    version=linien.__version__,
    author="Benjamin Wiegand",
    author_email="highwaychile@posteo.de",
    description="Spectroscopy lock application using RedPitaya",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hermitdemschoenenleben/linien",
    packages=['linien', 'linien.gui', 'linien.gui.ui', 'linien.client'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    entry_points={
        'console_scripts': [
            'linien=linien.gui.app:run_application'
        ]
    },
    # all requirements were already installed
    install_requires=[],
    package_data={
        # IMPORTANT: any changes have to be made in client.spec, too
        # (for the standalone installer)
        # IMPORTANT: any changes have to be made in setup_client_and_gui.py
        # of flathub repo as well
        '': ['*.ui', 'VERSION', '*.ico']
    }
)