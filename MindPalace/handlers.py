import logging
from typing import Dict, Any
from aiogram import Dispatcher, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from typing import Union, cast
import uuid

from words_database import words_db
from keyboards import (
    get_main_menu_keyboard,
    get_quiz_keyboard,
    get_continue_quiz_keyboard,
    get_new_word_keyboard
)

# Configure logging
logger = logging.getLogger(__name__)

# States for quiz
class QuizStates(StatesGroup):
    waiting_for_answer = State()

# Store user scores and quiz data
user_data: Dict[int, Dict[str, Any]] = {}

def get_user_data(user_id: int) -> Dict[str, Any]:
    """Get or create user data"""
    if user_id not in user_data:
        user_data[user_id] = {
            "score": 0,
            "total_questions": 0,
            "current_question": None
        }
    return user_data[user_id]

async def start_command(message: Message, state: FSMContext):
    """Handle /start command"""
    await state.clear()
    user = message.from_user
    first_name = user.first_name if user and user.first_name else "Foydalanuvchi"
    
    welcome_text = (
        f"Assalomu alaykum, {first_name}! 👋\n\n"
        "🤖 Men **Intellekt Bot**man va sizga ingliz tilini o'rganishda yordam beraman!\n\n"
        "📚 **Imkoniyatlar:**\n"
        "• Yangi so'zlarni o'rganish\n"
        "• Bilimingizni test orqali sinash\n"
        "• O'rganish statistikangizni ko'rish\n\n"
        "Quyidagi tugmalardan birini tanlang:"
    )
    
    await message.answer(
        welcome_text,
        reply_markup=get_main_menu_keyboard(),
        parse_mode="Markdown"
    )

async def help_command(message: Message):
    """Handle /help command"""
    help_text = (
        "🤖 **Intellekt Bot Yordam**\n\n"
        "**Buyruqlar:**\n"
        "/start - Botni ishga tushirish\n"
        "/help - Yordam ma'lumotlari\n"
        "/yangi_soz - Yangi so'z o'rganish\n"
        "/test - Testni boshlash\n\n"
        "**Tugmalar:**\n"
        "📚 Yangi so'z o'rganish - Tasodifiy ingliz so'zini ko'rsatadi\n"
        "🧠 Testni boshlash - Ko'p tanlovli test boshlaydi\n"
        "📊 Statistika - Sizning natijalaringizni ko'rsatadi\n"
        "ℹ️ Yordam - Bu yordam xabarini ko'rsatadi\n\n"
        "Muvaffaqiyatlar! 🎯"
    )
    
    await message.answer(help_text, parse_mode="Markdown")

async def learn_new_word(message: Message):
    """Handle learning new word"""
    word_data = words_db.get_random_word()
    
    word_text = (
        f"📚 **Yangi so'z:**\n\n"
        f"🇬🇧 **Inglizcha:** {word_data['english'].title()}\n"
        f"🔊 **Talaffuz:** {word_data['transcription']}\n"
        f"🇺🇿 **O'zbekcha:** {word_data['uzbek'].title()}\n\n"
        f"Bu so'zni eslab qoling! 💡"
    )
    
    await message.answer(
        word_text,
        reply_markup=get_new_word_keyboard(),
        parse_mode="Markdown"
    )

async def start_quiz(message: Message, state: FSMContext):
    """Start quiz"""
    user_id = message.from_user.id if message.from_user else 0
    data = get_user_data(user_id)
    
    # Reset quiz data
    data["score"] = 0
    data["total_questions"] = 0
    
    await message.answer(
        "🧠 **Test boshlandi!**\n\n"
        "Sizga ingliz so'zi beriladi, to'g'ri o'zbek tarjimasini tanlang.\n"
        "Omad! 🍀",
        parse_mode="Markdown"
    )
    
    await send_quiz_question(message, state)

