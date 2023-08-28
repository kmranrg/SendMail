from myMailer import send_email
import flet as ft
from typing import Dict

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

    prog_bars: Dict[str, ft.ProgressRing] = {}
    files = ft.Ref[ft.Column]()
    upload_button = ft.Ref[ft.ElevatedButton]()
    attachment_files = []

    def file_picker_result(e: ft.FilePickerResultEvent):
        upload_button.current.disabled = True if e.files is None else False
        prog_bars.clear()
        files.current.controls.clear()
        if e.files is not None:
            for f in e.files:
                prog = ft.ProgressRing(value=0, bgcolor='#eeeeee', width=20, height=20)
                prog_bars[f.name] = prog
                files.current.controls.append(ft.Row([prog, ft.Text(f.name)]))
        page.update()

    def on_upload_progress(e: ft.FilePickerUploadEvent):
        prog_bars[e.file_name].value = e.progress
        prog_bars[e.file_name].update()

    file_picker = ft.FilePicker(on_result=file_picker_result, on_upload=on_upload_progress)

    def upload_files(e):
        uf = []
        if file_picker.result is not None and file_picker.result.files is not None:
            for f in file_picker.result.files:
                attachment_files.append("attachments/"+str(f.name))
                print(attachment_files)
                uf.append(
                    ft.FilePickerUploadFile(
                        f.name,
                        upload_url=page.get_upload_url(f.name, 600)
                    )
                )
            file_picker.upload(uf)
    
    # hiding dialog in an overlay
    page.overlay.append(file_picker)


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
        mail_status.value = send_email(to.value,subject.value,message.value,type_of_message,attachment_files)
        page.snack_bar.open = True
        page.update()

    homepage_content = ft.Column(
        [
            logo,
            to,
            subject,
            ft.Row([
                message_type,
                ft.ElevatedButton(
                    "Attachment",
                    icon=ft.icons.ATTACH_FILE,
                    on_click=lambda _: file_picker.pick_files(allow_multiple=True)
                ),
                ft.Column(
                    ref=files
                ),
                ft.ElevatedButton(
                    "Upload File(s)",
                    ref=upload_button,
                    icon=ft.icons.UPLOAD,
                    on_click=upload_files,
                    disabled=True
                )
            ],alignment="center"),
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
        alignment='center',
        horizontal_alignment='center',
    )

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
                        ft.Container(
                            content=homepage_content,
                            gradient=ft.LinearGradient(
                                begin=ft.alignment.top_center,
                                end=ft.alignment.bottom_center,
                                colors=[ft.colors.WHITE,'#dbeef7']
                            ),
                            border_radius=20,
                            padding=20
                        ),
                        
                    ],
                    scroll='always',
                    horizontal_alignment="center",
                    padding=0,
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


ft.app(target=main, assets_dir="assets", upload_dir="attachments")