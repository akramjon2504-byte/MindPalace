import asyncio
import logging
import os
from aiohttp import web
from aiohttp.web_request import Request
from aiogram import Bot, Dispatcher
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application
from handlers import setup_handlers

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Bot configuration
BOT_TOKEN = os.getenv("BOT_TOKEN", "your_bot_token_here").strip()
WEBHOOK_HOST = os.getenv("WEBHOOK_HOST", "https://your-app.onrender.com")
WEBHOOK_PATH = "/webhook"
WEBHOOK_URL = f"{WEBHOOK_HOST}{WEBHOOK_PATH}"
WEB_SERVER_HOST = "0.0.0.0"
WEB_SERVER_PORT = int(os.getenv("PORT", 8000))

# Initialize bot and dispatcher
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

async def on_startup():
    """Set webhook on startup"""
    try:
        await bot.set_webhook(url=WEBHOOK_URL)
        logger.info(f"Webhook set to {WEBHOOK_URL}")
    except Exception as e:
        logger.error(f"Failed to set webhook: {e}")

async def on_shutdown():
    """Clean up on shutdown"""
    try:
        await bot.delete_webhook()
        await bot.session.close()
        logger.info("Bot session closed")
    except Exception as e:
        logger.error(f"Error during shutdown: {e}")

def create_app():
    """Create aiohttp application"""
    app = web.Application()
    
    # Setup webhook handler
    webhook_requests_handler = SimpleRequestHandler(
        dispatcher=dp,
        bot=bot
    )
    webhook_requests_handler.register(app, path=WEBHOOK_PATH)
    setup_application(app, dp, bot=bot)
    
    # Setup handlers
    setup_handlers(dp)
    
    return app

async def main():
    """Main function for local development"""
    setup_handlers(dp)
    
    try:
        await dp.start_polling(bot)
    except KeyboardInterrupt:
        logger.info("Bot stopped by user")
    finally:
        await bot.session.close()

if __name__ == "__main__":
    if os.getenv("ENVIRONMENT") == "production":
        # Production mode with webhook
        app = create_app()
        
        # Set webhook on startup
        asyncio.get_event_loop().run_until_complete(on_startup())
        
        # Start web server
        web.run_app(
            app,
            host=WEB_SERVER_HOST,
            port=WEB_SERVER_PORT
        )
    else:
        # Development mode with polling
        asyncio.run(main())
