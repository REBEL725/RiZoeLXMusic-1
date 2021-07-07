#RiZoeLXMusic

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import os
from RiZoeLXMusic.config import SOURCE_CODE
from RiZoeLXMusic.config import ASSISTANT_NAME
from RiZoeLXMusic.config import PROJECT_NAME
from RiZoeLXMusic.config import SUPPORT_GROUP
from RiZoeLXMusic.config import UPDATES_CHANNEL
class Messages():
      START_MSG = "**ʜɪ ᴛʜᴇʀᴇ 👋 [{}](tg://user?id={})!**\n\n☯︎ ɪ ᴀᴍ ᴀɴ ᴀᴅᴠᴀɴᴄᴇᴅ ʙᴏᴛ ᴄʀᴇᴀᴛᴇᴅ ғᴏʀ ᴘʟᴀʏɪɴɢ ᴍᴜsɪᴄ ɪɴ ᴛʜᴇ ᴠᴏɪᴄᴇ ᴄʜᴀᴛs ᴏғ ᴛᴇʟᴇɢʀᴀᴍ ɢʀᴏᴜᴘs & ᴄʜᴀɴɴᴇʟs.\n\n♡︎♥︎ 𝚜𝚎𝚗𝚍 𝚖𝚎 /help 𝚏𝚘𝚛 𝚖𝚘𝚛𝚎 𝚒𝚗𝚏𝚘."
      HELP_MSG = [
        ".",
f"""
**𝙷𝚎𝚢 👋 𝚆𝚎𝚕𝚌𝚘𝚖𝚎 𝚝𝚘 {PROJECT_NAME}

𒊹︎︎︎️ {PROJECT_NAME} ᴄᴀɴ ᴘʟᴀʏ ᴍᴜsɪᴄ ɪɴ ʏᴏᴜʀ ᴛᴇʟᴇɢʀᴀᴍ ɢʀᴏᴜᴘ's ᴠᴏɪᴄᴇ ᴄʜᴀᴛ ᴀs ᴡᴇʟʟ ᴀs ᴄʜᴀɴɴᴇʟ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ.

𒊹︎︎︎️ ᴀssɪsᴛᴀɴᴛ ➪ @{ASSISTANT_NAME}\n\nClick next for instructions**
""",

f"""
**setting up**

1) ᴍᴀᴋᴇ ʙᴏᴛ ᴀᴅᴍɪɴ (ɢʀᴏᴜᴘ ᴀɴᴅ ɪɴ ᴄʜᴀɴɴᴇʟ ɪғ ᴜsᴇ ᴄᴘʟᴀʏ)
2) sᴛᴀʀᴛ ᴀ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ
3) ᴛʀʏ /play <song name> ғᴏʀ ᴛʜᴇ ғɪʀsᴛ ᴛɪᴍᴇ ʙʏ ᴀɴ ᴀᴅᴍɪɴ
*) ɪғ ᴜsᴇʀʙᴏᴛ ᴊᴏɪɴᴇᴅ ᴇɴᴊᴏʏ ᴍᴜsɪᴄ, ɪғ ɴᴏᴛ ᴀᴅᴅ @{ASSISTANT_NAME} ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ʙʏ ᴜsɪɴɢ ᴄᴍᴅ /userbotjoin ᴏʀ ᴀᴅᴅ ᴍᴀɴᴜᴀʟʏʏ.

**for channel Music play**
1) Make me admin of your channel 
2) Send /userbotjoinchannel in linked group
3) Now send commands in linked group
""",
f"""
**Commands**

**=>> Song Playing 🎧**

- /play: Play the requestd song
- /play [yt url] : Play the given yt url
- /play [reply yo audio]: Play replied audio
- /dplay: Play song via deezer
- /splay: Play song via jio saavn
- /ytplay: Directly play song via Youtube Music

**=>> Playback ⏯**

- /player: Open Settings menu of player
- /skip: Skips the current track
- /pause: Pause track
- /resume: Resumes the paused track
- /end: Stops media playback
- /current: Shows the current Playing track
- /playlist: Shows playlist

*Player cmd and all other cmds except /play, /current  and /playlist  are only for admins of the group.
""",

f"""
**=>> Channel Music Play 🛠**

𒊹︎︎︎ For linked group admins only:

- /cplay [song name] - play song you requested
- /cdplay [song name] - play song you requested via deezer
- /csplay [song name] - play song you requested via jio saavn
- /cplaylist - Show now playing list
- /cccurrent - Show now playing
- /cplayer - open music player settings panel
- /cpause - pause song play
- /cresume - resume song play
- /cskip - play next song
- /cend - stop music play
- /userbotjoinchannel - invite assistant to your chat

channel is also can be used instead of c ( /cplay = /channelplay )

𒊹︎︎︎ If you donlt like to play in linked group:

1) Get your channel ID.
2) Create a group with tittle: Channel Music: your_channel_id
3) Add bot as Channel admin with full perms
4) Add @{ASSISTANT_NAME} to the channel as an admin.
5) Simply send commands in your group. (remember to use /ytplay instead /play)
""",

f"""
**=>> More tools 🧑‍🔧**

- /musicplayer [on/off]: Enable/Disable Music player
- /admincache: Updates admin info of your group. Try if bot isn't recognize admin
- /userbotjoin: Invite @{ASSISTANT_NAME} Userbot to your chat
""",
f"""
**=>> Song Download 🎸**

- /video [song mame]: Download video song from youtube
- /song [song name]: Download audio song from youtube
- /saavn [song name]: Download song from saavn
- /deezer [song name]: Download song from deezer

**=>> Search Tools 📄**

- /search [song name]: Search youtube for songs
- /lyrics [song name]: Get song lyrics
""",

f"""
**=>> Commands for Sudo Users ⚔️**

 - /userbotleaveall - remove assistant from all chats
 - /broadcast <reply to message> - globally brodcast replied message to all chats
 - /pmpermit [on/off] - enable/disable pmpermit message
*Sudo Users can execute any command in any groups

"""
      ]
