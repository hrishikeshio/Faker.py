
def words(num=False):
    if not num:
        num = 3
    return helper.shuffle(definitions.lorem()).slice(0, num)

def sentence(word_count=False):
    if not word_count:
        word_count = 3
    return  words(word_count + helper.random_number(7)).join(' ').totitle()


def sentences(sentence_count=False):
    if not sentence_count:
        sentence_count
    sentences=[] 
    for i in range(sentence_count):
        sentences.append(sentence())
    return sentences.join("\n")

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
    return paragraphs.join("\n \r\t")