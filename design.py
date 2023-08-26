from myMailer import send_email
import flet as ft

def main(page: ft.Page):
    page.title = "SendMail"
    page.theme_mode = "light"
    page.theme = ft.theme.Theme(color_scheme_seed="blue")
    page.window_bgcolor = '#00598f' 
    mail_status = ft.Text(text_align="center")
    page.snack_bar = ft.SnackBar(
        content=mail_status,
        bgcolor='#00598f'
    )

    logo = ft.Image(src=f"logo\mail_logo.png", height=150)
    to = ft.TextField(label="To", border_radius=30, border="none")
    subject = ft.TextField(label="Subject", border_radius=30, border="none")
    message = ft.TextField(label="Write your messsage", border_radius=30, multiline=True, border="none")
    message_type = ft.Switch(label='HTML Mode', value=False, active_color='#00598f')
    
    devInfo = ft.Container(
        content=ft.Text(value="Developer: Kumar Anurag | Instagram: kmranrg",weight='bold',color='#00598f'),
        margin=20,
        padding=20,
        bgcolor="#f2f2f2",
        border_radius=30
    )

    def send_mail(e):
        type_of_message = 'plain'
        if message_type.value == True:
            type_of_message = 'html'
        mail_status.value = send_email(to.value,subject.value,message.value,type_of_message)
        page.snack_bar.open = True
        page.update()

    def route_change(route):
        page.views.clear()
        page.views.append(
            ft.View(
                "/",
                [  
                    ft.Image(src=f"logo\mail_logo.png", height=500),
                    ft.ElevatedButton("Launch",on_click=lambda _: page.go("/homepage"))
                ],
                scroll='always',
                vertical_alignment="center",
                horizontal_alignment="center",
                padding=50,
                bgcolor='#00598f'
            )
        )
        if page.route == '/homepage':
            page.views.append(
                ft.View(
                    '/homepage',
                    [
                        logo,
                        to,
                        subject,
                        ft.Row([message_type],alignment="center"),
                        message,
                        
                        ft.Container(height=100),
                        ft.IconButton(
                            icon=ft.icons.SEND,
                            icon_color="#00598f",
                            icon_size=40,
                            tooltip="Send Mail",
                            on_click=send_mail
                        ),
                        ft.Container(height=10),
                        devInfo
                    ],
                    scroll='always',
                    horizontal_alignment="center",
                    padding=30,
                    bgcolor='#dbeef7'
                )
            )
        page.update()
    
    def view_pop(view):
        page.view.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)


ft.app(target=main, assets_dir="assets")