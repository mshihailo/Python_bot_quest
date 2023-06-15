import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Инициализация логгера
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Глобальные переменные
crime_scene_objects = ["НИФ-НИФ", "НАФ-НАФ", "НУФ-НУФ", "комнату"]
current_object_index = 0
evidences = {
    "НИФ-НИФ": {"объект": "кровь", "следы": "отсутствуют"},
    "НАФ-НАФ": {"объект": "кровь", "следы": "деодорант"},
    "НУФ-НУФ": {"объект": "тело", "следы": "деодорант"}
}
clues = {
    "НАФ-НАФ": {"объект": "топор", "следы": "отпечатки НАФ-НАФа и материал перчаток НАФ-НАФа"},
    "комнату": {"объект": "топор", "следы": "отпечатки НАФ-НАФа и материал перчаток НАФ-НАФа"}
}

# Обработка команды /start
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Добро пожаловать! Вас зовут мистер/мисс Монтгомери. Вы родом из поместья Гарденвил. В своём округе вы достаточно известный детектив с опытом более двадцати лет. Все эти годы вы были вынуждены браться за элементарные и очень скучные дела, т.к. альтернативы не было ввиду того, что ваш город был тихим поселением аристократов. Однако сегодня, разбирая почту, вам в руки попалось пакет с делом 50-ти летней давности. Описание происшествия вас заинтересовало, т.к. последние два дела подозрительно откликались с сюжетом вашей находки…\n\n'
    'Полгода назад: К вам пришло таинственное письмо. Джефферсон, автор письма, обратился с требованием расследовать убийство НИФ-НИФа в течение суток. Вас это озадачило, но любопытство взяло верх, и вы отправились за город по указанному адресу. В развалившейся старой усадьбе вы находите телефон с громко тикающем таймером и три тела, к грудным клеткам которых прибиты таблички с подписями. У первого отсутствовала голова, табличка гласила: “НИФ-НИФ”. Два других трупа были отравлены примерно в одно время. У одного из них была табличка “НАФ-НАФ”, у другого - “НУФ-НУФ”. Вы взяли отпечатки пальцев и начали расследование.")

# Обработка команды /help
def help(update , context):
context.bot.send_message(chat_id=update.effective_chat.id, text="Для продолжения расследования отправьте команду /search.")
Обработка команды /search
def search(update, context):
global current_object_index
if current_object_index >= len(crime_scene_objects):
context.bot.send_message(chat_id=update.effective_chat.id, text="Вы прошли все этапы расследования. Отправьте команду /answer, чтобы получить ответ.")
else:
current_object = crime_scene_objects[current_object_index]
context.bot.send_message(chat_id=update.effective_chat.id, text="Исследовать " + current_object + "?")
current_object_index += 1

# Обработка команды /suspect
def suspect(update, context):
suspects = "Список подозреваемых:\n\n- Джефферсон: автор таинственного письма\n- НИФ-НИФ: жертва убийства\n- НАФ-НАФ: обладатель отпечатков на топоре и следов дезодоранта на рубашке НУФ-НУФа\n- НУФ-НУФ: обладатель перчаток с отпечатками НАФ-НАФа"
context.bot.send_message(chat_id=update.effective_chat.id, text=suspects)

#Обработка текстового сообщения пользователя
def process_text_message(update, context):
message = update.message.text.lower()

if message == "исследовать все":
    current_object_index = len(crime_scene_objects)
    search(update, context)
elif message == "ответ":
    context.bot.send_message(chat_id=update.effective_chat.id, text="Ответ: убийство совершил НАФ-НАФ.")
elif message in crime_scene_objects:
    if message == "НИФ-НИФ":
        context.bot.send_message(chat_id=update.effective_chat.id, text="Осмотреть " + message + ":\n1. Взят образец крови.\n2. Голова была отрублена топором.")
    elif message == "НАФ-НАФ":
        context.bot.send_message(chat_id=update.effective_chat.id, text="Осмотреть " + message + ":\n1. На рубашке пятно крови.\n2. На рубашке следы дезодоранта.")
    elif message == "НУФ-НУФ":
        context.bot.send_message(chat_id=update.effective_chat.id, text="Осмотреть " + message + ":\n1. На теле найдены следы дезодоранта.\n2. В кармане брюк обнаружены перчатки с фрагментами отпечатков НАФ-НАФа на внешней стороне.")
    elif message == "комнату":
        context.bot.send_message(chat_id=update.effective_chat.id, text="Осмотреть " + message + ":\n1. Найден топор с отпечатками НАФ-НАФа.")
    
    context.bot.send_message(chat_id=update.effective_chat.id, text="Исследовать все объекты или дать ответ?")
elif message in ["1.1", "1.2", "2.1.1", "2.2.1", "3.2", "4.2"]:
    context.bot.send_message(chat_id=update.effective_chat.id, text="Исследовать место преступления или дать ответ?")
elif message == "2.1":
    context.bot.send_message(chat_id=update.effective_chat.id, text="Исследовать кровь или дать ответ?")
elif message == "2.2":
    context.bot.send_message(chat_id=update.effective_chat.id, text="Исследовать тело на наличие следов дезодоранта или дать ответ?")
elif message == "3.1":
    context.bot.send_message(chat_id=update.effective_chat.id, text="Исследовать НУФ-НУФ по перчаткам или дать ответ?")
elif message == "4.1":
context.bot.send_message(chat_id=update.effective_chat.id, text="Исследовать топор или дать ответ?")
else:
context.bot.send_message(chat_id=update.effective_chat.id, text="Команда не распознана. Отправьте команду /search, чтобы продолжить расследование.")

#Точка входа в программу
def main():
# Инициализация бота
updater = Updater(token='YOUR_BOT_TOKEN', use_context=True)

# Регистрация обработчиков команд и текстовых сообщений пользователя
start_handler = CommandHandler('start', start)
help_handler = CommandHandler('help', help)
search_handler = CommandHandler('search', search)
suspect_handler = CommandHandler('suspect', suspect)
message_handler = MessageHandler(Filters.text & (~Filters.command), process_text_message)
updater.dispatcher.add_handler(start_handler)
updater.dispatcher.add_handler(help_handler)
updater.dispatcher.add_handler(search_handler)
updater.dispatcher.add_handler(suspect_handler)
updater.dispatcher.add_handler(message_handler)

# Запуск бота
updater.start_polling()
updater.idle()
if name == 'main':
main()
