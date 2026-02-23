import random

print("\n\n           if Zero(0) leave it empty..")
noun = input("How many nouns? ")
verb = input("\nHow many verbs? ")
adj = input("\nHow many adjectives? ")

if noun:
    print("Nouns: ")
    for i in range(int(noun)):
        print("\n      " + random.choice(list(open("nouns.txt"))))

if verb:
    print("Verbs: ")    
    for i in range(int(verb)):
        print("\n      " + random.choice(list(open("verbs.txt"))))

if adj:
    print("Adjectives: ")
    for i in range(int(adj)):
        print("\n      " + random.choice(list(open("adjectives.txt"))))
    
    
