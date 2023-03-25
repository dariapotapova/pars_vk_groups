from autorize import autorize


def search_current_inf(vk_session):
    vk_session = vk_session
    vk = vk_session.get_api()
    letters = ['магазин', 'интернет-магазин', 'shop']
    group_info = []
    ids = []
    for letter in letters:
        all_groups = vk.groups.search(q=letter, count=2)['items']
        for i in all_groups:
            if i['id'] not in ids:
                group_info.append({
                    'group_id': i['id'],
                    'name': i['name'],
                    'screen_name': i['screen_name'],
                    'is_closed': i['is_closed'],
                    'type': i['type']
                })
                ids.append(i['id'])
    return group_info


def search_by_ids():
    vk_session = autorize()
    vk = vk_session.get_api()
    group_info = search_current_inf(vk_session)
    for i in range(len(group_info)):
        inf = vk.groups.getById(group_id=group_info[i]['group_id'], fields=['city', 'country', 'description', 'contacts'])

        if 'city' in inf[0]:
            group_info[i]['city'] = inf[0]['city']['title']
        else:
            group_info[i]['city'] = ''

        if 'country' in inf[0]:
            group_info[i]['country'] = inf[0]['country']['title']
        else:
            group_info[i]['country'] = ''

        if 'description' in inf[0]:
            group_info[i]['description'] = inf[0]['description']
        else:
            group_info[i]['description'] = ''

        if 'contacts' in inf[0]:
            group_info[i]['contacts'] = [[user.get('user_id'), user.get('desc'), user.get('phone'), user.get('email')]
                                         for user in inf[0]['contacts']]
        else:
            group_info[i]['contacts'] = ''

    return group_info

