test_settings = {
    "theme": "dark",
    "volume": 75,
    "language": "English",
    "notifications": True,
}

def add_setting(settings_dictionary, key_value_tuple):
    key,value = key_value_tuple
    key_lower = key.lower()

    if isinstance(value,str):
        value_lower= value.lower()
    else:
        value_lower = value
    if key_lower in settings_dictionary:
        return f'Setting \'{key_lower}\' already exists! Cannot add a new setting with this name.'
    else:
        settings_dictionary [key_lower]=value_lower 
        return f'Setting \'{key_lower}\' added with value \'{value_lower}\' successfully!'

def update_setting(settings_dictionary, key_value_tuple):
    key,value = key_value_tuple
    key_lower = key.lower()
    if isinstance(value,str):
        value_lower= value.lower()
    else:
        value_lower = value
    if key_lower in settings_dictionary:
        settings_dictionary[key_lower]=value_lower
        return f'Setting \'{key_lower}\' updated to \'{value_lower}\' successfully!'
    else:
        return f'Setting \'{key_lower}\' does not exist! Cannot update a non-existing setting.'


def delete_setting(settings_dictionary, key_value_tuple):
    key = key_value_tuple
    key_lower = key.lower()

    if key_lower in settings_dictionary:
        del settings_dictionary[key_lower]
        return f'Setting \'{key_lower}\' deleted successfully!'
    else:
        return f'Setting not found!'

def view_settings(settings_view):
    if not settings_view:
        return f'No settings available.'
    else:
        result = "Current User Settings:\n"
        for key, value in settings_view.items():
            key_cap = key.capitalize()
            result += f'{key_cap}: {value}\n'
        
        return result


print(view_settings(test_settings))
