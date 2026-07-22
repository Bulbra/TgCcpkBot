from typing_extensions import Annotated
import typer
from db import crud
import asyncio
from CLI.typers.main_typer import app
admin_app = typer.Typer(help="Админское приложение, для запуска хэндлеров необходим пароль")
app.add_typer(admin_app, name="admin")

@admin_app.command()
def all_subs_info(
        password: Annotated[str, typer.Option(..., "-p", help="your password", prompt=True, confirmation_prompt=True, hide_input=True)]
        ):
    if password != "1006":
        print("Неверные данные")
        return
    try:
        subs = asyncio.run(crud.get_all_user_subs_with_join())
    except Exception as e:
        print(f"error in admin_app, handler all_subs_info: {e}")
        return
    for sub in subs:
        print(f"tgid: {sub.user_id} | to_station: {sub.to_station_id} | from_station: {sub.from_station_id} | "
              f"date: {sub.origin_date}")
if __name__ == '__main__':
    app()