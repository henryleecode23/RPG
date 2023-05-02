__project__ = "HLCT RPG Bot"
__author__ = "HLCT"
__gmail__ = "henryleecode23@gmail.com"
__version__ = "0.0.3"


def main():
    from core.bot import Bot
    from dotenv import load_dotenv
    from os import getenv
    load_dotenv()
    Bot().run(getenv("BOT_TOKEN"))

if __name__ == "__main__":
    main()
