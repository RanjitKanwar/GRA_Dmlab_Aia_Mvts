"""
 * aia-mvts, a project at the Data Mining Lab
 * (http://dmlab.cs.gsu.edu/) of Georgia State University (http://www.gsu.edu/).
 *
 * Copyright (C) 2020 Georgia State University
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

from ConfigReader import ConfigReader
from ..datasources.harp_disk_source import HARPDiskSource

# Create a ConfigReader object and load the configuration
config_reader = ConfigReader()
config_reader.load_config('my_config_file.json')

# Retrieve the necessary parameters
base_dir = config_reader.get_value('base_dir')
output_dir = config_reader.get_value('output_dir')

# Create a HARPDiskSource object
harp_disk_source = HARPDiskSource(base_dir)

# Get the list of harp numbers
harp_nums = harp_disk_source.get_harp_nums()

# Cycle through the harps and save the relevant info to files
for harp_num in harp_nums:
    harp_info = harp_disk_source.get_harp_info(harp_num)
    output_file = f'{output_dir}/{harp_num}.json'
    with open(output_file, 'w') as f:
        json.dump(harp_info, f)
