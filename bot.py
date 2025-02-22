from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import os

# تعريف دالة معالجة أمر /start
def start(update: Update, context: CallbackContext) -> None:
    # إرسال رسالة الترحيب مع إيموجي يد
    update.message.reply_text("مرحبا بكم 👋")

def main() -> None:
    # الحصول على التوكن من متغيرات البيئة (آمن أكثر)
    TOKEN = os.environ.get("7463755558:AAFuiOzMjwblpmD_SL1ZWOIwO7hZs1ISJD8")
    
    # إنشاء الكائنات الأساسية للبوت
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher
    
    # إضافة معالج لأمر /start
    dispatcher.add_handler(CommandHandler("start", start))
    
    # بدء استقبال التحديثات
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
