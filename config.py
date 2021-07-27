import logging
from os import environ
from dotenv import load_dotenv
load_dotenv()

"""
Backend: Discord
"""
BACKEND = "Discord"

"""Necessário o arquivo .env no formato:
TOKENDISCORD=<token>
onde <token> contém o valor obtido de
https://discord.com/developers/applications
"""
BOT_IDENTITY = {
    "token": environ.get("TOKENDISCORD")
}
BOT_ADMINS = (environ.get("BOT_ADMIN"), )

"""
Prefixo do bot
"""
BOT_PREFIX = "!"
BOT_PREFIX_OPTIONAL_ON_CHAT = True

"""
Diretórios do Errbot
"""
BOT_DATA_DIR = r"data"
BOT_EXTRA_PLUGIN_DIR = r"plugins"
BOT_EXTRA_BACKEND_DIR = r"backends"

"""
Se os plugins têm dependências, usar ambiente virtual e requirements.txt
"""
AUTOINSTALL_DEPS = True

"""
Log
"""
BOT_LOG_FILE = r"errbot.log"
BOT_LOG_LEVEL = logging.DEBUG