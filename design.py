from myMailer import send_email
import flet as ft

def main(page: ft.Page):
    page.title = "SendMail"
    page.horizontal_alignment = "center"
    page.theme_mode = "light"
    page.theme = ft.theme.Theme(color_scheme_seed="blue")
    page.window_bgcolor = '#00598f'
    page.scroll = 'always'
    page.padding = 30
    page.bgcolor = '#dbeef7'
    page.snack_bar = ft.SnackBar(
        content=ft.Text("Mail sent successfully!",text_align="center"),
        bgcolor='#00598f'
    )

    logo = ft.Image(src=f"logo\mail_logo.png", height=150)
    to = ft.TextField(label="To", border_radius=30, border="none")
    subject = ft.TextField(label="Subject", border_radius=30, border="none")
    message = ft.TextField(label="Write your messsage", border_radius=30, multiline=True, border="none")
    message_type = ft.Switch(label='HTML Mode', value=False, active_color='#00598f')
    
    outputContainer = ft.Container(
        content=ft.Text(value="Developer: Kumar Anurag | Instagram: kmranrg",weight='bold'),
        margin=20,
        padding=20,
        bgcolor="#f2f2f2",
        border_radius=30
    )

    def send_mail(e):
        page.snack_bar.open = True
        page.update()

    page.add(
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
        outputContainer
    )

ft.app(target=main, assets_dir="assets")