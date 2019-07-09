import itchat
import jieba
import re

itchat.auto_login(hotReload=True)

friends = itchat.get_friends(update=True)[0:]

sigList = []

for i in friends:
    signature = i["Signature"].strip().replace("span", "").replace("class", "").replace("emoji", "")
    #将正则表达式进行编译
    rep =re.compile('1f\d+\w*|[<>/=""\n]')
    signature = rep.sub('', signature)
    sigList.append(signature+'\n')

text = "".join(sigList)

wordlist = jieba.cut(text,cut_all=True)

word_space_split = "".join(wordlist)


from wordcloud import WordCloud ,ImageColorGenerator
import numpy as numpy
import PIL.Image as Image
import matplotlib.pyplot as pyplot

coloring = numpy.array(Image.open('/home/null/Downloads/pict.png'))

my_wordcloud = WordCloud(font_path='/home/null/Desktop/pythonExc/simhei.ttf', background_color='grey', max_words=3000, mask=coloring, max_font_size=60, random_state=42, scale=2).generate(word_space_split)

image_colors = ImageColorGenerator(coloring)

pyplot.imshow(my_wordcloud.recolor(color_func=image_colors))

pyplot.imshow(my_wordcloud)

pyplot.axis('off')

pyplot.show()






