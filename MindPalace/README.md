# Intellekt Bot - English Learning Telegram Bot

An educational Telegram bot designed to help users learn English vocabulary with Uzbek translations. Features interactive learning with 530+ word pairs, multiple-choice quizzes, and complete Uzbek interface.

## Features

- 📚 **Learn New Words**: Display random English words with transcription and Uzbek translation
- 🧠 **Interactive Quizzes**: Multiple-choice questions to test vocabulary knowledge
- 📊 **Progress Tracking**: Score tracking and statistics for quiz performance
- 🇺🇿 **Uzbek Interface**: Complete user interface in Uzbek language
- 🤖 **User-Friendly**: Intuitive keyboard navigation and immediate feedback

## Tech Stack

- **Python 3.10+**
- **aiogram** - Modern Telegram Bot API framework
- **aiohttp** - Async HTTP server for webhooks
- **Render.com** - Deployment platform

## Setup Instructions

### 1. Create a Telegram Bot

1. Message [@BotFather](https://t.me/botfather) on Telegram
2. Send `/newbot` command
3. Follow the instructions to create your bot
4. Save the bot token you receive

### 2. Local Development

1. Clone the repository:
```bash
git clone https://github.com/yourusername/intellekt-bot.git
cd intellekt-bot
```

2. Install dependencies:
```bash
pip install aiogram aiohttp aiofiles
```

3. Set environment variable:
```bash
export BOT_TOKEN="your_bot_token_here"
```

4. Run the bot:
```bash
python main.py
```

### 3. Render.com Deployment

1. **Fork/Upload to GitHub**:
   - Upload your code to GitHub repository

2. **Create Render.com Account**:
   - Go to [render.com](https://render.com) and sign up

3. **Deploy Bot**:
   - Connect GitHub repository
   - Create "Web Service"
   - Set Environment Variables:
     - `BOT_TOKEN`: Your bot token from BotFather
     - `WEBHOOK_HOST`: `https://your-app-name.onrender.com`
     - `ENVIRONMENT`: `production`

4. **Automatic Deployment**:
   - Bot will automatically deploy using `render.yaml`
   - Webhook mode will be activated for production

## Bot Commands

- `/start` - Botni ishga tushirish va asosiy menuni ko'rsatish
- `/help` - Yordam ma'lumotlarini ko'rsatish  
- `/test` - Lug'at testini boshlash
- `/yangi_soz` - Yangi so'z o'rganish

## Vocabulary Categories

The bot includes 530+ words across categories:
- Body parts, Numbers, Days, Months
- Food, Animals, Clothing, Household items  
- Transport, Weather, Verbs, Adjectives
- Nature, Places, Professions, Technology
- Sports, Music, Emotions, Health, Education

## Current Bot

- **Bot ID**: 8393433620
- **Username**: [@ingliztilidatest_bot](https://t.me/ingliztilidatest_bot)
- **Name**: "Ingliz tilini o'rganish"
