import os
import sys

sys.path.append("..")
sys.path.append("../..")

import json

from global_config import *
from lib.task.test_task import *
from lib.util.misc import *


class TestCombination(object):
    def __init__(self, combination_file):
        if os.path.exists(combination_file) == False:
            print("cannot find %s" % combination_file)
            raise

        self.combination_file = combination_file
        self.test_combination = []
        self.machine_pool = None

    def parse_combination(self):
        combination_dict = jsonfile2dict(self.combination_file)

        test_combination = combination_dict["combination"]
        for item in test_combination:
            tmp_dic = {"suite": None, "option": None}
            tmp_dic["suite"] = os.path.join(TAOTIE_HOME, item["suite"])
            tmp_dic["option"] = os.path.join(TAOTIE_HOME, item["option"])
            self.test_combination.append(tmp_dic)
        self.machine_pool = combination_dict["machine_pool"]

    def create_test_task(self, branch=None, commit_id=None, author=None, test_type="DAILY", official_task=True):
        if self.test_combination == None or self.machine_pool == None:
            print("test_combination / machine_pool should not be None")
            raise

        test_task_list = []
        for machine in self.machine_pool:
            for item in self.test_combination:
                option_dict = jsonfile2dict(item["option"])
                project = option_dict["project"]
                if project == "INTEL_CAFFE":
                    task = TestTaskCaffe(option=item["option"], suite=item["suite"], machine=machine, branch=branch,
                                         commit_id=commit_id, author=author, test_type=test_type,
                                         official_task=official_task)
                elif project == "INTEL_CHAINER":
                    task = TestTaskChainer(option=item["option"], suite=item["suite"], machine=machine, branch=branch,
                                           commit_id=commit_id, author=author, test_type=test_type,
                                           official_task=official_task)
                elif project == "INTEL_THEANO":
                    task = TestTaskTheano(option=item["option"], suite=item["suite"], machine=machine, branch=branch,
                                          commit_id=commit_id, author=author, test_type=test_type,
                                          official_task=official_task)
                elif project == "INTEL_TORCH":
                    task = TestTaskTorch(option=item["option"], suite=item["suite"], machine=machine, branch=branch,
                                         commit_id=commit_id, author=author, test_type=test_type,
                                         official_task=official_task)
                elif project == "INTEL_DNET":
                    task = TestTaskDnet(option=item["option"], suite=item["suite"], machine=machine, branch=branch,
                                        commit_id=commit_id, author=author, test_type=test_type,
                                        official_task=official_task)
                else:
                    task = TestTask(option=item["option"], suite=item["suite"], machine=machine, branch=branch,
                                    commit_id=commit_id, author=author, test_type=test_type,
                                    official_task=official_task)

                test_task_list.append(task)

        return test_task_list