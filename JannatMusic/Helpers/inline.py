from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

import config
from JannatMusic import BOT_USERNAME

close_key = InlineKeyboardMarkup(
    [[InlineKeyboardButton(text="✯ ᴄʟᴏsᴇ ✯", callback_data="close")]]
)


buttons = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(text="▷", callback_data="resume_cb"),
            InlineKeyboardButton(text="II", callback_data="pause_cb"),
            InlineKeyboardButton(text="‣‣I", callback_data="skip_cb"),
            InlineKeyboardButton(text="▢", callback_data="end_cb"),
        ],
        [
            InlineKeyboardButton(text="✯ ᴄʟᴏsᴇ ✯", callback_data="close"),
        ],
    ]
)


pm_buttons = [
    [
        InlineKeyboardButton(
            text="ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        )
    ],
    [   
        InlineKeyboardButton(text="ᴄσммαи∂ѕ нєяє", callback_data="jannat_help"),
    ],
    [
        InlineKeyboardButton(text="ᴄʜᴀɴɴᴇʟ", url=config.SUPPORT_CHANNEL),
        InlineKeyboardButton(text="sᴜᴩᴩᴏʀᴛ", url="https://t.me/+hTILedqSqOo4MzI1"),
    ],
    [
        InlineKeyboardButton(
            text="sᴏᴜʀᴄᴇ", url="https://github.com/CodeLearning301/JannatMusic"
        ),
        InlineKeyboardButton(text="ᴅᴇᴠᴇʟᴏᴩᴇʀ", user_id=config.OWNER_ID),
    ],
]


gp_buttons = [
    [
        InlineKeyboardButton(
            text="ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        )
    ],
    [
        InlineKeyboardButton(text="ᴄʜᴀɴɴᴇʟ", url=config.SUPPORT_CHANNEL),
        InlineKeyboardButton(text="sᴜᴩᴩᴏʀᴛ", url=config.SUPPORT_CHAT),
    ],
    [
        InlineKeyboardButton(
            text="sᴏᴜʀᴄᴇ", url="https://github.com/CodeLearning301/JannatMusic"
        ),
        InlineKeyboardButton(text="ᴅᴇᴠᴇʟᴏᴩᴇʀ", user_id=config.OWNER_ID),
    ],
]


helpmenu = [
    [
        InlineKeyboardButton(text="ᴇᴠᴇʀʏᴏɴᴇ", callback_data="jannat_cb help"),
        
    ],
    [
        InlineKeyboardButton(text="sᴜᴅᴏ", callback_data="jannat_cb sudo"),
        InlineKeyboardButton(text="ᴏᴡɴᴇʀ", callback_data="jannat_cb owner"),
    ],
    [
        InlineKeyboardButton(text="ʙᴀᴄᴋ", callback_data="jannat_home"),
        InlineKeyboardButton(text="ᴄʟᴏsᴇ", callback_data="close"),
    ],
]


help_back = [
    [InlineKeyboardButton(text="sᴜᴩᴩᴏʀᴛ", url=config.SUPPORT_CHAT)],
    [
        InlineKeyboardButton(text="ʙᴀᴄᴋ", callback_data="jannat_help"),
        InlineKeyboardButton(text="ᴄʟᴏsᴇ", callback_data="close"),
    ],
]
