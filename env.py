# -*- coding: utf-8 -*-
import os
from dotenv import load_dotenv
from os.path import join, dirname

load_dotenv(verbose=True)

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

host = os.environ.get("HOST")
database = os.environ.get("DATABASE")
user = os.environ.get("USER")
password = os.environ.get("PASSWORD")