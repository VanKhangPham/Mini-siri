import os
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
LOGS_DIR = os.path.join(BASE_DIR, "logs")

os.makedirs(DATA_DIR, exist_ok = True)
os.makedirs(LOGS_DIR, exist_ok = True)

#voice
MICROPHONE_INDEX = None
SPEECH_RATE = 10
PHRASE_TIME_LIMIT = None

#TTS
TTS_VOICE_INDEX = 0 # 0=Nam, 1=Nữ
TTS_RATE = 150 #Tốc độ đọc

#Database
DB_PATH = os.path.join(DATA_DIR, "assistant.db")

#Logging
LOG_FILE = os.path.join(LOGS_DIR, f"log_{datetime.now().strftime('%Y%m%d')}.txt")

#Wake word
WAKE_WORD = "hey assistant"
