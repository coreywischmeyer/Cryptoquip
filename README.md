#Cryptoquip

This program solves the cryptoquips or cryptograms in the puzzle section of your newspaper. 

```bash
usage: cryptoquip.py [-h] puzzle word_list

Solve your Sunday Cryptoquip!

positional arguments:
  puzzle      A text file that contains your Cryptoquip
  word_list   A text file list of English words

optional arguments:
  -h, --help  show this help message and exit
```

##Input
```
Contents of puzzle.txt:
TGIAB FZU TGPHVGHPB FPB GSB BTTBZVB QR F CQQW OPBFG KUBFT FPB SQOLFTS
```

##Output
The output is actually the resulting set for each letter. For example, there wasn't enought information in the below result to decide if: `QR` is `OF`, `OX`, or `OK`, etc.

```
['S']['T']['Y']['L']['E'] ['A']['N']['D'] ['S']['T']['R']['U']['C']['T']['U']['R']['E'] ['A']['R']['E'] ['T']['H']['E'] ['E']['S']['S']['E']['N']['C']['E'] ['O']['X', 'K', 'B', 'Z', 'F'] ['A'] ['B', 'Z']['O']['O']['K', 'M'] ['G']['R']['E']['A']['T'] ['I']['D']['E']['A']['S'] ['A']['R']['E'] ['H']['O']['G']['W']['A']['S']['H']
```

That means you'll have to decide which letter makes sense in some instances. 

##How it works

The program transforms both the puzzle and list of words into patterns. For example: `HELLO` is `ABCCD`. The puzzle's words are then joined with all the words that match the pattern. The choices are then pruned by iterating over the sets until nothing changes after pruning.
