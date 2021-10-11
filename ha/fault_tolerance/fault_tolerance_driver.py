#!/usr/bin/env python3

# Copyright (c) 2021 Seagate Technology LLC and/or its Affiliates
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.
# For any questions about this software or licensing,
# please email opensource@seagate.com or cortx-questions@seagate.com.


import time

from cortx.utils.conf_store import Conf
from cortx.utils.log import Log

from ha import const
from ha.core.config.config_manager import ConfigManager
from ha.k8s_setup.const import _DELIM


class FaultToleranceDriver:
    """
    Driver class which will poll contineously with a specific
    time gap and analyzes the alert condition and it gets
    notified to event manager
    """
    def __init__(self, poll_time=10):
        ConfigManager.init('fault_tolerance_driver')
        self._poll_time = Conf.get(const.HA_GLOBAL_INDEX, f"prometheus_config{_DELIM}poll_time")
        if self._poll_time is None:
            self._poll_time = poll_time
        Log.info(f'poll time: {self._poll_time}')

    def poll(self):
        try:
            while True:
                # Get alert condition from ALertGenerator. Analyze changes
                # with the help of event manager and notify if required
                print('Ready to analyze faults in the system')
                Log.info('Ready to analyze faults in the system')

                time.sleep(self._poll_time)
        except Exception as exe:
            raise(f'Oops, some issue in the fault tolerance_driver: {exe}')

if __name__ == '__main__':
    fault_tolerance = FaultToleranceDriver()
    fault_tolerance.poll()