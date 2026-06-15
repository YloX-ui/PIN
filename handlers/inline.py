from aiogram import Router,F
from aiogram.types import CallbackQuery

from .inline_booton import plan_menu

from .inline_booton import (
    main_key,
    helper_kb,
    pay_sub,
    vpn_path_true,
    vpn_path_false,
    profile_kb,
    bonus_kb
)

router = Router()


@router.callback_query(F.data == F.data)
async def inline_handler(call:CallbackQuery):
    #
    if call.data == 'main':
        await call.message.edit_caption(
            caption='💎 (name VPN)\n\nВыбери действие:',
            reply_markup=main_key)
    #
    elif call.data == 'vpn_path':
        test = 0
        if test == 0:
            inline_kb = vpn_path_false
            text_vpn_path = 'Нет активной подписки\nкупи подписку, чтобы получить ссылку'
        else:
            inline_kb = vpn_path_true
            text_vpn_path ='''
Ссылка на подписку

для Hiddify/V2Box/NekoBox:
(Будет генирироваться ссылка)
                '''  

        await call.message.edit_caption(
                caption=text_vpn_path,
                reply_markup=inline_kb)
    #
    elif call.data == 'pay_sub':
        await call.message.edit_caption(
            text='Выбери тариф',
            reply_markup=pay_sub)
        
    #
    elif 'plan_' in call.data:
        await call.message.edit_caption(caption=f"""
💎 Lite

📅 {call.data} дней
⚡️ Без ограничений скорости
🌍 Все серверы

💰 Цена: {call.data}

Выбери способ оплаты:
""",reply_markup=plan_menu(call.data))
        
    #
    elif call.data == 'profile':
        await call.message.edit_caption(
            caption=f"Личный кабинет\nПодписка{'db'}\n приглашенно друзуй:{'db'}",
            reply_markup=profile_kb)
        
    elif call.data == 'bonus':
        await call.message.edit_caption(
            caption="""
🎁 Бонусы

🎟 Промокод — введи код и получи бесплатные дни

👥 Реферальная программа
Приглашай друзей — оба получаете +7 дней!

📊 Приглашено: db друзей
🎁 Бонусных дней: db
""",reply_markup=bonus_kb)

    elif call.data == 'helper':
        await call.message.edit_caption(
            caption='Напишите нам',
            reply_markup=helper_kb)
        
