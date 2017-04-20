import logging
import os.path
import sys
import time

from wickiecorpus import WikiCorpus

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

    output = open(outp, 'w')
    wiki = WikiCorpus(inp, lemmatize=False, dictionary={})
    t = time.time()
    for text in wiki.get_texts():
        output.write(space.join(text).decode() + "\n\n")
        i = i + 1
        #if i == 5:
        #    break
        if (i % 50 == 0):
            t2 = time.time()
            logger.info("Saved " + str(i) + " articles")

            per_s = 50/(t2-t)
            logger.info("Current Rate: %.2f/s" % per_s)
            if i <= 4500000:
                logger.info("Approx. time left: %.2f hours" % (((4500000-i)/per_s)/3600))
            t = t2
    output.close()
    logger.info("Finished Saved " + str(i) + " articles")
