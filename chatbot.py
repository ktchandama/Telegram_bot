# Importer les librairies
from telegram.ext import CommandHandler, Updater, MessageHandler, Filters

# Ajouter le token
TOKEN = "Insérer votre token par ici"

def start(update, context):
    update.message.reply_text("""Bienvenue chez TKL Consulting! Je suis Akossiwa et je suis chargé de vous guider!
    Voici les commandes disponibles:

    - /start  vous permet de lancer la conversation
    - /linkedin vous permet d'avoir le lien linkedin de TKL Consulting
    - /site vous permet d'avoir le site web de TKL Consulting
    - /help vous permet d'obtenir de l'aide
    """)

def linkedin(update, context):
    update.message.reply_text("https://www.linkedin.com/in/tklconsulting")

def site(update, context):
    update.message.reply_text("https://tklconsutingtg.com")

def incomprehension(update, context):
    update.message.reply_text("Désolé, je n'ai pas compris ce que vous voulez, veuillez réessayer une autre commande.")

def main():
    # Lire le token
    updater = Updater(TOKEN, use_context=True)

    # Avoir facilement accès au dispatcher
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("site", site))
    dp.add_handler(CommandHandler("incomprehension", incomprehension))

    # Gérer les messages qui ne sont pas des commandes
    dp.add_handler(MessageHandler(Filters.text, incomprehension))

    # Lancer le chatbot
    updater.start_polling()

    # Commande pour arrêter le bot avec "CTRL + C" à l'invite
    updater.idle()
    
if __name__ == "__main__":
    main()