from PURVIMUSIC.core.bot import PURVI
from PURVIMUSIC.core.dir import dirr
from PURVIMUSIC.core.git import git
from PURVIMUSIC.core.userbot import Userbot
from PURVIMUSIC.misc import dbb, heroku

from SafoneAPI import SafoneAPI
from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = PURVI()
api = SafoneAPI()
userbot = Userbot(name="PURVIBOTS")



from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
