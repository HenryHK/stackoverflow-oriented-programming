import json
import re
from collections import Counter, OrderedDict

import matplotlib.pyplot as plt
import numpy as np

languages = ['c', 'c++', 'java', 'c#','python', 
                'javascript', 'objective-c', 'php',
                'go', 'ruby']
test = ["C=", "this", "is", "bias", "Objective-C"]

data = {}

with open(r"/home/lhan/workplace/stackoverflow/stackoverflow/spiders/newest_1_1000_time_stamped.json", "r", encoding="utf-8") as f1:
    data1 = json.load(f1)
    for _, value in enumerate(data1):
        # TODO regex applied here
        if len(value['time_stamps'])<=0:
            continue
        time = str(value['time_stamps'][0])
        tags = value['tags']
        matchObj = re.search(r'(?=\')\'[0-1][0-9]', time)
        if(type(matchObj)==type(None)):
            matchObj = re.search(r'(?=20)20[0-1][0-9]', time)
            year = matchObj.group().replace('20', "")
        else:
            year = matchObj.group().replace('\'', "")
        matchedLanguages = [x for x in languages if x in tags]
        if year in data.keys():
            new = []
            for ele in data[year]:
                new.append(ele)
            for ele in matchedLanguages:
                new.append(ele)
            data[year] = new
        else:
            data[year] = list(matchedLanguages)
        

countData = {}
for year, matched in data.items():
    countData[year] = dict(Counter(data[year]))

countData = sorted(countData.items(), key=lambda k: int(k[0]))


groups = len(countData)
c = ()
cpp = ()
java = ()
csharp = ()
python = ()
javascript = ()
objectivec = ()
php = ()
go = ()
ruby = ()
years = tuple([str(x).zfill(2) for x in range(16,18)])

print(years)
print(countData)

for year in years:
    if year not in (dict(countData)).keys():
        countData.append((year,{}))
print(countData)

data_to_removed = []
for i in range(0, len(countData)):
    if countData[i][0] not in years:
        data_to_removed.append(countData[i])
for data in data_to_removed:
    countData.remove(data)

countData = sorted(countData, key=lambda k: int(k[0]))
print(countData)


for data in countData:
    for l in languages:
        if l not in data[1].keys():
            data[1][l] = 0
    for language, times in data[1].items():
        if language == 'c':
            c = c + (times,)
        if language == 'c++':
            cpp = cpp + (times,)
        if language == 'java':
            java = java + (times,)
        if language == 'c#':
            csharp = csharp + (times,)
        if language == 'python':
            python = python + (times,)
        if language == 'javascript':
            javascript = javascript + (times,)
        if language == 'objective-c':
            objectivec = objectivec + (times,)
        if language == 'php':
            php = php + (times,)
        if language == 'go':
            go = go + (times,)
        if language == 'ruby':
            ruby = ruby + (times,)

groups = len(years)
fig, ax = plt.subplots()
index = np.arange(groups)
bar_width = 0.4

opacity = 0.4
each_language = [c, cpp, java, csharp, python, javascript, objectivec, php, go, ruby]
colors = ['#FF0000', '#000000', '#FFFF33', '#800080', '#FF00FF', '#0000FF', '#708090', '#00FA9A', '#B8860B', '#CD5C5C']
divider = len(each_language)

# print(java)

# bar(left, height, width=0.8, bottom=None, hold=None, data=None, **kwargs)
labeled = False
counter = 0
print(divider)
for l in each_language:
    plt.bar(index+ counter*bar_width/divider, l, bar_width/divider, alpha=opacity, color=colors[counter],label=languages[counter])
    counter = counter+1

plt.xticks(index + divider*bar_width/(2*divider), years)
plt.tight_layout() 
plt.legend()
plt.show()