# GitHub va Render.com ga Deploy qilish yo'riqnomasi

## 1. GitHub'ga yuklash

### Dastur kodini GitHub'ga yuklash:

1. **GitHub'da repository yarating**:
   - [GitHub.com](https://github.com) ga kiring
   - "New repository" tugmasini bosing
   - Repository nomi: `intellekt-bot`
   - Description: `Educational Telegram bot for English-Uzbek vocabulary learning`
   - Public yoki Private tanlang
   - "Create repository" tugmasini bosing

2. **Replit'dan fayllarni yuklab oling**:
   - Barcha loyiha fayllarini zip formatida yuklab oling
   - Yoki har bir faylni alohida nusxalab oling

3. **Fayllarni GitHub'ga yuklang**:
   - "uploading an existing file" havolasini bosing  
   - Quyidagi fayllarni yuklang:
     - `main.py`
     - `handlers.py` 
     - `keyboards.py`
     - `words_database.py`
     - `pyproject.toml`
     - `README.md`
     - `render.yaml`
     - `.gitignore`
     - `replit.md`

## 2. Render.com'ga Deploy qilish

### Render.com'da Web Service yaratish:

1. **Render.com'ga kiring**:
   - [Render.com](https://render.com) ga kiring
   - GitHub account bilan login qiling

2. **Web Service yarating**:
   - "New +" tugmasini bosing
   - "Web Service" ni tanlang
   - GitHub repository'ni tanlang (`intellekt-bot`)

3. **Service sozlamalari**:
   ```
   Name: intellekt-bot
   Environment: Python 3
   Build Command: pip install -r pyproject.toml
   Start Command: python main.py
   Plan: Free
   ```

4. **Environment Variables qo'shing**:
   ```
   BOT_TOKEN = sizning_bot_tokeningiz
   WEBHOOK_HOST = https://intellekt-bot.onrender.com
   ENVIRONMENT = production
   PORT = 8000
   ```

5. **Deploy tugmasini bosing**:
   - Bot avtomatik deploy bo'ladi
   - 5-10 daqiqa kutib turing

## 3. Bot tokenini yangilash

Deploy bo'lgandan keyin bot webhook rejimida ishlaydi:

1. **BotFather'da webhook o'rnating**:
   ```
   curl -X POST "https://api.telegram.org/bot<YOUR_BOT_TOKEN>/setWebhook?url=https://intellekt-bot.onrender.com/webhook"
   ```

2. **Webhook holatini tekshiring**:
   ```
   curl "https://api.telegram.org/bot<YOUR_BOT_TOKEN>/getWebhookInfo"
   ```

## 4. Test qilish

- Telegram'da botingizni toping: `@ingliztilidatest_bot`
- `/start` buyrug'ini yuboring
- Barcha funksiyalarni test qiling

## Muhim eslatmalar

- **Free plan**: Render.com free plan 15 daqiqadan keyin "sleep" rejimiga o'tadi
- **Cold start**: Birinchi request 30 soniya vaqt olishi mumkin  
- **Logs**: Render dashboard'dan log'larni kuzatishingiz mumkin
- **Custom domain**: Agar kerak bo'lsa, custom domain qo'shishingiz mumkin

## Xatoliklarni tuzatish

Agar bot ishlamasa:
1. Render logs'ni tekshiring
2. Environment variables'ni tekshiring  
3. Bot token to'g'ri ekanligi tekshiring
4. Webhook URL'i to'g'ri ekanligi tekshiring