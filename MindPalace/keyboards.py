from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

def get_main_menu_keyboard() -> ReplyKeyboardMarkup:
    """Create main menu keyboard with Uzbek labels"""
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="📚 Yangi so'z o'rganish")],
            [KeyboardButton(text="🧠 Testni boshlash")],
            [KeyboardButton(text="📊 Statistika"), KeyboardButton(text="ℹ️ Yordam")]
        ],
        resize_keyboard=True,
        one_time_keyboard=False
    )
    return keyboard

def get_quiz_keyboard(options: list, question_id: str) -> InlineKeyboardMarkup:
    """Create inline keyboard for quiz questions"""
    keyboard = InlineKeyboardMarkup(inline_keyboard=[])
    
    # Add option buttons
    for i, option in enumerate(options):
        button = InlineKeyboardButton(
            text=f"{chr(65 + i)}) {option}",  # A), B), C), D)
            callback_data=f"q_{question_id}_{i}"  # Shortened callback data
        )
        keyboard.inline_keyboard.append([button])
    
    return keyboard

def get_continue_quiz_keyboard() -> InlineKeyboardMarkup:
    """Create keyboard for continuing or stopping quiz"""
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="➡️ Keyingi savol", callback_data="quiz_continue"),
            InlineKeyboardButton(text="🏁 Testni tugatish", callback_data="quiz_finish")
        ]
    ])
    return keyboard

def get_new_word_keyboard() -> InlineKeyboardMarkup:
    """Create keyboard for new word actions"""
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="🔄 Boshqa so'z", callback_data="new_word"),
            InlineKeyboardButton(text="🏠 Bosh menu", callback_data="main_menu")
        ]
    ])
    return keyboard
