import pandas as pd
import numpy as np
import pycountry
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
from yandex_translate import YandexTranslate
from yandex_translate import YandexTranslateException

YANDEX_API_KEY = 'trnsl.1.1.20180409T091123Z.2e26c9a93f898363.415b316ae3f5492c0370cba8a72e925ab753e2ad'
try:
    translator_obj = YandexTranslate(YANDEX_API_KEY)
except YandexTranslateException:
    translator_obj = None

# Generation color map
# They return color list
def getColors():
    COLORS = []
    cm = plt.cm.get_cmap('hsv', n)
    for  i in np.arange(n):
        COLORS.append(cm(i))
    return COLORS

def translate(string, translator_obj = None):
    if translator_obj == None:
        return string
    t = translator_obj.translate(string, 'en-ru')
    return t['text'][0]

def dict_sort(my_dict):
    keys = []
    values = []
    my_dict = sorted(my_dict.items(), key = lambda x:x[1], reverse = True)
    for k, v in my_dict:
        keys.append(k)
        values.append(v)
    return (keys, values)

df = pd.read_csv('./scrubbed.csv', escapechar = '`', low_memory = False)
df = df.replace({'shape': None}, 'unknown')


country_label_count = pd.value_counts(df['country'].values)
for label in list(country_label_count.keys()):
    c = pycountry.countries.get(alpha_2 = str(label).upper())
    t = translate(c.name, translator_obj)
    df = df.replace({'country':str(label)}, t)
