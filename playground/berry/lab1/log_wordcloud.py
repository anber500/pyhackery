import os
import re
from os import listdir
from os.path import isfile, join

import numpy
from PIL import Image
from wordcloud import WordCloud, STOPWORDS

"""
The following code will look through your logs and create a wordcloud out of the most mentioned words.
"""


class LogCloud:
    # this is a list of chars that we want to use to split strings into different words
    delimiters = ",", "...", "?", "|", "#", ".", "!", " ", "/", "\\", "\n", ":", "-", "@"

    # this is our bucket where we will dump our strings
    string_bucket = ""
    # this is the folder that we will search
    search_path = ""
    # this is an optional path to your mark
    mask_path = ""

    """
    This is your constructor
    """

    def __init__(self, search_path, mask_path):
        self.search_path = search_path
        self.mask_path = mask_path

        self.__explore()  # explore the filestructure
        self.__generate_wordcloud()  # generate the word cloud image

    """
    This method will explore your folders
    """

    def __explore(self, path=None):
        # on initial call, do not set the path
        if not path:
            path = self.search_path

        # return a list of directories
        dir_list = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
        # loop through the directories
        for dir in dir_list:
            # generate a directory path by using the old python string method
            dir_path = '%s\%s' % (path, dir)
            try:
                # get the list of files in a directory
                files = [f for f in listdir(dir_path) if isfile(join(dir_path, f))]
                for file in files:
                    # add the string to the cloud strings
                    self.string_bucket += self.__collect_words('%s\%s' % (dir_path, file))

                # recursive call to iterate through the directories
                self.__explore(dir_path)
            except Exception as exp:
                # generate an error message by using the new python 3 "format"
                print("permission issue for {0}".format(dir))

    """
    This method will collect words from a log file and return it as a single string
    """

    def __collect_words(self, file):
        # this is the string that will be returned
        _string = ""
        # open files that ends with .log extension
        if file.endswith('.log'):
            with open(file, "r") as ins:
                for line in ins:
                    # split the string at the delimiters and create words
                    regexPattern = '|'.join(map(re.escape, self.delimiters))
                    # get rid of any characters we don't want
                    line = re.sub('[#$()<>=~*^&{}"]', '', line)
                    words = re.split(regexPattern, line)
                    # this gets rid of any empty strings in the array and words that are not longer than 1 character
                    words = [_word for _word in words if _word and len(_word) > 1]
                    # only add list of words that are larger than 0
                    if len(words) > 0:
                        # join everything into one big sentence
                        _string += ' '.join(words)
        # return the sting
        return _string

    """
    Generate a word cloud from the top 200 collected strings
    """

    def __generate_wordcloud(self):
        if not self.string_bucket:
            print("You can't generate a word cloud without words!")
        else:
            # Open the mask and convert to an array
            mask = numpy.array(Image.open(self.mask_path))
            # create the word cloud
            wordcloud = WordCloud(background_color="white",
                                  max_words=200,
                                  stopwords=STOPWORDS,  # common words that needs to be ignored
                                  random_state=5,
                                  mask=mask).generate(self.string_bucket)
            # save it to file
            wordcloud.to_file("pyhackery.png")
