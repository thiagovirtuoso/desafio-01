def add_contact(contact_list, contact_name, contact_phone, contact_email):
    contact = {"name": contact_name, "phone": contact_phone, "email": contact_email, "favorite": False}
    contact_list.append(contact)
    print(f'Contato {contact_name} foi adicionado com sucesso!')
    return

def view_contact_list(contact_list):
    print('\nLista de contatos:')
    for index, contact in enumerate(contact_list, start=1):
        favorite_icon = '★' if contact['favorite'] else '☆'
        contact_name = contact['name']
        contact_phone = contact['phone']
        contact_email = contact['email']
        print(f'{index}. [ {favorite_icon} ] Nome: {contact_name} - Telefone: {contact_phone} - Email: {contact_email}')
    return

def edit_contact(contact_list, contact_index, new_name, new_phone, new_email):
    contact_index = int(contact_index) - 1
    if contact_index >= 0 and contact_index < len(contact_list):
        contact = contact_list[contact_index]
        contact['name'] = new_name
        contact['phone'] = new_phone
        contact['email'] = new_email
        print(f'O contato {new_name} foi atualizado com sucesso!')
    return

def add_remove_favorite(contact_list, contact_index):
    contact_index = int(contact_index) - 1
    if contact_index >= 0 and contact_index < len(contact_list):
        contact = contact_list[contact_index]
        contact_name = contact['name']
        if contact['favorite']:
            contact['favorite'] = False
            print(f'O contato {contact_name} foi desfavoritado com sucesso!')
        else:
            contact['favorite'] = True
            print(f'O contato {contact_name} foi favoritado com sucesso!')
    return

def favorite_list(contact_list):
    favorites = []

    print('\nLista de favoritos:')
    for index, contact in enumerate(contact_list):
        if contact['favorite']:
            favorites.append(contact)
    for index, favorite in enumerate(favorites, start=1):
        favorite_icon = '★' if favorite['favorite'] else '☆'
        contact_name = favorite['name']
        contact_phone = favorite['phone']
        contact_email = favorite['email']
        print(f'{index}. [ {favorite_icon} ] Nome: {contact_name} - Telefone: {contact_phone} - Email: {contact_email}')

def delete_contact(contact_list, contact_index):
    contact_index = int(contact_index) - 1
    if contact_index >= 0 and contact_index < len(contact_list):
        contact = contact_list[contact_index]
        contact_name = contact['name']
        contact_list.remove(contact)
        print(f'O contato {contact_name} foi removido com sucesso!')
    return
    
contact_list = []
while True:
    print('Agenda de contatos:')
    print('1 - Adicionar um contato')
    print('2 - Lista de contatos')
    print('3 - Editar contato')
    print('4 - Adicionar/remover favorito')
    print('5 - Favoritos')
    print('6 - Apagar contato')
    print('7 - Sair')

    user_choice = input('Digite a sua escolha: ')
    
    if user_choice == '1':
        contact_name = input('Digite o nome do contato: ')
        contact_phone = input('Digite o número do telefone: ')
        contact_email = input('Digite o email do contato: ')
        add_contact(contact_list, contact_name, contact_phone, contact_email)
    elif user_choice == '2':
        view_contact_list(contact_list)
    elif user_choice == '3':
        view_contact_list(contact_list)
        contact_index = input('Escolha qual contato deseja editar: ')
        contact_name = input('Digite o nome atualizado do contato: ')
        contact_phone = input('Digite o número atualizado do telefone: ')
        contact_email = input('Digite o email atualizado do contato: ')
        edit_contact(contact_list, contact_index, contact_name, contact_phone, contact_email)
    elif user_choice == '4':
        view_contact_list(contact_list)
        contact_index = input('Escolha qual contato deseja favoritar/desfavoritar: ')
        add_remove_favorite(contact_list, contact_index)
    elif user_choice == '5':
        favorite_list(contact_list)
    elif user_choice == '6':
        view_contact_list(contact_list)
        contact_index = input('Escolha qual contato deseja excluir: ')
        delete_contact(contact_list, contact_index)
    elif user_choice == '7':
        break