"""
    Name: Jarvis_wikipedia.py
    Author: Triumph Ogbonnia
    Created: 3/19/24
    Purpose: Jarvis text to speech wikipedia implementation
"""


import wikipedia
from rich.console import Console
from rich.panel import Panel
import pyttsx3
import speech_recognition as sr

# Initialize the console
console = Console()

# Print a nice title using Rich
console.print(
    Panel.fit(
        "   =====   Jarvis Wikipedia   =====   ",
        style="bold blue",
        subtitle="By Python Triumph"
    )
)

# Define the commands
commands = """
[bold cyan]Commands:[/bold cyan]
1. "Wikipedia" to start a search.
2. "quit" to exit the program.
"""

# Print out the commands at the start of the program
console.print(commands)

class WikipediaApp:
    def __init__(self):
        pass
    
    def get_wikipedia(self):
        """
        Search Wikipedia using voice input after the command "Wikipedia"
        """
        try:
            # Initialize speech recognition
            r = sr.Recognizer()
            with sr.Microphone() as source:
                console.print("[bold blue]\nWaiting for command. . .[/bold blue]")
                audio = r.listen(source)

            try:
                # Recognize speech input
                command = r.recognize_google(audio)
                if command.lower() == "quit":
                    console.print("[bold cyan]Jarvis shutting down . . .\n Goodbye![/bold cyan]")
                    exit()
                elif command.lower() == "wikipedia":
                    # Echo the user's command
                    console.print(f"[bold blue]Command received: {command.capitalize()}[/bold blue]")
                    # Initialize text-to-speech engine
                    engine = pyttsx3.init()
                    # Prompt user to speak search term
                    engine.say("What would you like to search on Wikipedia?")
                    engine.runAndWait()

                    # Listen for the search term
                    with sr.Microphone() as source:
                        console.print("[bold blue]\nSpeak your search term >> [/bold blue]")
                        audio = r.listen(source)

                    # Recognize speech input for search term
                    try:
                        query = r.recognize_google(audio)
                        # Get Wikipedia summary based on user input
                        self._summary = wikipedia.summary(query, sentences=3)
                    
                    # Handle exceptions
                    except sr.UnknownValueError:
                        console.print("[bold red]Sorry, I could not understand the search term. Please try again.[/bold red]")
                else:
                    console.print("[bold red]Invalid command. Please say 'Wikipedia' to start a search or 'quit' to exit.[/bold red]")
            except sr.UnknownValueError:
                console.print("[bold red]Sorry, I could not understand the command. Please try again.[/bold red]")

        except Exception as e:
            # Handle exceptions
            console.print("[red]Error: {}[/red]".format(e))
            console.print("[red]Try a different search term or check your internet connection.[/red]")

    def display_wikipedia(self):
        """
        Display Wikipedia search results
        """
        # Display search result
        console.print("[bold blue]\nResult >> [/bold blue]", self._summary)
        
        # Initialize text to speech engine
        engine = pyttsx3.init()
        # Say the Wikipedia summary
        engine.say(self._summary)
        engine.runAndWait()

# Create a Jarvis program object
wikipedia_app = WikipediaApp()

while True:
    # Execute Wikipedia search and display
    wikipedia_app.get_wikipedia()
    wikipedia_app.display_wikipedia()