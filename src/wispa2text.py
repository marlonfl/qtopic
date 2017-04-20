import logging
import os.path
import sys
import spacy

from wickiecorpus import WikiCorpus
from gensim import utils


if __name__ == '__main__':
    program = os.path.basename(sys.argv[0])
    logger = logging.getLogger(program)

    logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s')
    logging.root.setLevel(level=logging.INFO)
    logger.info("running %s" % ' '.join(sys.argv))

    # check and process input arguments
    if len(sys.argv) < 3:
        sys.exit("not enough arguments")

    inp, outp = sys.argv[1:3]
    space = b" "
    i = 0

    #output = open(outp, 'w')
    wiki = WikiCorpus(inp, lemmatize=False, dictionary={})
    sp = spacy.load("en")
    for text in wiki.get_texts():
        text = space.join(text).decode()
        # print ("MAYBE WRONG")
        print (text)
        # print ("\n\n\n\n")
        # test = sp(text)
        # for ent in test.ents:
        #     print (ent)
        #output.write(space.join(text) + "\n")
        i = i + 1
        if i == 1:
            break
        #if (i % 10000 == 0):
        #    logger.info("Saved " + str(i) + " articles")

    #output.close()
    #logger.info("Finished Saved " + str(i) + " articles")
