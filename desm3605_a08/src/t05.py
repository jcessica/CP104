"""
------------------------------------------------------------------------
[program description]
------------------------------------------------------------------------
Author: Jessica Desmond
ID:     169033605
Email:  desm3605@mylaurier.ca
__updated__ = "2023-11-24"
------------------------------------------------------------------------
"""

# Imports
from functions import has_word_chain
# Constants
words = ['camel', 'leopard', 'dog', 'garry', 'yank']
word_chain = has_word_chain(words)

print(f"Words: {words}")
print(word_chain)