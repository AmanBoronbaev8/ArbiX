import args
from pyrogram.types import Message
from pyrogram import Client, filters

API_HASH = args.APIH
API_ID = args.APII

GROUP_ID = args.GROUP_ID
CHANNEL_ID = args.CHANNEL_ID
GROUP_TOPIC_IDS = args.GROUP_TOPIC_IDS
CHANNEL_TOPIC_IDS = args.CHANNEL_TOPIC_IDS

app = Client("my_session", api_id=API_ID, api_hash=API_HASH)

@app.on_message(filters.chat(chats=GROUP_ID) & filters.topic(GROUP_TOPIC_IDS[0]))
async def forward_new_messages(client: app, message: Message):
    message_id = message.id
    await app.forward_messages(from_chat_id=GROUP_ID, message_ids=message_id, chat_id=CHANNEL_ID, message_thread_id=CHANNEL_TOPIC_IDS[0])

@app.on_message(filters.chat(chats=GROUP_ID) & filters.topic(GROUP_TOPIC_IDS[1]))
async def forward_new_messages1(client: app, message: Message):
    message_id = message.id
    await app.forward_messages(from_chat_id=GROUP_ID, message_ids=message_id, chat_id=CHANNEL_ID, message_thread_id=CHANNEL_TOPIC_IDS[1])

@app.on_message(filters.chat(chats=GROUP_ID) & filters.topic(GROUP_TOPIC_IDS[2]))
async def forward_new_messages2(client: app, message: Message):
    message_id = message.id
    await app.forward_messages(from_chat_id=GROUP_ID, message_ids=message_id, chat_id=CHANNEL_ID, message_thread_id=CHANNEL_TOPIC_IDS[2])

@app.on_message(filters.chat(chats=GROUP_ID) & filters.topic(GROUP_TOPIC_IDS[3]))
async def forward_new_messages3(client: app, message: Message):
    message_id = message.id
    await app.forward_messages(from_chat_id=GROUP_ID, message_ids=message_id, chat_id=CHANNEL_ID, message_thread_id=CHANNEL_TOPIC_IDS[3])

@app.on_message(filters.chat(chats=GROUP_ID) & filters.topic(GROUP_TOPIC_IDS[4]))
async def forward_new_messages4(client: app, message: Message):
    message_id = message.id
    await app.forward_messages(from_chat_id=GROUP_ID, message_ids=message_id, chat_id=CHANNEL_ID, message_thread_id=CHANNEL_TOPIC_IDS[4])

@app.on_message(filters.chat(chats=GROUP_ID) & filters.topic(GROUP_TOPIC_IDS[5]))
async def forward_new_messages5(client: app, message: Message):
    message_id = message.id
    await app.forward_messages(from_chat_id=GROUP_ID, message_ids=message_id, chat_id=CHANNEL_ID, message_thread_id=CHANNEL_TOPIC_IDS[5])

@app.on_message(filters.chat(chats=GROUP_ID) & filters.topic(GROUP_TOPIC_IDS[6]))
async def forward_new_messages6(client: app, message: Message):
    message_id = message.id

@app.on_message(filters.chat(chats=GROUP_ID) & filters.topic(GROUP_TOPIC_IDS[7]))
async def forward_new_messages7(client: app, message: Message):
    message_id = message.id
    await app.forward_messages(from_chat_id=GROUP_ID, message_ids=message_id, chat_id=CHANNEL_ID, message_thread_id=CHANNEL_TOPIC_IDS[7])

@app.on_message(filters.chat(chats=GROUP_ID) & filters.topic(GROUP_TOPIC_IDS[8]))
async def forward_new_messages8(client: app, message: Message):
    message_id = message.id
    await app.forward_messages(from_chat_id=GROUP_ID, message_ids=message_id, chat_id=CHANNEL_ID, message_thread_id=CHANNEL_TOPIC_IDS[8])

@app.on_message(filters.chat(chats=GROUP_ID) & filters.topic(GROUP_TOPIC_IDS[9]))
async def forward_new_messages9(client: app, message: Message):
    message_id = message.id
    await app.forward_messages(from_chat_id=GROUP_ID, message_ids=message_id, chat_id=CHANNEL_ID, message_thread_id=CHANNEL_TOPIC_IDS[9])

@app.on_message(filters.chat(chats=GROUP_ID) & filters.topic(GROUP_TOPIC_IDS[10]))
async def forward_new_messages10(client: app, message: Message):
    message_id = message.id
    await app.forward_messages(from_chat_id=GROUP_ID, message_ids=message_id, chat_id=CHANNEL_ID, message_thread_id=CHANNEL_TOPIC_IDS[10])

@app.on_message(filters.chat(chats=GROUP_ID) & filters.topic(GROUP_TOPIC_IDS[11]))
async def forward_new_messages11(client: app, message: Message):
    message_id = message.id
    await app.forward_messages(from_chat_id=GROUP_ID, message_ids=message_id, chat_id=CHANNEL_ID, message_thread_id=CHANNEL_TOPIC_IDS[11])

@app.on_message(filters.chat(chats=GROUP_ID) & filters.topic(GROUP_TOPIC_IDS[12]))
async def forward_new_messages12(client: app, message: Message):
    message_id = message.id
    await app.forward_messages(from_chat_id=GROUP_ID, message_ids=message_id, chat_id=CHANNEL_ID, message_thread_id=CHANNEL_TOPIC_IDS[12])

@app.on_message(filters.chat(chats=GROUP_ID) & filters.topic(GROUP_TOPIC_IDS[13]))
async def forward_new_messages13(client: app, message: Message):
    message_id = message.id
    await app.forward_messages(from_chat_id=GROUP_ID, message_ids=message_id, chat_id=CHANNEL_ID, message_thread_id=CHANNEL_TOPIC_IDS[13])

@app.on_message(filters.chat(chats=GROUP_ID) & filters.topic(GROUP_TOPIC_IDS[14]))
async def forward_new_messages14(client: app, message: Message):
    message_id = message.id
    await app.forward_messages(from_chat_id=GROUP_ID, message_ids=message_id, chat_id=CHANNEL_ID, message_thread_id=CHANNEL_TOPIC_IDS[14])


app.run()
