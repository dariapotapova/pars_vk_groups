from search_groups import search_by_ids
import sqlite3


def add_to_db():
    data = search_by_ids()
    conn = sqlite3.connect("new_file.db")
    for i in range(len(data)):
        conn.cursor().execute(f'''INSERT INTO groups(group_id, name,
                             screen_name, is_closed, type_group, city, country,
                              description, contacts) VALUES({data[i]['group_id']}, "{data[i]['name']}",
                               "{data[i]['screen_name']}", {data[i]['is_closed']}, "{data[i]['type']}",
                                "{data[i]['city']}", "{data[i]['country']}", "{data[i]['description']}", "{data[i]['contacts']}")''')
    conn.commit()


add_to_db()

