from flet import *
from time import sleep
from random import choice

from Core.Config import *
from Core.Run import start_async_attacks
from Core.Attack.Services import urls
from Core.Attack.Feedback_Services import feedback_urls
from Core.TBanner import banner

color = check_config()['color']

def main(page: Page):
    page.window_center()
    page.title = 'Grobovsheke-SmsBomber'
    page.scroll = 'adaptive'
    page.auto_scroll = True
    page.window_width = 560
    page.window_height = 600
    page.vertical_alignment = 'center'
    page.horizontal_alignment = 'center'
    page.theme_mode = check_config()['theme']
    page.window_maximizable = False
    page.window_resizable = False
    change_config('attack', 'False')

    def type_attack_change(e):
        change_config('type_attack', f'{type_attack.value}')

    def feedback_change(e):
        change_config('feedback', f'{feedback.value}')

    def theme_change(e):
        page.theme_mode = 'dark' if page.theme_mode == 'light' else 'light'
        page.update()
        change_config('theme', f'''{page.theme_mode}''')

    def color_change(e):
        _color = [MY_COLOR, 'red', 'pink', 'WHITE', 'black', 'purple', 'indigo', 'blue', 'cyan', 'teal', 'green', 'lime', 'yellow', 'amber', 'orange', 'brown', 'bluegrey', 'grey']
        global color
        color = choice(_color)
        banner.controls = [Text(spans=[TextSpan('Grobovsheke', TextStyle(size=85, foreground=Paint(color=color, stroke_width=9, stroke_join='round', style='stroke')))], font_family='Consolas'), Text(spans=[TextSpan('GROBOVSHEKE', TextStyle(size=95, color=color))], font_family='Consolas')]
        
        number.border_color=color
        number.cursor_color=color
        number.focused_border_color=color
        number.selection_color=color
        number.label_style=TextStyle(color=color)

        replay.border_color=color
        replay.cursor_color=color
        replay.focused_border_color=color
        replay.selection_color=color
        replay.label_style=TextStyle(color=color)

        type_attack.border_color=color
        type_attack.label_style=TextStyle(color=color)

        feedback.active_color=color

        attack_button.color=color

        page.clean()
        ADD()
        change_config('color', f'{color}')

    def error(message, reason='error'):
        def button_cancel(e):
            error_message.open = False
            page.update()

        error_message = AlertDialog(title=Text(reason, color=color, size=30, text_align='center', font_family='Consolas'), content=Text(message, font_family='Consolas'), actions=[TextButton('ОКЕЙ', on_click=button_cancel, style=ButtonStyle(color=color))], actions_alignment='end')

        page.dialog = error_message
        error_message.open = True
        page.update()

    def start_attack():
        def button_cancel(e):
            attack_window.open = False
            page.update()

        attack_window = AlertDialog(modal=True, title=Text('attack started', color=color, size=30, text_align=TextAlign.CENTER), content=ProgressBar(width=325, color=color), actions=[TextButton('close', width=90, height=40, on_click=button_cancel, style=ButtonStyle(color=color))], actions_alignment='end', open=True)

        page.dialog = attack_window
        page.update()

        change_config('attack', 'True')
        start_async_attacks(number.value, replay.value)
        change_config('attack', 'False')
        attack_window.open = False
        page.update()

    def confirmation():
        def button_cancel(e):
            confirmation_window.open = False
            page.update()

        def button_continue(e):
            confirmation_window.open = False
            page.update()
            sleep(1)
            start_attack()    


        confirmation_window = AlertDialog(modal=True, title=Text('Attention!', color=color, size=30, text_align='center'), content=Text('After launching an attack and instantly canceling it, the launch process will be irreversible, and the attack will be completed to completion in any case!\n\nContinue?'), actions=[TextButton('NO', on_click=button_cancel, style=ButtonStyle(color=color)), TextButton('YES', on_click=button_continue, style=ButtonStyle(color=color))], actions_alignment='end', open=True)
        page.dialog = confirmation_window
        page.update()

    def checking_values(e):
        if number.value:
            try:
                int(number.value)
                if number.value.isdigit() == True:
                    if replay.value:
                        try:
                            int(replay.value)
                            if replay.value.isdigit() == True:
                                if int(replay.value) > 0 and int(replay.value) < 1001:
                                    if check_config()['attack'] == 'False':
                                        confirmation()
                                    else:
                                        confirmation()
                                else:
                                    error('Enter the number of laps, from 1 to 1000!')
                                    replay.focus()
                            else:
                                error('Enter the number of circles without any symbols!')
                                replay.focus()
                        except:
                            error('Enter the number of laps!')
                            replay.focus()
                    else:
                        error('Enter the number of laps!')
                        replay.focus()
                else:
                    error('Enter the number without any characters!')
                    number.focus()
            except:
                error('Please enter a valid number!')
                number.focus()
        else:
            error('Enter attack number!')
            number.focus()

    def information(e):
        def button(e):
            information_window.open = False
            page.update()

        information_window = AlertDialog(content=Text(f'''Grobovsheke-SmsBomber!''', text_align='center', size=24, color=color, font_family='Consolas'), open=True, actions=[TextButton('ok', width=110, height=50, on_click=button, style=ButtonStyle(color=color))], actions_alignment='end')

        page.dialog = information_window
        page.update()

    banner = Stack([Text(spans=[TextSpan('Grobovsheke', TextStyle(size=85, foreground=Paint(color=color, stroke_width=9, stroke_join='round', style='stroke')))], font_family='Consolas'), Text(spans=[TextSpan('Grobovsheke', TextStyle(size=85, color=color))], font_family='Consolas')])

    number = TextField(label='Enter the number without "+"', width=275, text_align='center', border_radius=40, border_color=color, cursor_color=color, focused_border_color=color, autofocus=True, selection_color=color, label_style=TextStyle(color=color))

    replay = TextField(label='replays', width=131, text_align='center', border_radius=40, border_color=color, cursor_color=color, focused_border_color=color, selection_color=color, value='1', label_style=TextStyle(color=color))

    type_attack = Dropdown(label='Attack type', hint_text='choose Attack type', options=[dropdown.Option('MIX'), dropdown.Option('SMS'), dropdown.Option('CALL')], width=131, border_radius=40, alignment=alignment.bottom_center, border_color=color, value=check_config()['type_attack'], label_style=TextStyle(color=color), on_change=type_attack_change)

    feedback = Switch(label='Feedback services (?)', value=True if check_config()['feedback'] == 'True' else False, width=280, active_color=color, on_change=feedback_change, tooltip='Services that leave applications (such as connecting to the Internet or taking out a loan) on different sites. Be careful\nwhen using this function!')

    attack_button = ElevatedButton(content=Text('Attack', size=25), on_click=checking_values, width=190, height=60, color=color)

    def ADD():
        page.add(
                Text('\n', size=6),
                banner,
                Text('\n', size=12),
                number,
                Row([type_attack, replay],alignment='CENTER'),
                feedback,
                attack_button,
                  Row([IconButton(icon='telegram', icon_size=48, tooltip='Channel', url='https://t.me/grobovsheke', icon_color=color),
                    IconButton(icon='telegram', icon_size=48, tooltip='Coder', url='https://t.me/HECAMCA', icon_color=color),
                    IconButton(icon='info', icon_size=48, tooltip='Information', icon_color=color, on_click=information)], alignment='CENTER')),    
    ADD()

def Start(web=True):
    if web:
        host, port = '127.0.0.1', 9876
        banner(host, port)
        app(main, view='web_browser', host=host, port=port)
    else:
        app(main)

