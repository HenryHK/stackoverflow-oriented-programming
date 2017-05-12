from collections import Counter
from collections import OrderedDict
import json
from wordcloud import WordCloud
import matplotlib.pyplot as plt


tags = []
with open(r"/home/lhan/workplace/stackoverflow/stackoverflow/spiders/page1-500.json", "r", encoding="utf-8") as f1:
    data1 = json.load(f1)
    for _, value in enumerate(data1):
        tags.extend(value['tags'])

with open(r"/home/lhan/workplace/stackoverflow/stackoverflow/spiders/page501-1000.json", "r", encoding="utf-8") as f2:
    data2 = json.load(f2)
    for _, value in enumerate(data2):
        tags.extend(value['tags'])

counter = Counter(tags)
counter_most = counter.most_common(200)

wordcloud = WordCloud(font_path=r"/usr/share/fonts/truetype/freefont/FreeSans.ttf",
                      width=1200,
                      height=600,
                      max_words=200).generate_from_frequencies(dict(counter_most))
plt.imshow(wordcloud)
plt.axis('off')
plt.show()

wordcloud.to_file(r'/home/lhan/workplace/stackoverflow/stackoverflow/utility/word_cloud.jpg')
