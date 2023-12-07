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

import os
import logging
import logging.handlers
import configparser


class ConfigReader:

    def __init__(self, conf_file_path: str, conf_file_name: str):
        config = configparser.ConfigParser()
        conf_file = conf_file_path + os.path.sep + conf_file_name
        config.read(conf_file)

        self._logger = self.__create_logger(config)

        self._jsoc_email = config['JSOC']['notify_email']
        self._lib_dir = config['RUNTIME']['lib_path']
        self._lib_name = config['RUNTIME']['lib_name']
        self._batch_size = int(config['RUNTIME']['batch_size'])
        self._cadence_hours = float(config['RUNTIME']['cadence_hours'])
        self._api_host_address = 'http://{0}:{1}/'.format(config['RESTFULAPI']['host'], config['RESTFULAPI']['port'])
        self._user_name = config['RESTFULAPI']['user']
        self._password = config['RESTFULAPI']['password']

    @staticmethod
    def __create_logger(config):
        log_dir = config['LOGGING']['log_path']
        log_file = config['LOGGING']['log_file']
        log_file_size = int(config['LOGGING']['log_file_size_bytes'])
        log_file_backups = int(config['LOGGING']['log_backups'])
        log_level = config['LOGGING']['level']

        if log_level == "DEBUG":
            log_level = logging.DEBUG
        elif log_level == "INFO":
            log_level = logging.INFO
        else:
            log_level = logging.CRITICAL

        formatter = logging.Formatter('%(name)s - %(asctime)s - %(levelname)s - %(message)s')
        logger = logging.getLogger("SHARP_NRT")
        logger.setLevel(level=log_level)

        log_file = os.path.realpath(os.path.join(log_dir, log_file))
        handler = logging.handlers.RotatingFileHandler(log_file, maxBytes=log_file_size, backupCount=log_file_backups)
        handler.setLevel(level=log_level)
        handler.setFormatter(formatter)

        logger.addHandler(handler)

        return logger

    def get_api_address(self):
        return self._api_host_address

    def get_api_user(self):
        return self._user_name

    def get_api_password(self):
        return self._password

    def get_notification_email(self):
        return self._jsoc_email

    def get_logger(self):
        return self._logger

    def get_lib_dir(self):
        return self._lib_dir

    def get_lib_name(self):
        return self._lib_name

    def get_cadence(self):
        return self._cadence_hours

    def get_batch_size(self):
        return self._batch_size
