"""
 * AIA-MVTS, a project at the Data Mining Lab
 * (http://dmlab.cs.gsu.edu/) of Georgia State University (http://www.gsu.edu/).
 *
 * Copyright (C) 2023 Georgia State University
 *
 * This program is free software: you can redistribute it and/or modify it under
 * the terms of the GNU General Public License as published by the Free Software
 * Foundation version 3.
 *
 * This program is distributed in the hope that it will be useful, but WITHOUT
 * ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
 * FOR A PARTICULAR PURPOSE. See the GNU General Public License for more
 * details.
 *
 * You should have received a copy of the GNU General Public License along with
 * this program. If not, see <http://www.gnu.org/licenses/>.
"""
from typing import List, Dict


class HARPDiskSource:

    def __init__(self, base_dir):
        self._base_dir = base_dir


    def get_harp_nums(self)->List[int]:
        print('return the list of harp numbers from the base directory')



    def get_harp_info(self, harp_number:int)->List[Dict]:
        print('return a list of the time stamps and the associated information for said time stamp')
