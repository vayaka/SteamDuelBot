from aiogram_dialog import Dialog

from bot.dialogs.main_menu import windows


def bot_main_menu():
    return [
        Dialog(
            windows.main_window(),
        ),
        Dialog(
            windows.confirm_window(),
            windows.opponent_setting_window(),
            windows.show_result_window()
        ),
        Dialog(
            windows.joke_window()
        )
    ]
