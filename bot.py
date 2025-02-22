from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# تعريف دالة لمعالجة أمر /start
def start(update: Update, context: CallbackContext) -> None:
    user = update.effective_user
    update.message.reply_text(f"مرحبًا {user.first_name}! أنا بوتك. كيف يمكنني مساعدتك؟")

def main() -> None:
    # ضع توكن البوت الخاص بك هنا
    updater = Updater("7463755558:AAFuiOzMjwblpmD_SL1ZWOIwO7hZs1ISJD8")

    # الحصول على المنبه لمعالجة الأوامر
    dispatcher = updater.dispatcher

    # إضافة معالج للأمر /start
    dispatcher.add_handler(CommandHandler("start", start))

    # بدء البوت
    updater.start_polling()
    updater.idle()

if name == "main":
    main()
