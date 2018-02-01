# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 12:25:49 2017

@author: RAVITHEJA
"""

import os


argument_config = {
    'daily_cron_time_utc': os.getenv('DAILY_CRON_TIME_UTC', '11:19'),

    'mssqlserver': os.getenv('MS_SQL_SERVER', '173.193.179.253:1433'),
    'mssqluser': os.getenv('MS_SQL_USER', 'SA'),
    'mssqlpassword': os.getenv('MS_SQL_PASSWORD', 'RTopps_2017'),
    'mssqldb': os.getenv('MS_SQL_DATABASENAME', 'ravitest'),

    'psqlserver': os.getenv('POSTGRE_SERVER', '40.71.214.191'),
    'psqluser': os.getenv('POSTGRE_USER', 'postgres'),
    'psqlpassword': os.getenv('POSTGRE_PWD', 'RandomTrees_2017'),
    'psqldb': os.getenv('POSTGRE_DATABASE', 'ravitest'),

    'from_mail': os.getenv('SENDER_MAILID', 'ravithejab@gmail.com'),
    'to_mail': os.getenv('RECIPIENT_MAILID', 'vavasarala@randomtrees.com'),
    'mail_pwd': os.getenv('SENDER_PASSWORD', ''),

    'smtp_host': os.getenv('SMTP_HOST_PORT', 'smtp.gmail.com:587'),
    'ssl_true': os.getenv('SSL_TRUE', False),
    'start_tls': os.getenv('START_TLS', True),

}
