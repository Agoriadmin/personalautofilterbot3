#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @NO-ONE-KN0WS-ME
From pyrogram import filters
From pyrogram import Client as Mai_bOTs
From pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
From bot import Translation # pylint: disable=import-error
From bot.database import Database # pylint: disable=import-error
#from bot import ADMINS
Db = Database()
@Mai_bOTs.on_message(filters.command([“start”]) & filters.private, group=1)
Async def start(bot, update):
        Try:
        File_uid = update.command[1]
    Except IndexError:
        File_uid = False
      If file_uid:
        File_id, file_name, file_caption, file_type = await db.get_file(file_uid)
        
        If (file_id or file_type) == None:
            Return
        
        Caption = file_caption if file_caption != (“” or None) else (“<code>” + file_name + “</code>”)
        
        If file_type == “document”:
        
            Await bot.send_document(
                Chat_id=update.chat.id,
                Document = file_id,
                Caption = “Thankyou for join “,
                Parse_mode=”html”,
                Reply_to_message_id=update.message_id,
                Reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(‘𝑺𝑯𝑨𝑹𝑬♻️’, url=https://t.me/share/url?url=https%3A//t.me/agorimovies)
                ],
                [
                    
                ],
                [
                    InlineKeyboardButton(‘📵𝐀𝐆𝐆𝐑𝐎𝐔𝐏📵’, url=https://t.me/agorimovies ),
                    InlineKeyboardButton(‘⚠️𝐀𝐆𝐒𝐄𝐑𝐈𝐄𝐒⚠️’, url=https://t.me/agoriseries )
                ]
            ]
        )
    )

        Elif file_type == “video”:
                    Await bot.send_video(
                Chat_id=update.chat.id,
                Video = file_id,
                Caption = caption,
                Parse_mode=”html”,
                Reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(‘𝑺𝑯𝑨𝑹𝑬🌐’, url=https://t.me/share/url?url=https%3A//t.me/agorimovies)
                ],
                [
                     InlineKeyboardButton(‘💥𝐌𝐎𝐕𝐈𝐄 𝐑𝐄𝐐💥’, url=https://t.me/agorimovies ),
                    InlineKeyboardButton(‘♻️𝐖𝐄𝐁𝐒𝐄𝐑𝐈𝐄𝐒♻️’, url=https://t.me/agoriseries )
                ],
                [
                    InlineKeyboardButton(‘🔱𝐆𝐑𝐎𝐔𝐏🔱’, url=https://t.me/mv_mania),
                    InlineKeyboardButton(‘♻️𝐀𝐍𝐈𝐌𝐄♻️’, url=https://t.me/agkidsroom)
                ]
            ]
        )
    )
            
        Elif file_type == “audio”:
           Await bot.send_audio(
                Chat_id=update.chat.id,
                Audio = file_id,
                Caption = caption,
                Parse_mode=”html”,
                Reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(‘𝑺𝑯𝑨𝑹𝑬 🌐’, url=https://t.me/share/url?url=https%3A//t.me/agorimovies)
                ],
                [
                    InlineKeyboardButton(‘💥𝐌𝐎𝐕𝐈𝐄 𝐑𝐄𝐐💥’, url=https://t.me/agorimovies ),
                    InlineKeyboardButton(‘♻️𝐖𝐄𝐁𝐒𝐄𝐑𝐈𝐄𝐒♻️’, url=https://t.me/agoriseries )
                ],
                [
                    InlineKeyboardButton(‘🔱𝐆𝐑𝐎𝐔𝐏🔱’, url=https://t.me/mv_mania),
                    InlineKeyboardButton(‘♻️𝐀𝐍𝐈𝐌𝐄♻️’, url=https://t.me/agkidsroom)
                ]
            ]
        )
    )

        Else:
            Print(file_type)
        
        Return
    Await bot.send_photo(
        Chat_id=update.chat.id,
        Photo = ‘https://telegra.ph/file/23a25b4f0ec04aaf1946d.jpg’,
        Caption=Translation.START_TEXT.format(
                Update.from_user.first_name),
        Reply_markup=InlineKeyboardMarkup(
            [
                
                [
                    InlineKeyboardButton(‘💥𝐌𝐎𝐕𝐈𝐄 𝐑𝐄𝐐💥’, url=’https://t.me/agorimovies’),
                    InlineKeyboardButton(‘♻️𝐖𝐄𝐁𝐒𝐄𝐑𝐈𝐄𝐒♻️’, url =’https://t.me/Agoriseries)
                ],
                [
                    InlineKeyboardButton(‘♻️𝐀𝐍𝐈𝐌𝐄♻️’, url=’https://t.me/agkidsroom),
                    InlineKeyboardButton(‘🔱𝐆𝐑𝐎𝐔𝐏🔱’, url=’https://t.me/mv_mania')
                ]
            ]
        ), 
        Parse_mode=”html”, 
        Reply_to_message_id=update.message_id
    )


@Mai_bOTs.on_message(filters.command([“help”]) & filters.private, group=1)
Async def help(bot, update):
    Buttons = [[
        InlineKeyboardButton(‘Close 🔐’, callback_data=’close’)
    ]]
        Reply_markup = InlineKeyboardMarkup(buttons)
        Await bot.send_message(
        Chat_id=update.chat.id,
        Text=Translation.HELP_TEXT,
        Reply_markup=reply_markup,
        Parse_mode=”html”,
        Reply_to_message_id=update.message_id
    )


@Mai_bOTs.on_message(filters.command([“about”]) & filters.private, group=1)
Async def about(bot, update):
        Buttons = [[
        InlineKeyboardButton(‘Close 🔐’, callback_data=’close’)
    ]]
    Reply_markup = InlineKeyboardMarkup(buttons)
        Await bot.send_message(
        Chat_id=update.chat.id,
        Text=Translation.ABOUT_TEXT,
        Reply_markup=reply_markup,
        Disable_web_page_preview=True,
        Parse_mode=”html”,
        Reply_to_message_id=update.message_id
    )

@Mai_bOTs.on_message(filters.text & ~ filters.command([“start”, “help”]) & filters.private & ~ filters.me)
Async def note(bot, update):
    Buttons = [[
        InlinekeyboardButton(‘MOVIE REQUEST 💥’, url=’https://t.me/agorimovies’)
    ],[
        InlineKeyboardButton(‘🏡 WEBSERIES CHANNEL’, url=’https://t.me/agoriseries),
        InlineKeyboardButton(‘📽️ ANIME CHANNEL’, url =’https://t.me/agkidsroom’)
    ],[
        InlineKeyboardButton(‘🤔𝙷𝙾𝚆 𝚃𝙾 𝚁𝙴𝚀?’, url=’https://t.me/c/1387634315/4’)
    ],[
        InlineKeyboardButton(‘𝚂𝙷𝙰𝚁𝙴 𝚃𝙾 𝚈𝙾𝚄𝚁 𝙵𝚁𝙸𝙴𝙽𝙳𝚂😍’, url=’https://t.me/cinemakottakafiles’)
    ]]
    
    Reply_markup = InlineKeyboardMarkup(buttons)
    
    Await bot.send_message(
        Chat_id=update.chat.id,
        Text=”എന്നെ ഉപയോഗിക്കുന്നതിനു നന്ദി😊.നിങ്ങൾക്ക് വേണ്ട പടങ്ങൾ @agorimovies എന്ന ഗ്രൂപ്പിൽ ചോദിച്ചാൽ മാത്രമേ കിട്ടുകയുള്ളൂ.\nഇവിടെ ചോദിച്ചു സമയം കളയണ്ട!🚶\n\nThank you for using me ❤️\nPlease Don’t Req For Movies Here.\nJoin Our @agorimovies Group And Req Your Movies There...🚶 “,
        Reply_markup=reply_markup,
        Parse_mode=”html”,
        Reply_to_message_id=update.message_id
    )
