*Будущая структура проекта:*

*Файлы:*\
app.py\
loader.py\
ccpk_class.py\
checking_scheduler.py

*Директории*:\
handlers\
keyboards\
states\
db

*Описание файлов*:\
app.py - файл для запуска бота\
loader.py - добавление роутеров в диспетчера\
ccpk_class.py - класс с api-функциями для получения данных\
checking_scheduler.py - файл с APScheduler, проверяющий наличие мест

*Описание директорий*:\
handlers - нужна для хранения в ней handler'ов\
keyboards - хранение inline-клавиатур и callback_data для них\
states - хранение состояний\
db - содержит crud, models и engine
