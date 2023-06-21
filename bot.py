import pandas as pd
from telegram import Update
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackContext


with open("token.txt", "r") as f:
    TOKEN = f.read()
    print("Il tuo token è", TOKEN)


def ordina_csv():
    csv_1 = pd.read_csv('data/cestini_bussolengo.csv', usecols=['id', 'lon', 'lat'])
    csv_2 = pd.read_csv('data/cestini_castelnuovo.csv', usecols=['id', 'lon', 'lat'])
    csv_3 = pd.read_csv('data/cestini_lazise.csv', usecols=['id', 'lon', 'lat'])
    csv_4 = pd.read_csv('data/cestini_mozzecane.csv', usecols=['id', 'lon', 'lat'])
    csv_5 = pd.read_csv('data/cestini_pastrengo.csv', usecols=['id', 'lon', 'lat'])
    csv_6 = pd.read_csv('data/cestini_pescantina.csv', usecols=['id', 'lon', 'lat'])
    csv_7 = pd.read_csv('data/cestini_sommacampagna.csv', usecols=['id', 'lon', 'lat'])
    csv_8 = pd.read_csv('data/cestini_sona.csv', usecols=['id', 'lon', 'lat'])
    csv_9 = pd.read_csv('data/cestini_valeggio.csv', usecols=['id', 'lon', 'lat'])
    csv_10 = pd.read_csv('data/cestini_vigasio.csv', usecols=['id', 'lon', 'lat'])
    csv_11 = pd.read_csv('data/cestini_villafranca.csv', usecols=['id', 'lon', 'lat'])

    datiCestini = pd.concat([csv_1, csv_2, csv_3, csv_4, csv_5, csv_6, csv_7, csv_8, csv_9, csv_10, csv_11, ])
    datiCestini.to_csv('data/datiCestino.csv', index = False)


async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text("""Comandi disponibili:
    /setlocation: metti il paese da dove vuoi cercare
    """)


async def setlocation(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton("bussolengo", url='http://umap.openstreetmap.fr/it/map/bussolengo_931583?scaleControl=false&miniMap=false&scrollWheelZoom=false&zoomControl=true&allowEdit=false&moreControl=true&searchControl=null&tilelayersControl=null&embedControl=null&datalayersControl=true&onLoadPanel=undefined&captionBar=false&captionMenus=true'),
                 InlineKeyboardButton("castelnuovo", url=''),
                 InlineKeyboardButton("lazise", url='')],
                [InlineKeyboardButton("mozzecane", url=''),
                 InlineKeyboardButton("pastrengo", url=''),
                 InlineKeyboardButton("pescantina", url='')],
                [InlineKeyboardButton("sommacampagna", url=''),
                 InlineKeyboardButton("sona", url=''),
                 InlineKeyboardButton("valeggio", url='')],
                [InlineKeyboardButton("vigasio", url=''),
                 InlineKeyboardButton("villafranca", url='')]]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text('Seleziona un paese:', reply_markup=reply_markup)


def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("help", help))
    app.add_handler(CommandHandler("setlocation", setlocation))
    app.run_polling()


if __name__ == '__main__':
    ordina_csv()
    main()