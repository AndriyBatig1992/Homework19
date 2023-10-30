from src.repository import get_user, create_record, list_records, update_record, remove_record
from src.data import  model_map, model, action, login, _id, my_arg


def perform_action(action, model, user, **kwargs):
    if action in model_map and model in model_map[action]:
        selected_model, args = model_map[action][model]
        if action == 'create':
            create_record(selected_model, user=user, **args, **kwargs)
        elif action == 'list':
            list_records(selected_model, user=user)
        elif action == 'update':
            kwargs = {key: value for key, value in my_arg.items() if value is not None}
            update_record(selected_model, record_id=_id, user=user, **kwargs)
        elif action == 'remove':
            remove_record(selected_model, record_id=_id, user=user)
    else:
        print('Invalid model or action')

def main(user, action, model):
    if action in ('create', 'list', 'update', 'remove'):
        perform_action(action, model, user)
    else:
        print('Invalid action')


if __name__ == '__main__':
    user = get_user(login)
    print(login)
    if user:
        password = input('Password: ')
        if password == user.password:
            main(user, action, model)
        else:
            print('Wrong password')
    else:
        print('User not found')


#Команди

# py main.py -a create -m Student -fn 'Василь' -idg 1 -l asd
# py main.py -a create -m Group -n '4_В' -l asd
# py main.py -a create -m Teacher -fn 'Іван Степанович' --l asd
# py main.py --a create -m Discipline -n "Фізика" -idt 1 -l asd
# py main.py -a create -m Grade -g 2 -d "2021-10-01"  -ids 1 -idd 1 -l asd

# py main.py -a list -m Student -l asd
# py main.py -a list -m Group -l asd
# py main.py -a list -m Teacher -l asd
# py main.py -a list -m Discipline -l asd
# py main.py -a list -m Grade -l asd


# py main.py -a update -m Student -id 1 -fn "Марія" -idg 1 -l asd
# py main.py -a update -m Group -id 1 n "10В"-l asd
# py main.py -a update -m Teacher -id 1 -fn "Баль Олена" -l asd
# py main.py -a update -m Discipline -id 1 -n "Історія України" -idt 1 -l asd
# py main.py -a update -m Grade -id  -g 3 -d "2021-10-01"  -ids 1 -idd 1 -l asd


# py main.py -a remove -m Student -id 1 -l asd
# py main.py -a remove -m Group -id 1 -l asd
# py main.py -a remove -m Teacher -id 1 -l asd
# py main.py -a remove -m Discipline -id 1 -l asd
# py main.py -a remove -m Grade -id 1 -l asd

