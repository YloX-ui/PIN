from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from aiogram.utils.keyboard import InlineKeyboardBuilder

main_key = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="пробный периуд", callback_data="test_cpn_user"),
        ],
        [
            InlineKeyboardButton(text="Получить ссылку", callback_data="vpn_path")
        ],
        [
            InlineKeyboardButton(text='Оплата',callback_data='pay_sub'),
            InlineKeyboardButton(text='Бонусы',callback_data='bonus')
        ],
        [
            InlineKeyboardButton(text="профиль", callback_data="profile")
        ],
        [
            InlineKeyboardButton(text="поддержка", callback_data="helper")
        ],
        [
            InlineKeyboardButton(text="Канал", url="http://google.com")
        ]
    ]
)

helper_kb = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Подержка", url="http://google.com")
    ],
    [
        InlineKeyboardButton(text="Назад", callback_data="main")
    ]
])




pay_sub = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='lite- 15 day(99r)', callback_data='plan_1')
    ],
    [
        InlineKeyboardButton(text='lite- 30 day(169r)', callback_data='plan_2')
    ],
    [
        InlineKeyboardButton(text='lite- 180 day(449r)', callback_data='plan_3')
    ],
    [
        InlineKeyboardButton(text='lite- 365 day(1499r)', callback_data='plan_4')
    ],
])


def plan_menu(plan):
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text=f'Карта/СБП ({plan})', callback_data=f'pay_yookassa:{plan.split("_")[1].strip()}')
        ],
        [
            InlineKeyboardButton(text=f'Крипта ({plan})', callback_data=f'crypto:{plan.split("_")[1].strip()}')
        ],
        [
            InlineKeyboardButton(text=f'Starts ({plan})', callback_data=f'pay_stars:{plan.split("_")[1].strip()}')
        ],
        [
            InlineKeyboardButton(text=f'к тарифом ({plan})', callback_data=f'pay_sub')
        ]
        ])
    return kb


profile_kb=InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text= "Получить ссылку",callback_data='vpn_path')
    ],
    [
        InlineKeyboardButton(text= "Купить подписку",callback_data='pay_sub')
    ],
    [
        InlineKeyboardButton(text= "Пригласить друзей",callback_data='ref_link')
    ],
    [
        InlineKeyboardButton(text= "Актевировать ключ",callback_data='accion_key')
    ],
    [
        InlineKeyboardButton(text= "Назад",callback_data='main')
    ],
])

bonus_kb = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text= "Ввести промокод",callback_data='input_promo')
    ],
    [
        InlineKeyboardButton(text= "пригласить друзей",callback_data='ref_link')
    ],
    [
        InlineKeyboardButton(text= "Назад",callback_data='main')
    ]
])


vpn_path_true = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text='Сменить сылку', callback_data='change_path')
        ],
        [
            InlineKeyboardButton(text='Назад',callback_data='main')
        ]
    ]
)

vpn_path_false = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text='Купить подписку', callback_data='pay_sub')
        ],
        [
            InlineKeyboardButton(text='Назад',callback_data='main')
        ]
    ]
)