# Overview

Intellekt Bot is a Telegram-based educational application designed to help users learn English vocabulary with Uzbek translations. The bot provides an interactive learning experience through vocabulary display and multiple-choice quizzes, with complete user interface in Uzbek language. It tracks user progress and provides immediate feedback to enhance the learning process.

# User Preferences

Preferred communication style: Simple, everyday language.

# System Architecture

## Bot Framework Architecture
The application uses aiogram, a modern asynchronous Python framework for Telegram Bot API, providing efficient handling of concurrent user interactions. The bot operates through webhook-based communication with Telegram servers for real-time message processing.

## Deployment Strategy
The bot is designed for deployment on Render.com using aiohttp web server for webhook handling. This approach enables scalable, cloud-based operation with automatic webhook management and proper lifecycle handling (startup/shutdown procedures).

## State Management
User interactions are managed through aiogram's Finite State Machine (FSM) system, specifically implementing QuizStates for handling quiz flow. In-memory user data storage tracks individual user scores, question history, and progress statistics without requiring persistent database connections.

## Data Storage Design
The vocabulary database is implemented as a simple in-memory Python class (WordsDatabase) containing English-Uzbek word pairs with phonetic transcriptions. This lightweight approach ensures fast word retrieval and quiz generation while maintaining easy expandability for additional vocabulary.

## User Interface Architecture
The bot employs a dual keyboard system:
- ReplyKeyboardMarkup for main navigation (persistent menu buttons)
- InlineKeyboardMarkup for interactive elements (quiz options, continue/finish buttons)

This design provides intuitive navigation while maintaining clean message threads for educational content.

## Quiz System Design
The quiz mechanism generates multiple-choice questions by randomly selecting incorrect options from the vocabulary database alongside the correct answer. Each question receives a unique identifier for tracking user responses and preventing answer manipulation.

# External Dependencies

## Core Framework Dependencies
- **aiogram**: Modern Telegram Bot API framework for asynchronous bot development
- **aiohttp**: Asynchronous HTTP client/server for webhook handling and web server functionality

## Deployment Platform
- **Render.com**: Cloud platform for hosting the webhook server with automatic deployment and environment variable management

## Telegram Bot API
- **Telegram Bot API**: Primary communication interface requiring bot token authentication and webhook URL configuration for real-time message processing

## Runtime Environment
- **Python 3.10+**: Required runtime environment with support for modern async/await patterns and type hints used throughout the application