import core.commands as commands


def set_handlers(dp):
    dp.register_message_handler(commands.start, commands=['start'])
