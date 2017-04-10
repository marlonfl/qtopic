from gensim.models import word2vec as w2v
import os
import sys

class MySentences(object):
    def __init__(self, dirname):
        self.dirname = dirname

    def __iter__(self):
        for fname in os.listdir(self.dirname):
            for line in open(os.path.join(self.dirname, fname)):
                yield line.split()


if __name__ == "__main__":
    sentences = MySentences(sys.argv[1])
    model = w2v.Word2Vec(sentences, min_count=1)

    print(model.similarity('this', 'test'))
