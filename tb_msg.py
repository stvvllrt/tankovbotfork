#Список воозжможных сообщений.
from datetime import datetime, timedelta

can_after24 = "\nВы сможете крутануть свой кок ещё раз через 24 часа."

tb_not_found = "Команда или аргумент некорректны! Проверьте написание если уверены в наличии данного функционала."
startmsg = """Бот с функцией крутануть кок ✅
\nКанал с приколами если они будут: @tnkv_shitpost
Доступные команды:
<code>/кок</code>

Потом сделаю команды:
<code>/кок топ</code>
<code>/кок антитоп</code>

Обязательно напишу в щитпост, если не забуду"""

def wait(time):
    time = timedelta(seconds = time)
    return f"😐 Вы не можете крутануть свой кок, с момента последней прокрутки прошло менее 24х часов.\n✅ Осталось: {time}"

def profile(db_reg_date, db_cock_lenght, db_last_cock, db_old_cock):
    db_reg_date = f"{datetime.utcfromtimestamp(db_reg_date+(3600*3)).strftime('%Y-%m-%d %H:%M:%S')} МСК"
    db_last_cock = f"{datetime.utcfromtimestamp(db_last_cock+(3600*3)).strftime('%Y-%m-%d %H:%M:%S')} МСК"
    msg = f"""✅ Длина вашего кока: {db_cock_lenght}
🚀 Максимально отпавший кок: {db_old_cock}
💀 Дата последнего кручения: {db_last_cock}
🤓 Дата регистрации: {db_reg_date}"""
    return msg

def tb_indev(command: str):
    return f"""Команда "{command}" находится в разработке, или отключена."""

def cockmsg(deystv: str, num = 0):
    if deystv == "otval":
        return "🤯 | Ваш кок оторвался и улетел вдаль, пиздец...\nЕго длина была равна: " + str(num) + " см." + can_after24
    elif deystv == "x2":
        return "😎 | Ваш кок увеличился в два раза!\nТеперь его длина равна: " + str(num) + " см." + can_after24
    elif deystv == "+":
        return "➕ | Ваш кок увеличился на " + str(num)+ " см." + can_after24
    else:
        return "➖ | Ваш кок уменьшился на " + str(num)+ " см." + can_after24
