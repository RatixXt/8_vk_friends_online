# -*- coding: utf-8 -*-
import vk
from getpass import getpass


APP_ID = 5667375


def get_user_login():
    return input(u'Введите номер мобильного телефона или e-mail:')


def get_user_password():
    return getpass(u'Введите пароль:')


def get_online_friends_info(login, password):
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
        scope='friends',
    )
    friends_online_list_id = vk.API(session).friends.getOnline()
    friends_online_info = vk.API(session).users.get(
        user_ids=friends_online_list_id,
        name_case='nom',
    )
    return friends_online_info


def output_friends_to_console(friends_online_info):
    print(u'Друзей онлайн: %i' % len(friends_online_info))
    for friend in friends_online_info:
        print(friend['first_name'], friend['last_name'])


if __name__ == '__main__':
    login = get_user_login()
    password = get_user_password()
    friends_online_info = get_online_friends_info(login, password)
    output_friends_to_console(friends_online_info)
