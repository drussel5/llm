Welcome to the super simple LLM. 
This is a space where I learn about the concepts and moving parts that create an LLM.
I'll push things occasionally as I learn them.

Most recently I added a simple tokenizer.
The tokenizer can encode and decode with a simple library.

Next:
- I'll be making the vocabulary broader to be able to include all of the words in "The Verdict" by Edith Wharton.
- I'll be adding special context tokens since I am still tokenizing full words.

Next next:
- add a new version of the tokenizer using byte pair encoding
  - will allow for fewer context tokens, specifically won't need an unknown context token
