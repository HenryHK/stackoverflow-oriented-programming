from collections import Counter
from collections import OrderedDict
import json
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import itertools
import networkx as NX


tags = []
with open(r"/home/lhan/workplace/stackoverflow/stackoverflow/spiders/page1-500.json", "r", encoding="utf-8") as f1:
    data1 = json.load(f1)
    for _, value in enumerate(data1):
        tags.append(value['tags'])

with open(r"/home/lhan/workplace/stackoverflow/stackoverflow/spiders/page501-1000.json", "r", encoding="utf-8") as f2:
    data2 = json.load(f2)
    for _, value in enumerate(data2):
        tags.append(value['tags'])

print(len(tags))

# print(tags[0])
# print(tags[1])

edges = []
for tag in tags:
    for result in itertools.combinations(tag, 2):
        edges.append(result)

print(len(edges))
g = NX.Graph()
g.add_edges_from(edges)

NX.draw_networkx(g)
NX.write_gexf(g, "full_network.gexf") #export full network
# limits = plt.axis('off')
# plt.show()