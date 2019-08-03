import time
from multiprocessing import Process
from adslpool.api import app
from adslpool.setting import *


class Scheduler(object):
    @staticmethod
    def api():
        print('API接口开始运行')
        app.run(host=API_HOST, port=API_PORT)

    def run(self):
        if API_PROCESS:
            api_process = Process(target=Scheduler.api)
            api_process.start()


