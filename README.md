Context-sensitive dictionary lookups
=================

A small demo of a dictionary that takes information about the surrounding sentence into account. For example:

```sh
>>> from api import best_definitions
>>> results = best_definitions(u"I ***refuse*** to accept refuse.")
>>> for result in results:
...     print result.definition
...
show unwillingness towards
refuse to accept
elude, especially in a baffling way
refuse to let have
resist immunologically the introduction of some foreign tissue or organ
refuse entrance or membership

>>> results = best_definitions(u"I refuse to accept ***refuse***.")
>>> for result in results:
...     print result.definition
... 
food that is discarded (as from a kitchen)

```

In the above examples, results are returned based on the two different senses of the word `refuse`. In other words, the dictionary is sensitive to the context of the word being looked up.

But mostly this is a playground for toying with all the awesome capabilities of NLTK, the Python Natural Language Toolkit.

Author: Herman Schaaf ([IronZebra](http://www.ironzebra.com))

License: MIT License
