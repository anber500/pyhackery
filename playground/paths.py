import os
import sys

__this_dir = os.path.dirname(os.path.abspath(__file__))
__parent_dir = os.path.split(__this_dir)[0]

PYHACKERY_SYS_PATH = os.path.join(__parent_dir, "pyhackery")
sys.path.append(PYHACKERY_SYS_PATH)
