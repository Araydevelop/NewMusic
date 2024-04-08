from pyrogram.types import InlineKeyboardButton

def start_panel(owner_id, support_chat_link, support_channel_link):
    buttons = [
        [
            InlineKeyboardButton(
                text="Add me to group or channel",
                url=f"https://t.me/YourBotUsername?startgroup=true"
            )
        ],
        [
            InlineKeyboardButton(
                text=f"Owner: {owner_id}",
                url=f"https://t.me/{owner_id}"
            )
        ],
        [
            InlineKeyboardButton(
                text="Support Chat",
                url=support_chat_link
            )
        ],
        [
            InlineKeyboardButton(
                text="Support Channel",
                url=support_channel_link
            )
        ]
    ]
    return buttons

# Example usage:
owner_id = "OwnerTelegramID"
support_chat_link = "https://t.me/YourSupportChat"
support_channel_link = "https://t.me/YourSupportChannel"

keyboard = start_panel(owner_id, support_chat_link, support_channel_link)
   
