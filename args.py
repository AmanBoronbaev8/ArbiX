from dotenv import load_dotenv
import os

load_dotenv()

APIH = os.getenv("API_HASH") #str
APII = int(os.getenv("API_ID")) #int
BT = os.getenv("BOT_TOKEN") #str

GROUP_ID = -1002361161091
GROUP_TOPIC_IDS = [9, 976, 1986, 2981, 65654, 63012, 17853, 96958, 28935, 79323, 65243, 3, 60756, 5, 736]

CHANNEL_ID = -1002612340392
CHANNEL_TOPIC_IDS = [8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36]