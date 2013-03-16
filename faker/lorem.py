from faker import frandom
from faker import helper
from faker import definitions
import random
def words(num=False):
    if not num:
        num = 3
    return helper.shuffle(definitions.lorem())[:num]

def sentence(word_count=False):
    if not word_count:
        word_count = 3
    return  " ".join(words(word_count + random.randint(0,7))).title()+"."


def sentences(sentence_count=False):
    if not sentence_count:
        sentence_count
    sentences=[] 
    for i in range(sentence_count):
        sentences.append(sentence())
    return " ".join(sentences)

def paragraph(sentence_count=False):
    if not sentence_count:
        sentence_count = 3
    return sentences(sentence_count + random.randint(0,3))

def paragraphs(paragraph_count):
    if not paragraph_count:
        paragraph_count = 3
    paragraphs = []
    for i in range(paragraph_count):
        paragraphs.append(paragraph())
    return ("\n \r\t").join(paragraphs)