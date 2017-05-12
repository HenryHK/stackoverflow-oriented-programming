from collections import Counter
from collections import OrderedDict
import json
import networkx as NX
import matplotlib.pyplot as plt
import functools
import itertools

python_related = []
with open(r"/home/lhan/workplace/stackoverflow/stackoverflow/spiders/page1-500.json", "r", encoding="utf-8") as f1:
    data1 = json.load(f1)
    for _, value in enumerate(data1):
        if 'python' in value['tags']:
            python_related.append(value)

with open(r"/home/lhan/workplace/stackoverflow/stackoverflow/spiders/page501-1000.json", "r", encoding="utf-8") as f2:
    data2 = json.load(f2)
    for _, value in enumerate(data2):
        if 'python' in value['tags']:
            python_related.append(value)

def comp(x, y):
    return int(x['votes'][0])>int(y['votes'][0])

python_related.sort(key=functools.cmp_to_key(comp))


with open(r'python_result.json','w') as python_result:
    json.dump(python_related, python_result, indent=4)

pairs = []
for value in python_related:
    l = [tag for tag in value['tags'] if tag!='python']
    for result in itertools.combinations(l,2):
        pairs.append(result)


counter = Counter(pairs)
counter_most = dict(counter.most_common(50))

# unweigted
unweighted_edges = [key for key in counter_most.keys()]
unweighted = NX.Graph()
unweighted.add_edges_from(unweighted_edges)

pos = NX.spring_layout(unweighted)

# node
NX.draw_networkx_nodes(unweighted,pos,node_size=200)

# edge
NX.draw_networkx_edges(unweighted, pos, edgelist=unweighted.edges(), wdith=6)

# draw
NX.draw_networkx_labels(unweighted,pos,font_size=14,font_family='sans-serif')

#NX.draw_networkx(unweighted)
limits = plt.axis('off')
plt.show()

# # weigted
weighted_edges = [(n1, n2, weight) for (n1,n2),weight in zip(counter_most.keys(), counter_most.values())]
weighted = NX.Graph()
for (u,v,d) in weighted_edges:
    weighted.add_edge(u,v,weight = d)

elarge=[(u,v) for (u,v,d) in weighted.edges(data=True) if d['weight'] >10]
esmall=[(u,v) for (u,v,d) in weighted.edges(data=True) if d['weight'] <=10]

pos=NX.spring_layout(weighted) # positions for all nodes

# nodes
NX.draw_networkx_nodes(weighted,pos,node_size=700)

# edges
NX.draw_networkx_edges(weighted,pos,edgelist=elarge,
                    width=6)
NX.draw_networkx_edges(weighted,pos,edgelist=esmall,
                    width=6,alpha=0.5,edge_color='b',style='dashed')

# labels
NX.draw_networkx_labels(weighted,pos,font_size=20,font_family='sans-serif')
print(len(weighted.edges()))
plt.axis('off')
plt.show() # display

print("Weighted edges number: "+str(len(weighted.edges())))
print("Unweighted edges number: "+str(len(unweighted.edges())))
