from flask import Flask
from aiogram import Bot, Dispatcher, types, executor
import requests, random, asyncio
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import os

app = Flask(__name__)

# Token del bot de Telegram
_token = '7217978134:AAHKzgbJqenKbwiXxblaLyXJziKrlRYHKcg'  # Reemplaza 'TU_TOKEN_AQUI' con tu token real
conex = Bot(_token, parse_mode='html')
rexa = Dispatcher(conex)

# ID del chat al que se enviarán los mensajes
chat_id = -1002153786640  # Reemplaza con el ID de tu chat

def rex(mix):
    def wrapper(func):
        _xix = rexa.message_handler(commands=[mix])(func)
        return _xix
    return wrapper

class Postresponse:
    def __init__(self, ccx: str = None):
        self.ccx = ccx

    def textMessage(self):
        ccx = self.ccx
        bina = self._binchk(ccx)
        _text = f"""<b>
NEW CARD!  [<code>{bina['bin']}</code>]

CARD NUMBER: <code>{ccx}</code>CARD EXTRA: <code>{bina['bin']}xxxx</code>

BIN: {bina['country_name']}|{bina['country_flag']}
𝙄𝙣𝙛𝙤 ≥ <code>{bina['brand']}</code> -  <code>{bina['level']}</code>
Banco : <code>{bina['bank']}</code>

BY : <code>@Gallegojgb2005 [0.{random.randint(1,100)}s]</code></b>"""
        return _text
    
    def _binchk(self, _chkb: int = None):
        try:
            response = requests.get(f'https://bins.antipublic.cc/bins/{_chkb}')
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Error al obtener el BIN: {e}")
            return {}

@rex('start')
async def start(msg: types.Message):
    botcmds = InlineKeyboardMarkup(row_width=2)
    botcmds.add(
        InlineKeyboardButton("𝗪𝗼𝗿𝗹𝗱𝘀𝗔𝗽𝗶𝘀「🐉」", url="https://t.me/Gallegojgb2005"),
        InlineKeyboardButton("Gallegojgb2005 ريكس🇮🇳 ", url="https://t.me/+573224658585")
    )

    print("Directorio actual:", os.getcwd())

    try:
        with open('ccs.txt') as archivo:
            x = archivo.readlines()
    except FileNotFoundError:
        await msg.reply("El archivo de tarjetas no se encuentra. Verifica que el archivo 'ccs.txt' esté en el mismo directorio que el script.")
        return
    except Exception as e:
        await msg.reply(f"Ocurrió un error al leer el archivo de tarjetas: {e}")
        return
    
    foto = 'https://i.imgur.com/ZEs9eij.mp4'
    for cc in x:
        text = Postresponse(cc.strip()).textMessage()
        try:
            await conex.send_video(chat_id=chat_id, caption=text, reply_markup=botcmds, video=foto)
            await asyncio.sleep(10)
        except Exception as e:
            print(f"Error al enviar el video: {e}")

print('_Onli : True...')
executor.start_polling(rexa)

# Ruta de Flask para que el servidor se mantenga activo
@app.route('/')
def home():
    return "El bot está en funcionamiento."

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
