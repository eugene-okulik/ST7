def check_permissions(func):

    def wrapper(*args):
        if args[0]['is_admin']:
            return func(*args)
        print('Доступ запрещен')
        return

    return wrapper


@check_permissions
def delete_user(user, user_id):
    print(f"Пользователь с id {user_id} удален")


admin_user = {"username": "admin", "is_admin": True}
normal_user = {"username": "user", "is_admin": False}

delete_user(normal_user, '001')
delete_user(admin_user, '001')
