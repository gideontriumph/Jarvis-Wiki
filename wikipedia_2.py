"""
    Name: wikipedia_2.py
    Author: Triumhp Ogbonnia
    Created: 3/17/24
    Purpose: OOP method which can be integrated into main JARVIS project
"""
# pip install wikipedia
import wikipedia
from rich.console import Console

# Initialize the console
console = Console()

class WikipediaApp:
    def __init__(self):
        pass
    
    def get_wikipedia(self):
        """
            Search Wikipedia
        """
        try:
            # Type in your search term
            result = console.input("[blue]\nSearch Wikipedia >> [/blue]")
            # Return a summary result for 3 sentences
            self._summary = wikipedia.summary(result, sentences=3)
            
        except:
            # Use raise for triubleshooting exceptions
            # raise
            # If there is an exception, allow the user to try again.
            console.print("[red]Try a different search term.[/red]")
            console.print("[blue]\nSearch Wikipedia >> [/blue]")
            
    def display_wikipedia(self):
        """
            Display Wikipedia search results
        """
        console.print("[green]\nResult >> [/green]", self._summary)
        
# Create a jarvis program object
wikipedia_app = WikipediaApp()
while True:
    wikipedia_app.get_wikipedia()
    wikipedia_app.display_wikipedia()