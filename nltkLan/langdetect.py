from langdetect import detect, DetectorFactory
from langdetect import detect_langs
DetectorFactory.seed = 0
print(detect('Have you eaten?'))
print(detect_langs('What did you eat?'))