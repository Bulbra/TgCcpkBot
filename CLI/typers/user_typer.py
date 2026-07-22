from typing_extensions import Annotated
import typer
from db import crud
import asyncio
from datetime import datetime
from CLI.typers.main_typer import app

users_app = typer.Typer(help="Приложение для обычных пользователей")
app.add_typer(users_app, name="users")


@users_app.command()
def sub(tg_id: Annotated[int, typer.Argument(help="Твой ай ди телеграмма, нужен для отправки информации в тг")],
        from_station_id: Annotated[int, typer.Argument(help="станция, откуда отправится поезд")],
        to_station_id: Annotated[int, typer.Argument(help="станция, куда приедет поезд")],
        origin_date: Annotated[str, typer.Argument(help="время отьезда поезда")],
          ):
    try:
        asyncio.run(crud.create_sub_by_user_tg_id(from_station_id, to_station_id,
                                              datetime.strptime(origin_date, "%Y-%m-%d %H:%M:%S"), tg_id))
    except Exception as e:
        print(f"Error in users_app, handler sub: {e}")
        return

if __name__ == '__main__':
    app()