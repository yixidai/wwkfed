# coding=utf-8
try:
    import sys
except:
    pass
try:
    import os
except:
    pass
try:
    import socket
except:
    pass
try:
    import traceback
except:
    pass
try:
    import copy
except:
    pass
try:
    import re
except:
    pass
try:
    import math
except:
    pass
try:
    import time
except:
    pass
try:
    import datetime
except:
    pass
try:
    import codecs
except:
    pass
try:
    import SocketServer
except:
    pass
try:
    import SimpleXMLRPCServer
except:
    pass
try:
    import imp
except:
    pass
try:
    import logging
except:
    pass
try:
    import struct
except:
    pass
try:
    import urllib2
except:
    pass
try:
    import urllib
except:
    pass
try:
    import json
except:
    pass
try:
    import cookielib
except:
    pass
try:
    import threading
except:
    pass
try:
    import xmlrpclib
except:
    pass
try:
    import subprocess
except:
    pass
try:
    import shelve
except:
    pass
try:
    import multiprocessing
except:
    pass
try:
    import hashlib
except:
    pass
try:
    import inspect
except:
    pass
try:
    import zipfile
except:
    pass
try:
    import types
except:
    pass
try:
    import random
except:
    pass
try:
    import ConfigParser
except:
    pass
try:
    import pickle
except:
    pass
try:
    import zipfile
except:
    pass
try:
    import tarfile
except:
    pass
try:
    import platform
except:
    pass
try:
    import gc
except:
    pass
try:
    import uuid
except:
    pass
try:
    import string
except:
    pass
try:
    import weakref
except:
    pass
try:
    import Cookie
except:
    pass
try:
    import shutil
except:
    pass
try:
    import StringIO
except:
    pass
try:
    import gzip
except:
    pass
try:
    import sqlite3
except:
    pass
try:
    import decimal
except:
    pass
try:
    import fcntl
except:
    pass
try:
    import email.mime.text
    import email.header
except:
    pass
try:
    import smtplib
except:
    pass
try:
    import cgi
except:
    pass
try:
    import math
except:
    pass
try:
    import collections
except:
    pass
try:
    import binascii
except:
    pass
try:
    import pymongo
except:
    pass

#{找到项目根目录}
cur_dir = os.path.realpath(os.path.dirname(__file__))
while True:
    if os.path.exists(cur_dir + "/util/allimport3.py"):
        sys.path.append(cur_dir)
        break
    cur_dir = os.path.realpath(cur_dir + "/..")
#{找到项目根目录}
from util.allimport3 import f
from config.conf import conf_handler
from db.storage import Mongodb_handler, DB_handler


def main():
    # while True:
    #     f.p("running")
    #     f.ec(f.let_print_exc(main))
    #     time.sleep(1)
    try:
        worker = Worker()
        worker.work()
    except:
        f.p(f.exc())


class Worker:

    def __init__(self, ):
        user_log_handler = Mongodb_handler(conf_handler.get("user_log"))
        self.user_log_reader = DB_handler(user_log_handler)

        channel_pv_uv_handler = Mongodb_handler(conf_handler.get("channel_pv_uv"))
        self.channel_data_writer = DB_handler(channel_pv_uv_handler)

        daily_break_point_handler = Mongodb_handler(conf_handler.get("daily_break_point"))
        self.daily_break_point_rw = DB_handler(daily_break_point_handler)

        self.server_name = f.name(__file__)
        self.flag_key_template = "%(date)s.done.%(server_name)s"
        # f.eb()

    def deal_date(self, date):
        self.__dict__.update(locals())
        self.check_date_done()
        f.eb()

    def check_date_done(self, ):
        self.flag_key = self.flag_key_template % self.__dict__
        rt = self.daily_break_point_rw.exist_key(self.flag_key)
        f.eb()
        if rt:
            return True
        else:
            return False

    def work(self, ):
        work_dates = f.date_section(f.ago(30), f.ago(1))
        f.deal_col(work_dates, self.deal_date)

if __name__ == "__main__":
    f.check_process_exist()
    main()


# end
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
