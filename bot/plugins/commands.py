#!/usr/bin/env python3

# -*- coding: utf-8 -*-

# (c) @personal robot 



From pyrogram import filters, Client

From pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery

From bot import Translation # pylint: disable=import-error

From bot.database import Database # pylint: disable=import-error



Db = Database()



@Client.on_message(filters.command([“start”]) & filters.private, group=1)

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

                Caption = “Thankyou For Using Our Service Please Support And Share Our Channel And Group Link To Your Friends \n\n @agorimovies 👈\n @mv_mania 👈 \n @agorihome 👈\n @agoriseries 👈”,

              

                Parse_mode=”html”,

                Reply_to_message_id=update.message_id,

                Reply_markup=InlineKeyboardMarkup(

                    [

                        [

                            InlineKeyboardButton

                                (

                                    ‘📵 Developer 📵’, url=https://t.me/personal_privetbot1

                                )

                        ]

                    ]

                )

            )



        Elif file_type == “video”:

        

            Await bot.send_video(

                Chat_id=update.chat.id,

                Video = file_id,

                Caption = f”{file_name} \n @agorimovies \n @mv_mania \n @agorihome”,

                Parse_mode=”html”,

                Reply_markup=InlineKeyboardMarkup(

                    [

                        [

                            InlineKeyboardButton

                                (

                                    ‘💙 Developer 💙’, url=https://t.me/personal_privetbot1

                                )

                        ]

                    ]

                )

            )

            

        Elif file_type == “audio”:

        

            Await bot.send_audio(

                Chat_id=update.chat.id,

                Audio = file_id,

                Caption = f”{file_name} \n @agorimovies \n @mv_mania”,

                Parse_mode=”html”,

                Reply_markup=InlineKeyboardMarkup(

                    [

                        [

                            InlineKeyboardButton

                                (

                                    ‘🤗Developer🤗’, url=https://t.me/personal_privetbot1

                                )

                        ]

                    ]

                )

            )



        Else:

            Print(file_type)

        

        Return



    Buttons = [[

        InlineKeyboardButton(‘🤗Developers🤗’, url=’https://t.me/agorimovies’),

        InlineKeyboardButton(‘📃 Source Code 🧾’, url =’https://github.com/CrazyBotsz/Adv-Auto-Filter-Bot-V2’)

    ],[

        InlineKeyboardButton(‘Support 🛠’, url=’https://t.me/agorihome’)

    ],[

        InlineKeyboardButton(‘Help ⚙’, callback_data=”help”)

    ]]

    

    Reply_markup = InlineKeyboardMarkup(buttons)

    

    Await bot.send_message(

        Chat_id=update.chat.id,

        Text=Translation.START_TEXT.format(

                Update.from_user.first_name),

        Reply_markup=reply_markup,

        Parse_mode=”html”,

        Reply_to_message_id=update.message_id

    )





@Client.on_message(filters.command([“help”]) & filters.private, group=1)

Async def help(bot, update):

    Buttons = [[

        InlineKeyboardButton(‘Home ⚡’, callback_data=’start’),

        InlineKeyboardButton(‘About 🚩’, callback_data=’about’)

    ],[

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





@Client.on_message(filters.command([“about”]) & filters.private, group=1)

Async def about(bot, update):

    

    Buttons = [[

        InlineKeyboardButton(‘Home ⚡’, callback_data=’start’),

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

    

