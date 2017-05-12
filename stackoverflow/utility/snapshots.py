import json
import re
from collections import Counter, OrderedDict

import matplotlib.pyplot as plt
import numpy as np

count = 0

# with open(r"/home/lhan/workplace/stackoverflow/stackoverflow/spiders/newest_266000_267000.json", "r", encoding="utf-8") as f:
# with open(r"/home/lhan/workplace/stackoverflow/stackoverflow/spiders/newest_1_1000_time_stamped.json", "r", encoding="utf-8") as f:
with open(r"/home/lhan/workplace/stackoverflow/stackoverflow/spiders/newest_166000_167000.json", "r", encoding="utf-8") as f:
    data = json.load(f)
    for _, value in enumerate(data):
        # TODO get the time of each piece of data
        # and see wheter it contains tag java and functional programming
        # within a limited span of time
        tags = value['tags']
        if "java" in tags and "functional-programming" in tags:
            print(value['questions'])
            count+=1

print("There are " + str(count) + " edges between java and functional programming tags.")
