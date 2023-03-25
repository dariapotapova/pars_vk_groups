from password_login import LOGIN, PASSWORD
import vk_api


def auth_handler():
    key = input("Enter authentication code: ")
    remember_device = True

    return key, remember_device


def autorize():
    login, password = LOGIN, PASSWORD
    vk_session = vk_api.VkApi(
        login, password,
        auth_handler=auth_handler
    )

    try:
        vk_session.auth()
        return vk_session
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return
