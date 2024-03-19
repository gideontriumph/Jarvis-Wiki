"""
    Name: wikipedia_1.py
    Author: Triumhp Ogbonnia
    Created: 3/17/24
    Purpose: Jarvis wikipedia
"""

# pip install wikipedia
from rich.console import Console
import wikipedia

# Initialize the console
console = Console()

# Type in your search term
result = console.input("[bold blue]Search Wikipedia >> [/bold blue]")

# Return a summary result of 3 sentences
summary = wikipedia.summary(result, sentences=3)

# Print the result
console.print("[bold blue]\nResult >>[/bold blue]" ,summary)