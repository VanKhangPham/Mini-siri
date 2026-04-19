import logging
from datetime import date, datetime
import webbrowser as wb
from core.voice import VoiceEngine

logger = logging.getLogger(__name__)

class CommandHandler:
    def __init__(self, voice_engine: VoiceEngine):
        self.voice = voice_engine
    
    def handle(self, intent, user_input):
        """Xử lý lệnh dựa trên intent"""
        if intent == "greeting":
            self.voice.speak("Hello my friend!")
        
        elif intent == "time":
            now = datetime.now().strftime("%H hours %M minutes")
            self.voice.speak(f"It's {now}")
        
        elif intent == "date":
            today = date.today().strftime("%B %d, %Y")
            self.voice.speak(f"Today is {today}")
        
        elif intent == "google_search":
            self.voice.speak("What do you want to search?")
            query = self.voice.listen()
            if query:
                url = f"https://www.google.com/search?q={query}"
                wb.open(url)
                self.voice.speak(f"Searching Google for {query}")
        
        elif intent == "youtube_search":
            self.voice.speak("What video do you want?")
            query = self.voice.listen()
            if query:
                url = f"https://www.youtube.com/search?q={query}"
                wb.open(url)
                self.voice.speak(f"Searching YouTube for {query}")
        
        elif intent == "goodbye":
            self.voice.speak("Goodbye! See you soon!")
            return "EXIT"
        
        elif intent == "help":
            help_text = "I can search Google, YouTube, tell time, date, and say goodbye."
            self.voice.speak(help_text)
        
        else:
            self.voice.speak("I'm fine, thank you. And you?")
        
        return "CONTINUE"