import xlsxwriter as xlsxwriter
from nltk import wordpunct_tokenize
from nltk.corpus import stopwords
from openpyxl import load_workbook
import os
import re
from openpyxl import load_workbook
from collections import Counter
import enchant
import unicodedata

from langdetect import detect, DetectorFactory
from langdetect import detect_langs

DetectorFactory.seed = 0

sentenceCount = 0

sgenCount = 0

inputsen = open('post_unique.txt', 'r', encoding='latin-1')
for i in inputsen:
    if str(i) !="":
        if str(i)!=" ":

            print(str(i).strip())






languages_ratios = {}
row1 = 0
col1 = 0

workbook1 = xlsxwriter.Workbook('SinglishSentences.xlsx')
worksheet1 = workbook1.add_worksheet()


worksheet1.write(row1, col1, "test")


workbook1.close()


