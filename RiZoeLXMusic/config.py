# RiZoeLXMusic- Telegram bot project
# Copyright (C) 2021  RiZoeL
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
# Modified by Inukaasith

import os
from os import getenv

from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

que = {}
SESSION_NAME = getenv("SESSION_NAME", "BQBhqoLG52ELx6F7ETNbTawtWuoPeWhhcYZPd8F39A1CGcN_WaAw_BznDMx_TDXVhJcWObvsvVqIJ0LC8GNN4pJZgWOd78jittLxe-RgUe392yU3IiY_f9hVhTM9SfXaQPFfHqPELcSfHaKZDp7hJ2qC8nuRm4clOFvE6Qa-99sfQV_r27-7Upc4bwxwbC6jhfnL1NHMqcxyQgFv6KNIbcLn1bj2I1dDpqtdFjWJ6Jh7K2zvU5W4bq1CmefFWN3XU-8xG4zt2trGbHT0Kr_WFGM5RMCw1jhT9fYIPtwu-AB2jxnlP3x2XtfjPPD0XXhaB5qFwGZgS4pbk1Jn9JGA99XrZinaIAA")
BOT_TOKEN = getenv("BOT_TOKEN", "1897739843:AAE9ueAAdmP7ZxTkho2xwOgSAjVUXMTx0Uw")
BOT_NAME = getenv("BOT_NAME")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "REALVIBESn")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/e71ba08f40b9c8f5826f2.jpg")
admins = {}
API_ID = int(getenv("API_ID", "3989849"))
API_HASH = getenv("API_HASH", "a3384b30bcf31eb24ad597a526922084")
BOT_USERNAME = getenv("BOT_USERNAME", "RiZoeLvcBot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "RiZoeL_VC")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "DNHxHELL")
PROJECT_NAME = getenv("PROJECT_NAME", "RiZoeLXMusic")
SOURCE_CODE = getenv("SOURCE_CODE", "https://t.me/TheRiZoeL")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "120"))
ARQ_API_KEY = getenv("ARQ_API_KEY", "KFVWZW-YOEIQI-JVZVHS-GKQYLD-ARQ")
PMPERMIT = getenv("PMPERMIT", None)
LOG_GRP = getenv("LOG_GRP", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1517994352").split()))
