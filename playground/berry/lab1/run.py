from playground.berry.lab1 import log_wordcloud
import os
dir_path = os.path.dirname(os.path.realpath(__file__))
log_wordcloud.LogCloud("D:\\", dir_path + "\mask.png")

