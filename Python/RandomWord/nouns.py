from pathlib import Path

from nltk.corpus import wordnet

nouns = (n.name().split(".")[0] for n in wordnet.all_synsets("n"))
nouns = (n for n in nouns if all(c not in n for c in "/_0123456789"))

verbs = (n.name().split(".")[0] for n in wordnet.all_synsets("v"))
verbs = (n for n in verbs if all(c not in n for c in "/_0123456789"))

adjectives = (n.name().split(".")[0] for n in wordnet.all_synsets("a"))
adjectives = (n for n in adjectives if all(c not in n for c in "/_0123456789"))

Path("nouns.txt").write_text("\n".join((*sorted(set(nouns)), "")))
Path("verbs.txt").write_text("\n".join((*sorted(set(verbs)), "")))
Path("adjectives.txt").write_text("\n".join((*sorted(set(adjectives)), "")))
