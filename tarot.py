import random
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

tarot_cards = [
    'Шут', 'Маг', 'Жрица', 'Императрица', 'Император', 'Иерофант',
    'Влюблённые', 'Колесница', 'Сила', 'Отшельник', 'Колесо Фортуны',
    'Справедливость', 'Повешенный', 'Смерть', 'Умеренность', 'Дьявол',
    'Башня', 'Звезда', 'Луна', 'Солнце', 'Суд', 'Мир'
]

def generate_random_cards(cards, num=3):
    return random.sample(cards, num)

async def get_tarot_reading(name, birthdate, question):
    past, present, future = generate_random_cards(tarot_cards)

    prompt = f"""
    Ты — опытный таролог. Пользователь: {name}, дата рождения: {birthdate}, вопрос: "{question}".

    Карты, которые выпали (прошлое-настоящее-будущее):
    Прошлое: «{past}»  
    Настоящее: «{present}»  
    Будущее: «{future}»

    Тон дружелюбный и радушный.
    Опиши подробно каждую карту в контексте вопроса, кратко подытожь общий смысл расклада и дай персональный совет или прогноз для {name}.
    """

    client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

    response = client.chat.completions.create(
        model="gpt-4.1-nano-2025-04-14",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content
