from controlador import BotController

if __name__ == "__main__":
    TOKEN = '7931784865:AAESjqpTO2Yx62fe1xyCGu0wm9ERnYMaAlQ'
    LED_PIN = 18

    bot_controller = BotController(TOKEN, LED_PIN)
    bot_controller.run()
