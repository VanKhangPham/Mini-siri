import logging

logger = logging.getLogger(__name__)

INTENTS = {
    "greeting": {
        "keywords": ["hello", "hi", "xin chào", "chào"],
        "response": "Hello my friend! What can I help you with?"
    },
    "time": {
        "keywords": ["what time", "current time", "mấy giờ", "giờ bao nhiêu"],
        "response": None  # Xử lý dynamic
    },
    "date": {
        "keywords": ["what is today", "today date", "ngày mai", "hôm nay"],
        "response": None
    },
    "google_search": {
        "keywords": ["google", "search", "tìm kiếm"],
        "response": None
    },
    "youtube_search": {
        "keywords": ["youtube", "video"],
        "response": None
    },
    "goodbye": {
        "keywords": ["bye", "goodbye", "see you", "tạm biệt"],
        "response": "Goodbye my friend! See you soon."
    },
    "help": {
        "keywords": ["help", "what can you do", "abilities"],
        "response": None
    }
}

class IntentParser:
    def parse(self, user_input):
        """Phân tích intent từ input"""
        for intent_name, intent_data in INTENTS.items():
            for keyword in intent_data["keywords"]:
                if keyword in user_input:
                    logger.info(f"Detected intent: {intent_name}")
                    return intent_name, intent_data
        
        logger.warning(f"Unknown intent: {user_input}")
        return "unknown", None