# bot.py — Alpha Markets Signals Bot
# Install: pip install python-telegram-bot
# Host free on: railway.app or render.com

import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.environ.get("TOKEN")
FREE_CHANNEL = "https://t.me/WalleTrading1"
PAID_LINK_MONTHLY = "DM ME"
PAID_LINK_LIFETIME = "DM ME for questions, benefits and tailored setups"

async def start(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Welcome to Alpha Markets Signals!\n\n"
        "We cover TWO markets daily:\n"
        "₿ Crypto — BTC, ETH & high-potential alts\n"
        "📊 Stocks & CFDs — indices, tech, commodities\n\n"
        "Commands:\n"
        "/crypto - Latest crypto signals\n"
        "/stocks - Latest stock/CFD signals\n"
        "/performance - Our track record\n"
        "/subscribe - Join paid group\n"
        "/markets - What we're watching today\n"
        "/disclaimer - Risk warning\n"
        "/help - All commands"
    )

async def crypto(update, ctx):
    await update.message.reply_text(
        "₿ CRYPTO SIGNALS\n\n"
        "We cover: BTC, ETH, and select high-conviction altcoins.\n\n"
        "Free channel: 1–2 signals/week.\n"
        "Paid members: daily signals + live TP/SL updates.\n\n"
        f"Free channel: {FREE_CHANNEL}\n"
        f"Paid access: {PAID_LINK_MONTHLY}"
    )

async def stocks(update, ctx):
    await update.message.reply_text(
        "📊 STOCK / CFD SIGNALS\n\n"
        "We cover: US stocks (NVDA, TSLA, AAPL, general tech stocks & penny stocks), indices (SPX, US100, DAX), gold, oil.\n\n"
        "Signals sent 30 min before NY open daily.\n"
        "Paid members get pre-market briefings + intraday updates.\n\n"
        f"Free channel: {FREE_CHANNEL}\n"
        f"Paid access: {PAID_LINK_MONTHLY}"
    )

async def subscribe(update, ctx):
    await update.message.reply_text(
        "💎 MEMBERSHIP OPTIONS\n\n"
        "Monthly — $149/month\n"
        f"→ {PAID_LINK_MONTHLY}\n\n"
        "Lifetime — $1,200 (limited spots!)\n"
        f"→ {PAID_LINK_LIFETIME}\n\n"
        "Included:\n"
        "✅ Daily crypto signals (BTC, ETH, alts)\n"
        "✅ Daily stock & CFD setups\n"
        "✅ Entry, SL & TP on every signal\n"
        "✅ Live trade management updates\n"
        "✅ Pre-market briefings\n"
        "✅ Weekly performance recap\n"
        "✅ Direct Q&A access"
    )

async def performance(update, ctx):
    await update.message.reply_text(
        "📊 TRACK RECORD — Updated every Sunday\n\n"
        "This week:\n"
        "₿ Crypto: X signals | X% win rate\n"
        "📈 Stocks/CFD: X signals | X% win rate\n"
        "Combined: X% win rate\n\n"
        "⚠️ Past results do not guarantee future performance."
    )

async def markets(update, ctx):
    await update.message.reply_text(
        "🔍 MARKETS WE'RE WATCHING TODAY\n\n"
        "₿ Crypto: BTC, ETH — key levels in play\n"
        "📊 Stocks: update this daily\n"
        "📉 Indices: SPX, US100 — watching for breakout\n"
        "🪙 Commodities: Gold support zone\n\n"
        "Full analysis + signals in paid group.\n"
        f"→ {PAID_LINK_MONTHLY}"
    )

async def disclaimer(update, ctx):
    await update.message.reply_text(
        "⚠️ RISK DISCLAIMER\n\n"
        "All signals are for educational purposes only.\n"
        "Crypto and CFD trading involves significant risk.\n"
        "You can lose more than your initial investment.\n"
        "Never risk more than you can afford to lose.\n"
        "Always do your own research.\n\n"
        "This is NOT financial advice."
    )

async def help_cmd(update, ctx):
    await update.message.reply_text(
        "📋 ALL COMMANDS\n\n"
        "/start - Welcome & intro\n"
        "/crypto - Crypto signals info\n"
        "/stocks - Stock/CFD signals info\n"
        "/performance - Track record\n"
        "/subscribe - Pricing & payment\n"
        "/markets - Today's watchlist\n"
        "/disclaimer - Risk warning\n"
        "/help - This menu"
    )

app = ApplicationBuilder().token(TOKEN).build()
for cmd, fn in [
    ("start", start), ("crypto", crypto), ("stocks", stocks),
    ("subscribe", subscribe), ("performance", performance),
    ("markets", markets), ("disclaimer", disclaimer), ("help", help_cmd)
]:
    app.add_handler(CommandHandler(cmd, fn))

print("Alpha Markets Bot running...")
app.run_polling()
