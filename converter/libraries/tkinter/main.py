from converter.libraries.tkinter.utils import display_error_message

helping_words = [
    " с ", " със ", " съобщение ", " бутони ", " иконка "
]

class DisplayedMessage:
    def __init__(self, title='', message='', x=900, y=200, buttons=['ok,'], photo_path=''):
        self.title = title
        self.message = message
        self.x = x
        self.y = y
        self.buttons = self.rework_buttons(buttons)
        self.photo_path = photo_path

    def rework_buttons(self, buttons: str):
        buttons = buttons.split(',')
        print('buttons to split', buttons)
        result = []
        for button in buttons:
            result.append({"label": button.replace('"', ''), "command": lambda: print("Retry clicked")})
        return result
    


    def __str__(self):
        display_error_message(self.title, self.message, self.x, self.y, self.buttons, self.photo_path)
        return "Съобщението е показано"


titleAlias = {
    'грешка': "error",
    "предупреждение": "warning",
    'инфо': "info"
}    

def TKINTER_MESSAGE(line):
    print("TKINTER LINE: ", line)
    buttons_provided = 'с бутони' in line
    title_provided = ' грешка ' in line or ' предупреждение ' in line or ' инфо ' in line
    photo_provided = ' със иконка ' in line
    title, buttons, photo_path = '', '', ''
    message_data = {}
    for word in helping_words:
        line = line.replace(word, ' ')
    
    line_items = line.split(" ")
    string_res = ""
    match_start = False
    s_index = 0
    e_index = 0
    for index, el in enumerate(line_items):
        if '"' in el:
            if match_start:
                e_index = index
                string_res += " " + el
                break
            match_start = True
            s_index = index
        if match_start:
            string_res += " " + el
    
    line_items[s_index] = string_res
    line_items[s_index+1:e_index+1] = ''

    if title_provided:
        try:
            index = line_items.index("грешка")
        except:
            try:
                index = line_items.index('предупреждение')
            except:
                index = line_items.index('инфо')
    else:
        print(line_items)
        index = line_items.index('съобщение')
    
    arguments = line_items[index+1::]
    if title_provided:
        title = line_items.pop(index)
        message_data['title'] = f"'{titleAlias[title]}'"
    if buttons_provided:
        buttons = line_items.pop(index+1)
        message_data['buttons'] = f"'{buttons}" + "'"
    if photo_provided:
        photo_path = line_items.pop(1)
        message_data['photo_path'] = photo_path
    
    message = line_items.pop(index).replace('"', '')
    message_data['message'] = f"'{message}'"

    res = ''
    for m_index, key in enumerate(message_data.keys()):
        res += f"{key}={message_data[key]}"
        if m_index+1 != len(message_data.keys()):
            res += ','
    result = f"""DisplayedMessage({res}))"""
    line_items[index] = result

    return " ".join(line_items)