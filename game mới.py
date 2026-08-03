import os
import logging
from telegram import Update, WebAppInfo, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Lấy token từ biến môi trường (Environment Variable) trên Render
# Hoặc dùng mặc định nếu chưa cài đặt biến môi trường
TOKEN = os.getenv("BOT_TOKEN", "8910844792:AAE8x-e3UST4my-RhdQvBY-swhv9m8TGBVY")

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_name = update.effective_user.first_name
    
    # Nút mở Game Webview 2D (Sau này thay bằng link game thật)
    game_url = "https://google.com" 
    
    keyboard = [
        [InlineKeyboardButton("🍺 VÀO GAME NHẬU NGAY!", web_app=WebAppInfo(url=game_url))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        f"Chào sếp **{user_name}** đến với **Nhậu Phố Simulator**! 🍻\n\n"
        f"Hãy bấm nút bên dưới để mở quán và thách bia anh em vỉa hè ngay!",
        reply_markup=reply_markup,
        parse_mode="Markdown"
    )

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("🚀 Bot Nhậu Phố Simulator đang chạy...")
    app.run_polling()
