import os
import subprocess
from datetime import datetime

from aiogram import Router, types
from aiogram.filters import Command
from aiogram.filters.callback_data import CallbackData
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from pyexpat.errors import messages

from db_orm.crud import get_user_by_attrs, create_user, update_user_data
from db_orm.models import User
from tg_bot.handlers.menu import cmd_menu
from tg_bot.keyboards.groups import get_groups_names_kb
from tg_bot.states.register_user import InputUserStudyGroup
from utils.groups_jsoner import find_group_by_name

from tg_bot.lexicon.messages import lexicon as msgs_lexicon

router = Router()


@router.message(Command("start"))
async def cmd_start(message: Message, state: FSMContext):
    user = get_user_by_attrs(telegram_id=message.from_user.id)

    if user:
        if user.is_active:
            await cmd_menu(message, state)
        else:
            # todo: восстановление аккаунта или регистрация заново
            # удалил аккаунт, но данные о нём ещё есть
            pass
    else:
        # новый пользователь
        await message.answer(
            text=msgs_lexicon['registration']['ask_to_group']
        )
        await state.set_state(InputUserStudyGroup.waiting_for_msg)


@router.message(InputUserStudyGroup.waiting_for_msg)
async def find_and_insert_user_group(message: Message, state: FSMContext):
    input_user_group = message.text.strip()
    founded_groups = find_group_by_name(input_user_group)

    if founded_groups:
        if len(founded_groups) == 1:
            await state.clear()

            user_group_data = founded_groups[0]

            user = get_user_by_attrs(telegram_id=message.from_user.id)
            if user:
                user.faculty = user_group_data['faculty']
                user.group = user_group_data['group']

                update_user_data(user)

                await message.answer(
                    text=msgs_lexicon['group_updater']['group_updated'].replace('group_num', user_group_data['name'])
                )

            else:
                user = User(
                    telegram_id=message.from_user.id,
                    faculty=user_group_data["faculty"],
                    group=user_group_data["group"],
                    created_at_dt=datetime.now(),
                    locale='rus'
                )

                create_user(user)

                await message.answer(
                    text=msgs_lexicon['group_updater']['group_inserted'].replace('group_num', user_group_data['name'])
                )

        elif len(founded_groups) < 15:
            await message.answer(
                text=msgs_lexicon['group_updater']['many_groups'].replace('input_user_group', input_user_group),
                reply_markup=get_groups_names_kb(founded_groups)
            )
            # todo: set_state


        else:
            await message.answer(
                text=msgs_lexicon['group_updater']['too_many_groups'].replace('input_user_group', input_user_group)
            )

    else:
        await message.answer(
            text=msgs_lexicon['group_updater']['group_not_found'].replace('input_user_group', input_user_group)
        )


@router.callback_query(lambda c: c.data == 'git_pull')
async def process_callback_button(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    await callback.message.delete()
    await callback.message.answer(
        text="Выполняется перезапуск..."
    )

    repo_path = '/root/repos/polytech_bot_v2'
    restart_command = 'sudo systemctl restart polytech_bot'
    os.chdir(repo_path)
    subprocess.run(['git', 'pull'], check=True)
    subprocess.run(restart_command.split(), check=True)
