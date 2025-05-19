import asyncio
import re
from patterns import genesis_patterns
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

bot = Bot("7777976395:AAGVA_CO8NiyR9UIen1NEutZgBTsBSLoX0w")
dp = Dispatcher()

CHAT_ID = -1002662619525  # Ваш ID группы
TOPIC_ID = 2  # ID топика


@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer("Перешлите мне сообщение, и я отправлю его в топик!")

@dp.message()
async def handle_forwards(message: types.Message):
    print(message)
    if message.forward_from or message.forward_from_chat:
        try:
            sender = (
                f"👤 {message.forward_from.full_name}"
                if message.forward_from
                else f"📢 {message.forward_from_chat.title}"
            )

            print(sender)

            # await bot.send_message(
            #     chat_id=CHAT_ID,
            #     message_thread_id=TOPIC_ID,
            #     text=message.text
            # )

            print(message.text)
            text = message.text
            for pattern in genesis_patterns:
                if pattern in text:
                    print(pattern)
                    cleaned_text = re.sub(pattern=pattern, repl="", string=text).strip()

            print(cleaned_text)

            await bot.send_message(
                chat_id=CHAT_ID,
                message_thread_id=TOPIC_ID,
                text=cleaned_text
            )

            await message.answer("✅ Готово!")
        except Exception as e:
            await message.answer(f"❌ Ошибка: {e}")
    else:
        await message.answer("Это не пересланное сообщение!")

asyncio.run(dp.start_polling(bot))