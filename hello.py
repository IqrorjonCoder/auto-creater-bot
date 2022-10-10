from telegram import ReplyKeyboardRemove, ReplyKeyboardMarkup
from telegram.ext import ConversationHandler
from main import main
import os

state = {
    "turarjoy_raqami": 1,
    "guvohnoma_raqami": 2,
    "familiya": 3,
    "ism": 4,
    "ism_sharifi": 5,
    "xona_raqami": 6,
    "sana": 7,
    "rasm_id": 8,
    "tasdiqlash": 9,
}


def start_conversation(update, context):
    update.message.reply_text("*Turar-joy raqamini kiriting ?*", parse_mode="Markdown",
                              reply_markup=ReplyKeyboardRemove())
    return state["turarjoy_raqami"]


def turarjoy_raqami(update, context):
    context.user_data["turarjoy_raqami"] = update.message.text
    update.message.reply_text("*Guvohnoma raqamini kiriting ?*", parse_mode="Markdown",
                              reply_markup=ReplyKeyboardRemove())
    return state["guvohnoma_raqami"]


def guvohnoma_raqami(update, context):
    context.user_data["guvohnoma_raqami"] = update.message.text
    update.message.reply_text("*Familiangizni kiriting ?*", parse_mode="Markdown")
    return state["familiya"]


def familiya(update, context):
    context.user_data["familiya"] = update.message.text
    update.message.reply_text("*Ismingizni kiriting ?*", parse_mode="Markdown")
    return state["ism"]


def ism(update, context):
    context.user_data["ism"] = update.message.text
    update.message.reply_text("*Ism-sharifingizni kiriting ?*", parse_mode="Markdown")
    return state["ism_sharifi"]


def ism_sharifi(update, context):
    context.user_data["ism_sharifi"] = update.message.text
    update.message.reply_text("*Xona raqamini kiriting ?*", parse_mode="Markdown")
    return state["xona_raqami"]


def xona_raqami(update, context):
    context.user_data["xona_raqami"] = update.message.text
    update.message.reply_text("*Sanani kiriting ?*", parse_mode="Markdown")
    return state["sana"]


def sana(update, context):
    context.user_data["sana"] = update.message.text
    update.message.reply_text("*Rasmni yuboring ?*", parse_mode="Markdown")
    return state["rasm_id"]


def rasm(update, context):
    context.user_data["rasm_id"] = update.message.photo[0].file_unique_id
    context.user_data["rasm"] = update.message.photo[0].file_id

    update.message.reply_text("*Tasdiqlang !*", parse_mode="Markdown",
                              reply_markup=ReplyKeyboardMarkup([["Tasdiqlash ✅"],
                                                                ["Tasdiqlamaslik ❌"]]))
    return state["tasdiqlash"]


def tasdiqlash(update, context):
    if update.message.text == "Tasdiqlash ✅":
        file = context.user_data["rasm"]
        obj = context.bot.get_file(file)
        obj.download(f"./{context.user_data['rasm_id']}.jpg")


        main(context.user_data["rasm_id"],
             context.user_data["turarjoy_raqami"],
             context.user_data["guvohnoma_raqami"],
             context.user_data["familiya"],
             context.user_data["ism"],
             context.user_data["ism_sharifi"],
             context.user_data["xona_raqami"],
             context.user_data["sana"])

        i = 0
        while True:
            try:
                context.bot.delete_message(chat_id=update.message.chat_id, message_id=update.message.message_id - i)
                i += 1
            except:
                break
        update.message.reply_text("*Tasdiqlandi ✅✅✅*", parse_mode="Markdown", reply_markup=ReplyKeyboardMarkup([["📃 Guvohnoma yasash"]]))
        update.message.reply_photo(photo=open(f'./{context.user_data["rasm_id"]}_fully_saved_image.jpg', 'rb'))
        os.remove(f"./{context.user_data['rasm_id']}.jpg")
        os.remove(f"./{context.user_data['rasm_id']}_written.jpg")
        os.remove(f"./{context.user_data['rasm_id']}_fully_saved_image.jpg")

        return ConversationHandler.END
    else:
        i = 0
        while True:
            try:
                context.bot.delete_message(chat_id=update.message.chat_id, message_id=update.message.message_id - i)
                i += 1
            except:
                break
        update.message.reply_text("*Tasdiqlanmadi ❌❌❌*", parse_mode="Markdown",
                                  reply_markup=ReplyKeyboardMarkup([["📃 Guvohnoma yasash"]]))
        return ConversationHandler.END