async def send_quiz_question(message: Message, state: FSMContext):
    """Send a quiz question"""
    user_id = message.from_user.id if message.from_user else 0
    data = get_user_data(user_id)
    
    # Generate quiz question
    question_data = words_db.get_quiz_question()
    question_id = str(uuid.uuid4())[:8]
    
    # Store current question
    data["current_question"] = {
        "id": question_id,
        "correct_answer": question_data["correct_answer"],
        "english": question_data["english"],
        "options": question_data["options"]
    }
    
    question_text = (
        f"❓ **Savol {data['total_questions'] + 1}:**\n\n"
        f"🇬🇧 **{question_data['english'].title()}** /{question_data['transcription']}/\n\n"
        f"Bu so'zning o'zbek tilidagi ma'nosi qaysi?"
    )
    
    keyboard = get_quiz_keyboard(question_data["options"], question_id)
    
    await state.set_state(QuizStates.waiting_for_answer)
    await message.answer(
        question_text,
        reply_markup=keyboard,
        parse_mode="Markdown"
    )

async def handle_quiz_answer(callback: CallbackQuery, state: FSMContext):
    """Handle quiz answer"""
    user_id = callback.from_user.id if callback.from_user else 0
    data = get_user_data(user_id)
    
    # Parse callback data
    try:
        if callback.data:
            print(f"DEBUG: Callback data received: {callback.data}")
            _, question_id, option_index = callback.data.split("_", 2)
            option_index = int(option_index)
            print(f"DEBUG: Parsed - question_id: {question_id}, option_index: {option_index}")
        else:
            await callback.answer("Xatolik yuz berdi!")
            return
    except (ValueError, IndexError) as e:
        print(f"DEBUG: Parse error: {e}")
        await callback.answer("Xatolik yuz berdi!")
        return
    
    current_question = data.get("current_question")
    if not current_question or current_question["id"] != question_id:
        await callback.answer("Bu savol eskirgan!")
        return
    
    # Get the selected answer from options
    quiz_options = current_question.get("options", [])
    if option_index >= len(quiz_options):
        await callback.answer("Xatolik yuz berdi!")
        return
    
    selected_answer = quiz_options[option_index]
    correct_answer = current_question["correct_answer"]
    is_correct = selected_answer == correct_answer
    
    data["total_questions"] += 1
    if is_correct:
        data["score"] += 1
        feedback = "✅ **To'g'ri!** Ajoyib! 🎉"
    else:
        feedback = f"❌ **Xato!** To'g'ri javob: **{correct_answer}**"
    
    # Show score
    score_text = f"\n\n📊 **Natija:** {data['score']}/{data['total_questions']}"
    
    # Send a new message instead of editing to avoid type issues
    if callback.message:
        await callback.message.answer(
            f"❓ **Savol {data['total_questions']}:**\n\n{feedback}{score_text}",
            reply_markup=get_continue_quiz_keyboard(),
            parse_mode="Markdown"
        )
    
    await callback.answer()

async def handle_quiz_continue(callback: CallbackQuery, state: FSMContext):
    """Handle quiz continuation"""
    if callback.data == "quiz_continue" and callback.message:
        # Send new question as a new message
        new_message = await callback.message.answer("🔄 Keyingi savol tayyorlanmoqda...")
        await send_quiz_question(new_message, state)
    elif callback.data == "quiz_finish":
        await finish_quiz(callback, state)
    
    await callback.answer()

