# -*- coding: utf-8 -*-
# This file is part of pygal
#
# A python svg graph plotting library
# Copyright © 2012-2015 Kozea, Serge Droz
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
"""
US states map

"""

from __future__ import division
from pygal.graph.map import BaseMap
from pygal._compat import u
import os


STATES = {
    'AK': u('Alaska'),
    'AL': u('Alabama'),
    'AR': u('Arkansas'),
    'AZ': u('Arizona'),
    'CA': u('California'),
    'CO': u('Colorado'),
    'CT': u('Connecticut'),
    'DC': u('District of Columbia'),
    'DE': u('Delaware'),
    'FL': u('Florida'),
    'GA': u('Georgia'),
    'HI': u('Hawaii'),
    'IA': u('Iowa'),
    'ID': u('Idaho'),
    'IL': u('Illinois'),
    'IN': u('Indiana'),
    'KS': u('Kansas'),
    'KY': u('Kentucky'),
    'LA': u('Louisiana'),
    'MA': u('Massachusetts'),
    'MD': u('Maryland'),
    'ME': u('Maine'),
    'MI': u('Michigan'),
    'MN': u('Minnesota'),
    'MO': u('Missouri'),
    'MS': u('Mississippi'),
    'MT': u('Montana'),
    'NC': u('North Carolina'),
    'ND': u('North Dakota'),
    'NE': u('Nebraska'),
    'NH': u('New Hampshire'),
    'NJ': u('New Jersey'),
    'NM': u('New Mexico'),
    'NV': u('Nevada'),
    'NY': u('New York'),
    'OH': u('Ohio'),
    'OK': u('Oklahoma'),
    'OR': u('Oregon'),
    'PA': u('Pennsylvania'),
    'RI': u('Rhode Island'),
    'SC': u('South Carolina'),
    'SD': u('South Dakota'),
    'TN': u('Tennessee'),
    'TX': u('Texas'),
    'UT': u('Utah'),
    'VA': u('Virginia'),
    'VT': u('Vermont'),
    'WA': u('Washington'),
    'WI': u('Wisconsin'),
    'WV': u('West Virginia'),
    'WY': u('Wyoming)',
}


with open(os.path.join(
        os.path.dirname(__file__),
        'us.states.svg')) as file:
    CNT_MAP = file.read()


class Cantons(BaseMap):
    """US States map"""
    x_labels = list(STATES.keys())
    area_names = STATES
    area_prefix = 'z'
    kind = 'state'
    svg_map = CNT_MAP
