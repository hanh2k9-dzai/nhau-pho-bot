import os
import logging
from threading import Thread
from http.server import HTTPServer, BaseHTTPRequestHandler
from telegram import Update, WebAppInfo, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# --- WEB SERVER ĐỂ RENDER HEALTH CHECK (CHỐNG TIMED OUT) ---
class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Bot Nhau Pho Simulator is Running Live!")

def run_health_check_server():
    port = int(os.environ.get("PORT", 8080))
    server = HTTPServer(('0.0.0.0', port), SimpleHTTPRequestHandler)
    print(f"🌐 Web Server dang chay tren port {port}...")
    server.serve_forever()

# --- MAIN BOT TELEGRAM ---
TOKEN = os.getenv("BOT_TOKEN", "8910844792:AAFCjZWeWikS4p3OOfE1QQcOOQ30Bvueo-U")

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_name = update.effective_user.first_name
    # Link Game GitHub Pages của sếp
    game_url = "https://hanh2k9-dzai.github.io/nhau-pho-bot/" 
    
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
    # Chạy Web Server ở luồng phụ (background thread) để Render không báo Timed Out
    Thread(target=run_health_check_server, daemon=True).start()
    
    # Chạy Telegram Bot
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("🚀 Bot Nhậu Phố Simulator đang chạy...")
    app.run_polling()