async def finish_quiz(callback: CallbackQuery, state: FSMContext):
    """Finish quiz and show results"""
    user_id = callback.from_user.id if callback.from_user else 0
    data = get_user_data(user_id)
    
    score = data["score"]
    total = data["total_questions"]
    percentage = (score / total * 100) if total > 0 else 0
    
    if percentage >= 80:
        grade = "A'lo! 🏆"
        emoji = "🎉"
    elif percentage >= 60:
        grade = "Yaxshi! 👍"
        emoji = "😊"
    elif percentage >= 40:
        grade = "O'rtacha 📚"
        emoji = "😐"
    else:
        grade = "Ko'proq mashq qiling 💪"
        emoji = "😔"
    
    result_text = (
        f"🏁 **Test yakunlandi!**\n\n"
        f"📊 **Sizning natijangiz:**\n"
        f"✅ To'g'ri javoblar: {score}\n"
        f"📝 Jami savollar: {total}\n"
        f"📈 Foiz: {percentage:.1f}%\n\n"
        f"{emoji} **Baho:** {grade}\n\n"
        f"Tabriklaymiz! Davom eting! 🚀"
    )
    
    await state.clear()
    if callback.message and hasattr(callback.message, 'edit_text'):
        # For callback messages, we need to send a new message instead
        await callback.message.answer(
            result_text,
            parse_mode="Markdown"
        )

async def show_statistics(message: Message):
    """Show user statistics"""
    user_id = message.from_user.id if message.from_user else 0
    data = get_user_data(user_id)
    
    if data["total_questions"] == 0:
        stats_text = (
            "📊 **Statistika**\n\n"
            "Siz hali test topshirmadingiz.\n"
            "Bilimingizni sinab ko'rish uchun test boshlang! 🧠"
        )
    else:
        percentage = (data["score"] / data["total_questions"] * 100)
        stats_text = (
            f"📊 **Sizning statistikangiz:**\n\n"
            f"✅ To'g'ri javoblar: {data['score']}\n"
            f"📝 Jami savollar: {data['total_questions']}\n"
            f"📈 Muvaffaqiyat foizi: {percentage:.1f}%\n\n"
            f"Davom eting va yanada yaxshi natijalar qo'lga kiriting! 💪"
        )
    
    await message.answer(stats_text, parse_mode="Markdown")

async def handle_new_word_callback(callback: CallbackQuery):
    """Handle new word callback"""
    if callback.data == "new_word":
        word_data = words_db.get_random_word()
        
        word_text = (
            f"📚 **Yangi so'z:**\n\n"
            f"🇬🇧 **Inglizcha:** {word_data['english'].title()}\n"
            f"🔊 **Talaffuz:** {word_data['transcription']}\n"
            f"🇺🇿 **O'zbekcha:** {word_data['uzbek'].title()}\n\n"
            f"Bu so'zni eslab qoling! 💡"
        )
        
        if callback.message:
            await callback.message.answer(
                word_text,
                reply_markup=get_new_word_keyboard(),
                parse_mode="Markdown"
            )
    elif callback.data == "main_menu":
        if callback.message and hasattr(callback.message, 'answer'):
            await callback.message.answer(
                "🏠 Bosh menyuga qaytdingiz.\nKerakli bo'limni tanlang:",
                reply_markup=get_main_menu_keyboard()
            )
    
    await callback.answer()

def setup_handlers(dp: Dispatcher):
    """Setup all handlers"""
    # Command handlers
    dp.message.register(start_command, CommandStart())
    dp.message.register(help_command, Command(commands=["help"]))
    dp.message.register(learn_new_word, Command(commands=["yangi_soz"]))
    dp.message.register(start_quiz, Command(commands=["test"]))
    
    # Text message handlers
    dp.message.register(learn_new_word, F.text == "📚 Yangi so'z o'rganish")
    dp.message.register(start_quiz, F.text == "🧠 Testni boshlash")
    dp.message.register(show_statistics, F.text == "📊 Statistika")
    dp.message.register(help_command, F.text == "ℹ️ Yordam")
    
    # Callback handlers
    dp.callback_query.register(handle_quiz_answer, F.data.startswith("q_"))
    dp.callback_query.register(handle_quiz_continue, F.data.in_(["quiz_continue", "quiz_finish"]))
    dp.callback_query.register(handle_new_word_callback, F.data.in_(["new_word", "main_menu"]))
