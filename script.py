import feedparser
import requests
import json

# ضع رابط الـ Webhook الخاص بك هنا
WEBHOOK_URL = "https://discord.com/api/webhooks/1497337338358005882/BidfBI-pGOceKGD-i8AgzMOhP6B-zyNqcIwU0VsIX69Rd8HeJZ-5RVXAj7UeN-estXRc"
# رابط RSS (مثلاً Exploit-DB)
RSS_FEED_URL = "https://www.exploit-db.com/rss.xml"

def send_to_discord(entry):
    data = {
        "embeds": [{
            "title": entry.title,
            "description": entry.summary[:200] + "...",
            "url": entry.link,
            "color": 15548997, # لون أحمر
            "footer": {"text": "رادار الثغرات - حصن الشمال"}
        }]
    }
    requests.post(WEBHOOK_URL, json=data)

feed = feedparser.parse(RSS_FEED_URL)
# سنرسل آخر ثغرة فقط في كل فحص لتجنب التكرار
if feed.entries:
    send_to_discord(feed.entries[0])
