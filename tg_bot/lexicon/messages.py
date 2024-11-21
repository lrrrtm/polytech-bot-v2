from emoji import emojize

lexicon = {
    'service': {
        'command_not_allowed': f"{emojize(':information:')} Данная команда недоступна, отправь или нажми /start"
    },

    'registration': {
        'ask_to_group': f"{emojize(':waving_hand:')} Привет! Для продолжения отправь номер своей группы\n\n<blockquote>Пример: 5130904/20102</blockquote>"
    },

    'group_updater': {
        'group_updated': f"{emojize(':information:')} <b>Данные о группе обновлены!</b>\n\nНовая группа: group_num",
        'group_inserted': f"{emojize(':information:')} <b>Данные о группе сохранены!</b>\n\nНовая группа: group_num\n\nЧтобы открыть меню, отправь или нажми /menu",
        'group_not_found': f"{emojize(':information:')} Группы с номером \"input_user_group\", попробуй ещё раз",
        'too_many_groups': f"{emojize(':information:')} Найдено слишком много групп, у которых есть \"input_user_group\" в номере. Уточни номер группы",
        'many_groups': f"{emojize(':information:')} Найдено несколько групп, у которых есть \"input_user_group\" в номере. Выбери свою",
    }
}
