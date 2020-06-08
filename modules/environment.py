import os

"""
获取系统的所有环境变量
"""


def run(** args):
    print("In environment module")
    return str(os.version)
