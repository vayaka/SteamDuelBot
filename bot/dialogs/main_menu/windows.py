from aiogram_dialog import Window
from aiogram_dialog.widgets.input import TextInput
from aiogram_dialog.widgets.kbd import Column, SwitchTo, Cancel, Start, Button
from aiogram_dialog.widgets.text import Const, Format

from bot.dialogs.main_menu.buttons import go_clicked
from bot.dialogs.main_menu.getters import get_joke
from bot.dialogs.main_menu.selected import on_link_entered
from bot.dialogs.main_menu.states import MainMenu, DuelMenu, AccMenu, SettingMenu, JokeMenu


def main_window():
    return Window(
        Const("Меню готово!\nТеперь выбор за тобой - будто в RPG, только без драконов! 🐉"),
        Column(
            Start(Const("🎮 Дуэли"), id="duel", state=DuelMenu.confirm_duel),
            Start(Const("👤 Аккаунт"), id="account", state=AccMenu.acc_menu),
            Start(Const("⚙️ Настройки"), id="setting", state=SettingMenu.setting_menu),
            Start(Const("😂 Шутка"), id="joke", state=JokeMenu.joke_menu),
        ),
        state=MainMenu.main_menu
    )


def confirm_window():
    return Window(
        Const("Вы уверены, что хотите начать дуэль?"),
        Column(
            SwitchTo(Const("Подтвердить"), id="confirm_duel", state=DuelMenu.opponent_setting),
            Cancel(Const("Отмена"), id="cancel_duel")
        ),
        state=DuelMenu.confirm_duel
    )


def opponent_setting_window():
    return Window(
        Const("Введите ссылку на профиль оппонента: "),
        TextInput(
            id="opponent_link",
            on_success=on_link_entered,
        ),
        state=DuelMenu.opponent_setting
    )


def show_result_window():
    return Window(
        Const("Результаты дуэли: "),
        Column(
            Cancel(Const("Отмена"), id="cancel_result")
        ),
        state=DuelMenu.show_result
    )


def joke_window():
    return Window(
        Format("Шутка\n{joke}"),
        Column(
            SwitchTo(Const("Ещё"), id="more_joke", state=JokeMenu.joke_menu),
            Cancel(Const("Отмена"), id="cancel_joke")
        ),
        getter=get_joke,
        state=JokeMenu.joke_menu,
    )
