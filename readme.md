#What? Be.

This is an exercise in attempting to create a terse, Beckett- or Mamet- style dialogue through a computer. The first line would be inqusitive, the second line obnoxious, the third line then repetitive and annoyed, yet with more detail. This piece is semi-context-aware, based on parts-of-speech and sentence strucutre, and randomness comes in the form of phrase pairings. The project utilizes the [NLTK library](http://nltk.org/), with the [Brown Corpus](http://icame.uib.no/brown/bcm.html) for part of speech identification and phrase placement.

##Dialogue format:

> Question phrase + chain based on typically related tags to the phrase + ?
> Terse, pointed repitition of the final word + pronoun-based "being" phrase. Repeat Q?
> Repeat Question phrase predicate. Verb phrase + chain based phrase + final piece of original question + prepositional phrase to close sentence ...

##Examples:

    who was thereby prevented himself with another part?
    part, he would. who?
    was thereby. suddenly grinned and i'd rattle with, another part from the quarry...

    that was somehow seeing himself toppling growing-waiting well?
    well, it will. that?
    was somehow. only put around since with though, growing-waiting well in the jungle...

    which was doubtful five-hundred bombs hanging indeed run?
    run, they would. which?
    was doubtful. already working on scotty's entertainments given, indeed run of the road...

    which is filled i'd rendezvous carmer banging more?
    more, you need. which?
    is filled. still refused to their more loudly, banging more to the daintylegged...

##Requirements:

[Natural Language Toolkit 2.0](http://nltk.org/) (using the [Brown Corpus](http://icame.uib.no/brown/bcm.html))

    sudo pip install -U numpy pyyaml nltk
    sudo python -m nltk.downloader -d /usr/share/nltk_data all

####Command Line:

Usage (arguments can be empty):

    python what.py <number of iterations (def=3)>

Fun with say (Mac OSX):

    python what.py > foo; cat foo; say -v Alex < foo
