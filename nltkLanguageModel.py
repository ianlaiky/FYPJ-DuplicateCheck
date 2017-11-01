from nltk import wordpunct_tokenize
from nltk.corpus import stopwords
word =" Tiagong from reliable source related to peter that peter doesn't allow her to step into the amk home liao. That's why until now havent visit the two past tense dotters"


# print(stopwords.fileids())


languages_ratios = {}
tokens = wordpunct_tokenize(word)

words = [word.lower() for word in tokens]


# list of sets of stopwords for each language
dictOfSetsOfStopwords=[]

# for language in stopwords.fileids():
#     stopwords_set = set(stopwords.words(language))
#     dictOfSetsOfStopwords[language]=stopwords_set






# print(languages_ratios)