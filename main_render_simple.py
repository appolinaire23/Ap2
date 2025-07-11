"""
Point d'entrée SIMPLE pour le déploiement Render.com
Version simplifiée sans dépendances complexes
"""

import os
import sys
import asyncio
from dotenv import load_dotenv

# Charger les variables d'environnement
load_dotenv()

# Configuration
API_ID = int(os.getenv('API_ID', '29177661'))
API_HASH = os.getenv('API_HASH', 'a8639172fa8d35dbfd8ea46286d349ab')
BOT_TOKEN = os.getenv('BOT_TOKEN', '8168829272:AAEdBli_8E0Du_uHVTGLRLCN6KV7Gwox0WQ')
ADMIN_ID = int(os.getenv('ADMIN_ID', '1190237801'))

async def main():
    """Fonction principale simple"""
    try:
        print("🌐 Démarrage TeleFeed Bot sur Render.com")
        print(f"✅ API_ID: {API_ID}")
        print(f"✅ BOT_TOKEN: {BOT_TOKEN[:20]}...")
        print(f"✅ ADMIN_ID: {ADMIN_ID}")

        # Import et démarrage du bot
        from telethon import TelegramClient, events
        from bot.handlers import (
            start, valide, payer, deposer, connect, redirection, 
            transformation, whitelist, blacklist, chats, help_command,
            admin_command, confirm_command, generate_command, 
            users_command, stats_command, sessions_command, 
            handle_unknown_command
        )
        
        # Créer le client
        client = TelegramClient('bot', API_ID, API_HASH)
        
        # Démarrer le bot
        await client.start(bot_token=BOT_TOKEN)
        print("🚀 Bot TeleFeed démarré avec succès!")
        
        # Enregistrer les handlers
        client.add_event_handler(start, events.NewMessage(pattern='/start'))
        client.add_event_handler(valide, events.NewMessage(pattern='/valide'))
        client.add_event_handler(payer, events.NewMessage(pattern='/payer'))
        client.add_event_handler(deposer, events.NewMessage(pattern='/deposer'))
        client.add_event_handler(connect, events.NewMessage(pattern='/connect'))
        client.add_event_handler(redirection, events.NewMessage(pattern='/redirection'))
        client.add_event_handler(transformation, events.NewMessage(pattern='/transformation'))
        client.add_event_handler(whitelist, events.NewMessage(pattern='/whitelist'))
        client.add_event_handler(blacklist, events.NewMessage(pattern='/blacklist'))
        client.add_event_handler(chats, events.NewMessage(pattern='/chats'))
        client.add_event_handler(help_command, events.NewMessage(pattern='/help'))
        client.add_event_handler(admin_command, events.NewMessage(pattern='/admin'))
        client.add_event_handler(confirm_command, events.NewMessage(pattern='/confirm'))
        client.add_event_handler(generate_command, events.NewMessage(pattern='/generate'))
        client.add_event_handler(users_command, events.NewMessage(pattern='/users'))
        client.add_event_handler(stats_command, events.NewMessage(pattern='/stats'))
        client.add_event_handler(sessions_command, events.NewMessage(pattern='/sessions'))
        client.add_event_handler(handle_unknown_command, events.NewMessage)
        
        # Démarrer la restauration des redirections
        try:
            from bot.simple_restorer import SimpleRedirectionRestorer
            restorer = SimpleRedirectionRestorer()
            asyncio.create_task(restorer.start_restoration())
            print("🔄 Système de restauration des redirections activé")
        except Exception as e:
            print(f"⚠️ Erreur restauration redirections: {e}")
        
        # Exécuter le bot
        await client.run_until_disconnected()
        
    except Exception as e:
        print(f"❌ Erreur: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # Configuration variables d'environnement
    os.environ['RENDER_DEPLOYMENT'] = 'true'
    
    print("✅ Démarrage Render.com")
    
    # Exécuter
    asyncio.run(main())