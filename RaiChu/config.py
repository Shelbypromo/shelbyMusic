## Coder are here

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "AQC3G4E6EXiDIrrASsOxI2Abo6PJUvjFuirbn1HNby7CRO2n9TVC5naft9oDEtthmYTPKsoh4N7YgaN7PfSlbykuEIoT36AJbCDE7nnQ_QzwmFh3QKOe2UV7piiOG5-yIX0h0hWWKr8dLe2el1i6QfOrx67dNE6NrnDOQmFwLyayuyHqIjn0PR-zxZjmJhqP-zzTu5HwZX-X8LutjDBmmVkJ7aHjSH3WIo7p2YToOuqazMoAT5ZgvVg_QZ5hgnejnV5B1QsiBdmcVNmhz5ZuflPWN8HOCjq0RRGyfwq_KmHS9DYSWtyKHyS7ZcaDEBlDCJUMaa92XCc3y1lFITi4ByAAAAAUXFPIEA")
BOT_TOKEN = getenv("5783920500:AAGcj-xXhUKzRr9bsAbbE2yB24LMjHRyKpA
")
BOT_NAME = getenv("Newmusic")
API_ID = int(getenv("22651271")
API_HASH = getenv("b389a47046d273908229c18351849ea")
OWNER_NAME = getenv("OWNER_NAME", "theroombot")
ALIVE_NAME = getenv("ALIVE_NAME", "shelby")
ASSISTANT_USERNAME = getenv("ASSISTANT_USERNAME", "testiclf")
BOT_USERNAME = getenv("MusicshelbyBot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "candy")
GROUP_SUPPORT = getenv("https://t.me/+g60jQVAW3owzNjc1")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL")
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/c83b000f004f01897fe18.png")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/AMANTYA1/RaiChu-MusicV2")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/d6f92c979ad96b2031cba.png")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/6213d2673486beca02967.png")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/be5f551acb116292d15ec.png")
IMG_5 = getenv("IMG_5", "https://telegra.ph/file/c3401a572375b569138c3.png")
IMG_6 = getenv("IMG_6", "https://telegra.ph/file/d8f8fc1de9110b93ca94c.jpg")
YOUTUBE_IMG_URL = getenv("YOUTUBE_IMG_URL", "https://telegra.ph/file/58da23d726b601dc3b18e.jpg")
