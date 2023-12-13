from aiogram.fsm.state import StatesGroup, State


class MainMenu(StatesGroup):
    main_menu = State()


class DuelMenu(StatesGroup):
    confirm_duel = State()
    opponent_setting = State()
    show_result = State()
    # show_history = State()


class AccMenu(StatesGroup):
    acc_menu = State()
    acc_setting = State()


class SettingMenu(StatesGroup):
    setting_menu = State()


class JokeMenu(StatesGroup):
    joke_menu = State()
