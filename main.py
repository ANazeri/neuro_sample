import flet as ft

def main(page: ft.Page):
    page.title = "برنامه نمونه Flet"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    
    # تعریف یک متن
    text = ft.Text("به آکادمی پایتون خوش آمدید!", size=24, color="blue")
    
    # اضافه کردن به صفحه
    page.add(text)

ft.app(target=main)