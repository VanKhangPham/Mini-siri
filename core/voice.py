import speech_recognition as sr
import pyttsx3
import logging
from config import *

logger = logging.getLogger(__name__)

class VoiceEngine:
    def __init__(self):
        self.recognizer = speech_recognition.Recognizer()
        self.speaker = pyttsx3.init()
        self._setup_voice()

    def _setup_voice(self):
        """Cấu hình giọng nói """
        voices = self.speaker.getProperty('voices')
        self.speaker.setProperty('voice', voices[TTS_VOICE_INDEX].id)
        self.speaker.setProperty('rate', TTS_RATE)

    def listen(self, timeout=SPEECH_TIMEOUT):
        """Chatbot nhận diện giọng nói"""
        try:
            with speech_recognition.Microphone() as mic:
                print("Chatbot đang lắng nghe...")
                self.recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = self.recognizer.listen(mic, timeout=timeout)

            print("Đang xử lý giọng nói...")
            text = self.recognizer.recognize_google(audio).lower()
            logger.info(f"Người dùng nói: {text}")
            return text
        except speech_recognition.UnknownValueError:
            msg = "Xin lỗi, tôi không hiểu. Bạn có thể nói rõ hơn hoặc một câu hỏi khác tương tự không?"
            logger.warning(msg)
            self.speak(msg)
            return ""
        
        except speech_recognition.RequestError as e:
            msg = "Lỗi kết nối Internet. Vui lòng kiểm tra kết nối."
            logger.error(f"STT Error: {e}")
            self.speak(msg)
            return ""
        
        except Exception as e:
            logger.error(f"Unexpected error: {e}")
            return ""
        
    def speak(self, text):
        """Chatbot nói"""
        print(f"Chatbot: {text}")
        self.speaker.say(text)
        self.speaker.runAndWait()
        logger.info(f"Chatbot nói: {text}")




        

