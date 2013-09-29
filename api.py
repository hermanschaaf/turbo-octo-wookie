import re
import nltk
from nltk.corpus import wordnet as wn

re_query = re.compile(r'\*{3}(.*)\*{3}')


def best_definitions(context):
    """
    context is a unicode string argument with the word or phrase to be
    looked up marked like this:

        And now for something ***completely*** different

    The above example will return possible definitions for the word 
    "completely" as used in this context.
    """
    text = nltk.word_tokenize(context)
    query_indexes = [i for i, w in enumerate(text) if re_query.match(w)]
    text = [w.strip('*') for w in text]
    
    tagged_words = nltk.pos_tag(text)
    word, tag = tagged_words[query_indexes[0]]
    synsets = wn.synsets(word)

    results = [s for s in synsets if s.name.split('.')[1] == tag.lower()[0]]
    
    return results if results else synsets


if __name__ == '__main__':

    # first example
    context = u"I ***refuse*** to accept refuse."
    print context
    print "---------------"
    results = best_definitions(context)
    for result in results:
        print result.definition

    print "=========="

    # second example
    context = u"I refuse to accept ***refuse***."
    print context
    print "---------------"
    results = best_definitions(context)
    for result in results:
        print result.definition