#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This file is part of pygal
#
# A python svg graph plotting library
# Copyright © 2012-2014 Kozea
#
# This library is free software: you can redistribute it and/or modify it under
# the terms of the GNU Lesser General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option) any
# later version.
#
# This library is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more
# details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with pygal. If not, see <http://www.gnu.org/licenses/>.


from setuptools import setup, find_packages


setup(
    name="pygal_maps_usa",
    version='1.0.0',
    description="US state map for pygal",
    author="Serge droz",
    url="http://pygal.org/",
    author_email="serge.droz@switch.ch",
    license="GNU LGPL v3+",
    platforms="Any",
    packages=find_packages(),
    provides=['pygal_maps_usa'],
    keywords=[
        "svg", "chart", "graph", "maps", "usa"],
    package_data={'pygal_maps_usa': ['*.svg']},
    install_requires=["pygal>=1.9.9"],

    entry_points={
        'pygal.maps': [
            'usa = pygal_maps_usa.maps',
        ],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: "
        "GNU Lesser General Public License v3 or later (LGPLv3+)",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Topic :: Multimedia :: Graphics :: Presentation"])
