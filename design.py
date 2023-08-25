from myMailer import send_email
import flet as ft

def main(page: ft.Page):
    page.title = 'Flet App'
    page.add(
        ft.Text('Hello')
    )
ft.app(target=main)