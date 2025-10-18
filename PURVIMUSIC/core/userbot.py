import logging
from pyrogram import Client
import config

logger = logging.getLogger(__name__)

assistants = []
assistantids = []

class Userbot:
    def init(self):
        self.one = Client("Devineassistant1", api_id=config.API_ID, api_hash=config.API_HASH,
                          session_string=str(config.STRING1), no_updates=True)
        self.two = Client("Devineassistant2", api_id=config.API_ID, api_hash=config.API_HASH,
                          session_string=str(config.STRING2), no_updates=True)
        self.three = Client("Devineassistant3", api_id=config.API_ID, api_hash=config.API_HASH,
                            session_string=str(config.STRING3), no_updates=True)
        self.four = Client("Devineassistant4", api_id=config.API_ID, api_hash=config.API_HASH,
                           session_string=str(config.STRING4), no_updates=True)
        self.five = Client("Devineassistant5", api_id=config.API_ID, api_hash=config.API_HASH,
                           session_string=str(config.STRING5), no_updates=True)

    async def start(self):
        logger.info("Starting Assistants...")
        if config.STRING1:
            try:
                await self.one.start()
                await self.one.join_chat("As_cosmos")
                await self.one.join_chat("HXH_NETWORK")
                me = await self.one.get_me()
                self.one.id, self.one.username = me.id, me.username
                self.one.name = me.mention
                assistants.append(1); assistantids.append(self.one.id)
                await self.one.send_message("@zenitsu_xsupport", "<b>𝟷'sᴛ ᴀssɪsᴛᴀɴᴛ sᴛᴀʀᴛᴇᴅ</b>")
                logger.info(f"Assistant Started as {self.one.name}")
            except Exception as e:
                logger.warning(f"Warning: Failed to start Assistant 1 - {e}")

        if config.STRING2:
            try:
                await self.two.start()
                await self.two.join_chat("as_cosmos")
                await self.two.join_chat("hxh_network")
                me = await self.two.get_me()
                self.two.id, self.two.username = me.id, me.username
                self.two.name = me.mention
                assistants.append(2); assistantids.append(self.two.id)
                await self.two.send_message("@zenitsu_xsupport", "<b>𝟸ɴᴅ ᴀssɪsᴛᴀɴᴛ sᴛᴀʀᴛᴇᴅ</b>")
                logger.info(f"Assistant Two Started as {self.two.name}")
            except Exception as e:
                logger.warning(f"Warning: Failed to start Assistant 2 - {e}")

        if config.STRING3:
            try:
                await self.three.start()
                await self.three.join_chat("as_cosmos")
                await self.three.join_chat("hxh_network")
                me = await self.three.get_me()
                self.three.id, self.three.username = me.id, me.username
                self.three.name = me.mention
                assistants.append(3); assistantids.append(self.three.id)
                await self.three.send_message("@zenitsu_xsupport", "<b>𝟹ʀᴅ ᴀssɪsᴛᴀɴᴛ sᴛᴀʀᴛᴇᴅ</b>")
                logger.info(f"Assistant Three Started as {self.three.name}")
            except Exception as e:
                logger.warning(f"Warning: Failed to start Assistant 3 - {e}")

        if config.STRING4:
            try:
                await self.four.start()
                await self.four.join_chat("as_cosmos")
                await self.four.join_chat("hxh_network")
                me = await self.four.get_me()
                self.four.id, self.four.username = me.id, me.username
                self.four.name = me.mention
                assistants.append(4); assistantids.append(self.four.id)
                await self.four.send_message("@zenitsu_xsupport", "<b>𝟺ᴛʜ ᴀssɪsᴛᴀɴᴛ sᴛᴀʀᴛᴇᴅ</b>")
                logger.info(f"Assistant Four Started as {self.four.name}")
            except Exception as e:
                logger.warning(f"Warning: Failed to start Assistant 4 - {e}")
                
                if config.STRING5:
            try:
                await self.five.start()
                await self.five.join_chat("as_cosmos")
                await self.five.join_chat("hxh_network")
                me = await self.five.get_me()
                self.five.id, self.five.username = me.id, me.username
                self.five.name = me.mention
                assistants.append(5); assistantids.append(self.five.id)
                await self.five.send_message("@zenitsu_xsupport", "<b>𝟻ᴛʜ ᴀssɪsᴛᴀɴᴛ sᴛᴀʀᴛᴇᴅ</b>")
                logger.info(f"Assistant Five Started as {self.five.name}")
            except Exception as e:
                logger.warning(f"Warning: Failed to start Assistant 5 - {e}")

    async def stop(self):
        logger.info("Stopping Assistants...")
        try:
            if config.STRING1: await self.one.stop()
            if config.STRING2: await self.two.stop()
            if config.STRING3: await self.three.stop()
            if config.STRING4: await self.four.stop()
            if config.STRING5: await self.five.stop()
        except Exception as e:
            logger.warning(f"Warning: Failed to stop one or more assistants - {e}")
