# ➡️ Keyifle Kullanın Canlarım :)
import os
import heroku3
from telethon import TelegramClient, events, Button

#samilben
# 
api_id = 16571012
api_hash = "b4cb958074fb47640ec9bc0940333d13"
bot_token = "6351942473"

# Telethon 
client = TelegramClient('client', api_id, api_hash).start(bot_token=bot_token)
#
USERNAME = "cavresetiket"
log_qrup = -1001915718534
startmesaj = "\n\n• 𝖦𝗋𝗎𝖻𝗎𝗇𝗎𝗓𝖽𝖺𝗄𝗂 𝗇𝖾𝗋𝖽𝖾𝗒𝗌𝖾 𝗍𝗎𝗆 𝗎𝗒𝖾𝗅𝖾𝗋𝗂 𝖾𝗍𝗂𝗄𝖾𝗍𝗅𝖾𝗒𝖾𝖻𝗂𝗅𝗂𝗋𝗂𝗆 . . . • 𝖪𝗈𝗆𝗎𝗍𝗅𝖺𝗋 𝖻𝗎𝗍𝗈𝗇𝗎𝗇𝖺 𝗍𝗂𝗄𝗅𝖺𝗒𝗂𝗉 𝗍𝗎𝗆 𝗄𝗈𝗆𝗎𝗍𝗅𝖺𝗋𝗂 𝗈𝗀𝗋𝖾𝗇𝗂𝗇 . . ."
komutlar = "🇹🇷 𝖳𝗎𝗆 𝖪𝗈𝗆𝗎𝗍𝗅𝖺𝗋 ;\n\n» /utag   <  𝗆𝖾𝗌𝖺𝗃  >\n   - 𝖴𝗒𝖾𝗅𝖾𝗋𝗂 5'𝗅𝗂 𝖾𝗍𝗂𝗄𝖾𝗍𝗅𝖾𝗋 .\n\n» /tag   <  𝗆𝖾𝗌𝖺𝗃  >\n   - 𝖴𝗒𝖾𝗅𝖾𝗋𝗂 𝗍𝖾𝗄 𝗍𝖾𝗄 𝖾𝗍𝗂𝗄𝖾𝗍𝗅𝖾𝗋 .\n\n» /atag   <  𝗆𝖾𝗌𝖺𝗃  >\n   - 𝖸𝗈𝗇𝖾𝗍𝗂𝖼𝗂𝗅𝖾𝗋𝗂 𝖾𝗍𝗂𝗄𝖾𝗍𝗅𝖾𝗋 .\n\n» /etag   <  𝗆𝖾𝗌𝖺𝗃  >\n   - 𝖴𝗒𝖾𝗅𝖾𝗋𝗂 𝖾𝗆𝗈𝗃𝗂𝗅𝖾𝗋𝗅𝖾 𝖾𝗍𝗂𝗄𝖾𝗍𝗅𝖾𝗋 .\n\n» /stag   <  𝗆𝖾𝗌𝖺𝗃  >\n   - 𝖴𝗒𝖾𝗅𝖾𝗋𝗂 𝗀𝗎𝗓𝖾𝗅 𝗌𝗈𝗓𝗅𝖾𝗋𝗅𝖾 𝖾𝗍𝗂𝗄𝖾𝗍𝗅𝖾𝗋 .\n\n» /cancel =>\n   - 𝖤𝗍𝗂𝗄𝖾𝗍𝗅𝖾𝗆𝖾 𝗂𝗌𝗅𝖾𝗆𝗂𝗇𝗂 𝖽𝗎𝗋𝖽𝗎𝗋𝗎𝗋 ."
qrupstart = "• 𝖲𝗎𝖺𝗇 𝖠𝗄𝗍𝗂𝖿 𝖢𝖺𝗅𝗂𝗌𝗆𝖺𝗄𝗍𝖺𝗒𝗂𝗆 . . .\n\n• 𝖪𝗈𝗆𝗎𝗍𝗅𝖺𝗋𝗂 𝖦𝗈𝗋𝗆𝖾𝗄 𝗂𝖼𝗂𝗇 𝖡𝗈𝗍𝗎𝗇 𝗂𝖼𝖾𝗋𝗂𝗌𝗂𝗇𝖾 𝗀𝗂𝗋𝗂𝗉 𝖻𝖺𝗌𝗅𝖺𝗍𝗂𝗇 . . ."
support = "6351942473:AAF1gagdscrtwRlqxbOB8tfUb6Da-hS6ISw"
sahib = "rahatsizetmeyiniz34"
