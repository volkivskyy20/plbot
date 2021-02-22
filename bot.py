# - *- coding: utf- 8 - *-


import telebot
from telebot import types
import sys
import configure

sys.setdefaultencoding('utf-8')

bot = telebot.TeleBot(configure.config['token'], parse_mode='Markdown')
name = ''
number = ''


@bot.message_handler(commands=['start'])
def start_message(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    key1 = types.InlineKeyboardButton(text='Замовити дзвінок', callback_data='key1')
    key2 = types.InlineKeyboardButton(text="Часті запитання", callback_data='key2')
    key3 = types.InlineKeyboardButton(text="Перелік документів які надаються", callback_data='key3')
    key4 = types.InlineKeyboardButton(text="Відкриття банківського рахунку", callback_data='key4')
    key5 = types.InlineKeyboardButton(text="Банківські рахунки", callback_data='key5')
    key6 = types.InlineKeyboardButton(text="Подати заявку", callback_data='key6')
    key7 = types.InlineKeyboardButton(text="Карта Побуту ", callback_data='key7')
    key8 = types.InlineKeyboardButton(text="Що буде, якщо не платити податки вчасно", callback_data='key8')

    keyboard.add(key1)
    keyboard.add(key2)
    keyboard.add(key3)
    keyboard.add(key4)
    keyboard.add(key5)
    keyboard.add(key6)
    keyboard.add(key7)
    keyboard.add(key8)

    # bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=keyboard)
    bot.send_animation(chat_id=message.chat.id, animation=open('img/ss.gif', 'rb'), duration='5')

    bot.send_message(message.chat.id,
                     text='Вітаю\n тут ви зможете отримати відповіді на питання, як продовжити перебування і '
                          'працевлаштування після закінчення легальних документів',
                     reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data == "mainmenu":
        mainmenu = telebot.types.InlineKeyboardMarkup()
        key1 = types.InlineKeyboardButton(text='Замовити дзвінок', callback_data='key1')
        key2 = types.InlineKeyboardButton(text="Питання та відповіді", callback_data='key2')
        key3 = types.InlineKeyboardButton(text="Перелік документів які надаються", callback_data='key3')
        key4 = types.InlineKeyboardButton(text="Відкриття банківського рахунку", callback_data='key4')
        key5 = types.InlineKeyboardButton(text="Банківські рахунки", callback_data='key5')
        key6 = types.InlineKeyboardButton(text="Подати заявку", callback_data='key6')
        key7 = types.InlineKeyboardButton(text="Карта Побиту (дозвіл на тимчасове проживання)", callback_data='key7')
        key8 = types.InlineKeyboardButton(text="Про нас", callback_data='key8')
        mainmenu.add(key1)
        mainmenu.add(key2)
        mainmenu.add(key3)
        mainmenu.add(key4)
        mainmenu.add(key5)
        mainmenu.add(key6)
        mainmenu.add(key7)
        mainmenu.add(key8)
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=mainmenu)

    elif call.data == 'poznan':
        key = telebot.types.InlineKeyboardMarkup()
        key.add(telebot.types.InlineKeyboardButton(text="назад", callback_data="bank"))
        bot.send_message(chat_id=call.message.chat.id,
                         text='(Urząd Miasta Poznania\nWydział Finansowy\nOddział Pozostałych Dochodów '
                              'Podatkowych i Niepodatkowych\nul. Libelta 16/20 61-706 Poznań\nNr rachunku: 94 '
                              '1020 4027 0000 1602 1262 0763 )',
                         reply_markup=key)

    elif call.data == 'warsaw':
        g = telebot.types.InlineKeyboardMarkup()
        g.add(telebot.types.InlineKeyboardButton(text="назад", callback_data="bank"))
        bot.send_message(chat_id=call.message.chat.id,
                         text='(Centrum Obsługi Podatnika\nul. Obozowa 57, 01-161 Warszawa\n21 1030 1508 0000 '
                              '0005 5000 0070)',
                         reply_markup=g)
    elif call.data == 'wroclaw':
        ke = telebot.types.InlineKeyboardMarkup()
        ke.add(telebot.types.InlineKeyboardButton(text="назад", callback_data="bank"))
        bot.send_message(chat_id=call.message.chat.id,
                         text='(Gmina Wrocław, Plac Nowy Targ 1/8, 50-141 Wrocław \nPKO BP S.A. nr 82 1020 5226 '
                              '0000 6102 0417 7895)',
                         reply_markup=ke)
    elif call.data == 'krakow':
        k = telebot.types.InlineKeyboardMarkup()
        k.add(telebot.types.InlineKeyboardButton(text="назад", callback_data="bank"))
        bot.send_message(chat_id=call.message.chat.id,
                         text='(Wydział Podatków i Opłat UMK\nPKO Bank Polski S.A.\n49 1020 2892 2276 3005 0000 '
                              '0000)',
                         reply_markup=k)
    elif call.data == 'bank':
        ba = telebot.types.InlineKeyboardMarkup()
        key17 = types.InlineKeyboardButton(text='Банківський рахунок Уженду у Познані', callback_data='poznan')
        key18 = types.InlineKeyboardButton(text='Банківський рахунок Уженду у Варшаві', callback_data='warsaw')
        key19 = types.InlineKeyboardButton(text='Банківський рахунок Уженду у Вроцлаві', callback_data='wroclaw')
        key20 = types.InlineKeyboardButton(text='Банківський рахунок Уженду у Кракові', callback_data='krakow')
        key21 = types.InlineKeyboardButton(text='Назад', callback_data='key6')
        ba.add(key17)
        ba.add(key18)
        ba.add(key19)
        ba.add(key20)
        ba.add(key21)
        bot.send_message(call.message.chat.id, "( Вибираєте тільки рахунок того Уженду в який будете подавати свою "
                                               "справу. \n У разі оплати на рахунок не вашого Уженду, Ви можете "
                                               "написати "
                                               "заяву про повернення коштів і вам їх повернуть, але слід розуміти, "
                                               "що розгляд такого повернення може тривати декілька місяців. Слід "
                                               "бути уважним !",
                         reply_markup=ba)
    elif call.data == 'key1':

        poll = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        key88 = types.KeyboardButton(text="Далі")
        poll.add(key88)
        bot.send_photo(chat_id=call.message.chat.id, photo=open('img/oder_call.jpg', 'rb'))
        bot.send_message(call.message.chat.id, "<b>Зараз потрібно буде ввести ваше ім'я та ваш номер телефону</b>",
                         reply_markup=poll, parse_mode="HTML")
        key = telebot.types.InlineKeyboardMarkup()
        key.add(telebot.types.InlineKeyboardButton(text="назад", callback_data="mainmenu"))

        @bot.message_handler(content_types=['text'])
        def get_text_messages(message):

            bot.send_message(message.chat.id, "Будь-ласка введіть ваше ім'я")
            bot.register_next_step_handler(message, get_name)

        def get_name(message):
            global name
            name = message.text
            bot.send_message(message.from_user.id, 'Будь-ласка введіть ваш номер телефону у форматі +380ХХХХХХХХХ')
            bot.register_next_step_handler(message, get_number)

        def get_number(message):
            global number
            number = message.text
            bot.send_message(917722215, "Ім'я:\n" + name + " \n" + "Номер телефону\n" + str(number))
            bot.send_message(message.chat.id, "Дякую, найближчим часом з вами зв'яжуться", reply_markup=key)

    elif call.data == 'post':
        pos = telebot.types.InlineKeyboardMarkup()
        pos1 = types.InlineKeyboardButton(text="Варшава", callback_data='WAW')
        pos2 = types.InlineKeyboardButton(text="Познань", callback_data='POZ')
        pos3 = types.InlineKeyboardButton(text="Краків", callback_data='KRV')
        pos4 = types.InlineKeyboardButton(text="Вроцлав", callback_data='WRC')
        pos5 = types.InlineKeyboardButton(text='Назад', callback_data='yzhden')
        pos.row(pos1, pos2)
        pos.row(pos3, pos4)
        pos.add(pos5)
        #
        bot.send_message(chat_id=call.message.chat.id, text="Зібравши всі необхідні документи (оригінали і їх копії), "
                                                            "ви повинні заповнити 2 бланки (бланки знаходяться у "
                                                            "відділенні пошти) у відділенні Poczta Polska, а також сам "
                                                            "конверт. Конверт можете взяти в самому відділенні пошти і "
                                                            "уже при відправленні оплатити. Марки вклеює працівник "
                                                            "пошти і окремо купувати не потрібно.\nКонверт заповнюєте "
                                                            "по звичайній схемі ( зліва вверху пишете своє ПІБ, "
                                                            "вулицю, номер дому/квартири/кімнати, код поштовий і "
                                                            "місто). Внизу з правого боку по такій же аналогії пишите "
                                                            "повний адрес Отримувача. ")
        bot.send_photo(chat_id=call.message.chat.id, photo=open('img/post1.jpg', 'rb'))
        bot.send_message(chat_id=call.message.chat.id, text="Всі дані вказувати свої , обов'язковими вимогами є "
                                                            "відмітка в пунктах ( priorytetowa, potwierdzenie "
                                                            "doręczenia albo zwrotu, potwierdzenie odbioru).Стосовно "
                                                            "вибору формату ( S, M, L ) то ці дані вказує працівник "
                                                            "пошти.")
        bot.send_photo(chat_id=call.message.chat.id, photo=open('img/post2.jpg', 'rb'))
        bot.send_message(chat_id=call.message.chat.id, text="Сюди вписуєте ті ж дані, що і у попередньому бланку:\n "
                                                            "В графі Adresat - пишете адрес Ужонду\n в графі Zwrócić "
                                                            " do Vacancy - пишете свій адрес \n І ставите відмітку в "
                                                            "графі ( przesyłka polecona )\n На обороті, "
                                                            "в графі ( Miejsce na dodatkowe informacje Nadawcy ) "
                                                            "напишіть - Wniosek na zezwolenie na pobyt czasowy.")
        bot.send_photo(chat_id=call.message.chat.id, photo=open('img/post3.jpg', 'rb'))
        bot.send_message(chat_id=call.message.chat.id, text="Рекомендації стосовно надсилання документів на карту "
                                                            "побиту за допомогою пошти :\n1. Кожна справа повинна "
                                                            "надсилатися в окремому конверті, тому ви не можете "
                                                            "об'єднувати справи своїх знайомих або родичів.\n2. "
                                                            "Листи повинні бути тільки polecone - це значить, "
                                                            "що поштар передасть ваші документи особисто в "
                                                            "відповідний відділ Ужонду. Не рекомендується надсилати "
                                                            "через звичайну поштову скриньку, адже в такому випадку "
                                                            "зростає ймовірність втрати вашого листа.\n 3. В Бланку "
                                                            "№ 1 вказуйте свій контактний номер ( якщо у вас є "
                                                            "польський номер) або адрес електронної пошти, "
                                                            "тоді ви отримаєте смс сповіщення про доставлення вашого "
                                                            "листа.\n 4. Після 2-3 тижнів після надсилання "
                                                            "документів зателефонуйте або напишіть на електронну "
                                                            "адресу до вашого Ужонду і запитайте чи ваша справа уже "
                                                            "зареєстрована і чи просвоєний їй певний номер. Також "
                                                            "запитуйте чи можлива реєстрація на візит в Ужонд на "
                                                            "найблищий час задля отримання відмітки в паспорт. ",
                         reply_markup=pos)

    elif call.data == 'WAW':
        wa = telebot.types.InlineKeyboardMarkup()
        wa1 = types.InlineKeyboardButton(text='Назад', callback_data='post')
        wa.add(wa1)
        bot.send_message(chat_id=call.message.chat.id, text="Mazowiecki Urząd Wojewódzki w Warszawie\nWydział Spraw "
                                                            "Cudzoziemców\nul. "
                                                            "Marszałkowska 3/5\n00-624 Warszawa", reply_markup=wa)
    elif call.data == 'WRC':
        w = telebot.types.InlineKeyboardMarkup()
        w1 = types.InlineKeyboardButton(text='Назад', callback_data='post')
        w.add(w1)
        bot.send_message(chat_id=call.message.chat.id,
                         text="Dolnośląski Urząd Wojewódzki\nWydział Spraw Obywatelskich\ni "
                              "Cudzoziemców\npl. Powstańców Warszawy 1\n50-153 Wrocław",
                         reply_markup=w)

    elif call.data == 'POZ':
        po = telebot.types.InlineKeyboardMarkup()
        po1 = types.InlineKeyboardButton(text='Назад', callback_data='post')
        po.add(po1)
        bot.send_message(chat_id=call.message.chat.id,
                         text="Wielkopolski Urząd Wojewódzki w Poznaniu\nWydział Spraw Cudzoziemców\npl. "
                              "Wolności 17\n61-739 Poznań", reply_markup=po)
    elif call.data == 'KRV':
        kr = telebot.types.InlineKeyboardMarkup()
        kr1 = types.InlineKeyboardButton(text='Назад', callback_data='post')
        kr.add(kr1)
        bot.send_message(chat_id=call.message.chat.id,
                         text="Małopolski  Urząd Wojewódzki w Krakowie \nWydział Spraw Cudzoziemców\nul. "
                              "Przy Rondzie 6\n31-547 Kraków ", reply_markup=kr)

    elif call.data == "mail":
        ma = telebot.types.InlineKeyboardMarkup()
        ma1 = types.InlineKeyboardButton(text='Краков',
                                         url='https://www.malopolska.uw.gov.pl/default.aspx?page=rezerwacja')
        ma2 = types.InlineKeyboardButton(text='Познань', url='https://www.poznan.uw.gov.pl/rejestracja')
        ma3 = types.InlineKeyboardButton(text='Варшава', url='https://kolejka-wsc.mazowieckie.pl/rezerwacje/pol/login')
        ma4 = types.InlineKeyboardButton(text='Вроцлав', url='https://rezerwacje.duw.pl/reservations/pol/login')
        ma5 = types.InlineKeyboardButton(text='Назад', callback_data='yzhden')
        ma6 = types.InlineKeyboardButton(text='Інфолінія', callback_data='info')
        ma.row(ma1, ma2)
        ma.row(ma3, ma4)
        ma.add(ma6)
        ma.add(ma5)
        bot.send_message(chat_id=call.message.chat.id, text="Реєстрація на візит в Ужонд для отримання штампу в "
                                                            "паспорті про очікування на карту побиту\n ( Звертаємо "
                                                            "Вашу увагу на необхідність моніторингу офіційних сайтів "
                                                            "ваших Ужендів, там публікують актуальну інформацію щодо "
                                                            "змін і нових правил оформлення документів. Кожна справа є "
                                                            "індивідуальна і розглядається іншим інспектором Уженду. "
                                                            "Отже пам’ятайте, що стан справи, швидкість і позитивний "
                                                            "результат розгляду Вашої справи залежить тільки від Вас і "
                                                            "Вашої наполегливості.)", reply_markup=ma)

    elif call.data == 'info':
        fr = telebot.types.InlineKeyboardMarkup()
        fr1 = types.InlineKeyboardButton(text="Назад ", callback_data='mail')
        fr.add(fr1)

        bot.send_message(call.message.chat.id, text="Краків \n +48122102020 \n "
                                                    "email: info.opt@malopolska.uw.gov.pl \n\n Вроцлав \n "
                                                    "+480801430086 \n Umawianie wizyt na złożenie wniosku o "
                                                    "legalizację pobytu tymczasowego \n od godziny 10.00 do 14.00 "
                                                    "\n\n "
                                                    "Варшава\n+48226956770\n+48226956669\n+48723996079\n+48723997290"
                                                    "\n "
                                                    "e-mail: info@mazowieckie.pl \n\n Познань\n+48618508777",
                         reply_markup=fr)

    elif call.data == 'yzhden':
        fur = telebot.types.InlineKeyboardMarkup()
        fur1 = types.InlineKeyboardButton(text="За допомогою пошти ", callback_data='post')
        fur2 = types.InlineKeyboardButton(text=" Зареєструвати візит в Ужонд за допомогою електронної адреси ",
                                          callback_data='mail')
        fur3 = types.InlineKeyboardButton(text="Назад", callback_data='key2')
        fur.add(fur1)
        fur.add(fur2)
        fur.add(fur3)
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=fur)

    elif call.data == 'voevod':
        po = telebot.types.InlineKeyboardMarkup()
        po1 = types.InlineKeyboardButton(text='Назад', callback_data='key2')
        po.add(po1)
        bot.send_message(chat_id=call.message.chat.id,
                         text="1. Час очікування від 2 місяців, за допомогою якого Ви зможете в Україні відкрити "
                              "річну візу ( попереджати завчасно)", reply_markup=po)

    elif call.data == 'zap180':
        po = telebot.types.InlineKeyboardMarkup()
        po1 = types.InlineKeyboardButton(text='Назад', callback_data='key2')
        po.add(po1)
        bot.send_message(chat_id=call.message.chat.id,
                         text="( час очікування на електронну версію 2 тижні, час очікування на оригінал - 4 тижні ) "
                              "- актуальне лише у випадку, якщо впродовж останніх 180 днів Ви не працювали, "
                              "по такого типу запрошеннях", reply_markup=po)

    elif call.data == 'bezviz':
        po = telebot.types.InlineKeyboardMarkup()
        po1 = types.InlineKeyboardButton(text='Назад', callback_data='key2')
        po.add(po1)
        bot.send_message(chat_id=call.message.chat.id,
                         text="Після закінчення візи Ви можете, без виїзду, працювати і перебувати по безвізу 90 "
                              "днів.днів ( Задля уникнення депортації чи інших негативних наслідків Ви повинні чітко "
                              "знати кількість днів які у вас залишились по біометрії ).",
                         reply_markup=po)

    elif call.data == 'dogovir':
        po = telebot.types.InlineKeyboardMarkup()
        po1 = types.InlineKeyboardButton(text='Назад', callback_data='key2')
        po.add(po1)
        bot.send_message(chat_id=call.message.chat.id,
                         text="Задля уникнення штрафів, Вам необхідно повідомити нас за 14 днів до останнього дня "
                              "праці (Кожен невихід до праці, повинен бути підтверджений довідкою від лікаря, "
                              "або попередньо узгоджений з лідером, координатором агенції мінімум за добу)\nВиплата "
                              "зарплати тільки на польський рахунок  до 20 числа наступного місяця.", reply_markup=po)

    elif call.data == 'q1':
        po = telebot.types.InlineKeyboardMarkup()
        po1 = types.InlineKeyboardButton(text='Назад', callback_data='questions')
        po.add(po1)
        bot.send_message(chat_id=call.message.chat.id,
                         text="Обов'язково : \n -	фото першої сторінки закордонного паспорт\n -	фото візи \n -	"
                              "контактний телефон ( польський номер, або Viber) \n -	карта побиту (фото з двох "
                              "сторін) \n Примітка: фото чітке, не розмите, робиться на білому тлі, паспорт повинен "
                              "бути в розгорнутому вигляді, ніяких тіней, рук та іншого. Кожна сторінка повинна "
                              "поміститися повністю на фото.", reply_markup=po)

    elif call.data == 'q2':
        po = telebot.types.InlineKeyboardMarkup()
        po1 = types.InlineKeyboardButton(text='Назад', callback_data='questions')
        po.add(po1)
        bot.send_message(chat_id=call.message.chat.id,
                         text="-	90 днів по безвізу \n -    180 днів по візі D-05\nНа підставі 'Oświadczenie' не "
                              "більше 180 днів на рік, період виконання роботи іноземцем не може перевищувати 6 "
                              "місяців протягом 12-ти місяців, в незалежності від кількості роботодавців які "
                              "довіряють йому роботу на підставі запрошення. \n -    Воєводська віза відкривається на "
                              "1 рік протягом якого ви можете легально працювати у роботодавця який відкрив цю візу."
                         , reply_markup=po)

    elif call.data == 'q3':
        po = telebot.types.InlineKeyboardMarkup()
        po1 = types.InlineKeyboardButton(text='Назад', callback_data='questions')
        po.add(po1)
        bot.send_message(chat_id=call.message.chat.id,
                         text="Якщо між Oświadczenie пройшов коридор в 180 днів, ми можемо працевлаштовувати по "
                              "воєводі, в такому випадку ви повинні подавати менеджеру фото візи і виреєструвати всі "
                              "освядчення від попередніх працедавців. ( Обов’язково вимагайте попереднього працедавця "
                              "виреєструвати освядчення одразу по завершенню праці, адже ми не зможемо вас "
                              "зареєструвати від себе.). "
                         , reply_markup=po)

    elif call.data == 'q4':
        po = telebot.types.InlineKeyboardMarkup()
        po1 = types.InlineKeyboardButton(text='Назад', callback_data='questions')
        po.add(po1)
        bot.send_message(chat_id=call.message.chat.id,
                         text="-     біометрія \n  -     віза\n -     воєвода \n -     сезонна Віза \n -     карта "
                              "побиту (печатка) "
                         , reply_markup=po)

    elif call.data == 'q5':
        po = telebot.types.InlineKeyboardMarkup()
        po1 = types.InlineKeyboardButton(text='Назад', callback_data='questions')
        po.add(po1)
        bot.send_message(chat_id=call.message.chat.id,
                         text="Зарплата на банківський рахунок працівника до 20 числа ,на багатьох вакансіях можна "
                              "брати аванс від 100 злотих. "
                         , reply_markup=po)

    elif call.data == 'q6':
        po = telebot.types.InlineKeyboardMarkup()
        po1 = types.InlineKeyboardButton(text='Назад', callback_data='questions')
        po.add(po1)
        bot.send_message(chat_id=call.message.chat.id,
                         text="Ми доплачуємо від 150 до 300 злотих (в залежності від вакансії) , якщо працівник сам "
                              "знімає своє житло. "
                         , reply_markup=po)

    elif call.data == 'q7':
        po = telebot.types.InlineKeyboardMarkup()
        po1 = types.InlineKeyboardButton(text='Назад', callback_data='questions')
        po.add(po1)
        bot.send_message(chat_id=call.message.chat.id,
                         text="Вибирати зміни не можна, є графік на виробництві якому всі слідують."
                         , reply_markup=po)

    elif call.data == 'q8':
        po = telebot.types.InlineKeyboardMarkup()
        po1 = types.InlineKeyboardButton(text='Назад', callback_data='questions')
        po.add(po1)
        bot.send_message(chat_id=call.message.chat.id,
                         text="У нас багато хостелів/квартир в кожному місті де ми надаємо вакансію \n "
                              "Хостели/Квартири з усіма зручностями, роздільні кімнати, завжди є гаряча вода та "
                              "інтернет. "
                         , reply_markup=po)

    elif call.data == 'q9':
        po = telebot.types.InlineKeyboardMarkup()
        po1 = types.InlineKeyboardButton(text='Назад', callback_data='questions')
        po.add(po1)
        bot.send_message(chat_id=call.message.chat.id,
                         text="По можливості ми робимо фото з місця роботи, але в більшості випадків це заборонено "
                              "керівництвом заводу як розголошення комерційної таємниці. "
                         , reply_markup=po)

    elif call.data == 'q10':
        po = telebot.types.InlineKeyboardMarkup()
        po1 = types.InlineKeyboardButton(text='Назад', callback_data='questions')
        po.add(po1)
        bot.send_message(chat_id=call.message.chat.id,
                         text="‘У Польщі існує два поняття для позначення заробітної плати працівника - це зарплата "
                              "брутто і зарплата нетто.\n Зарплата брутто - це сума заробітної плати працівника без "
                              "урахування податку. \n Зарплата нетто - це сума, яку працівник отримує після "
                              "вирахування всіх внесків і податків із зарплати брутто. Фактично, зарплата нетто "
                              "становить 73% від з/п брутто. Решта 27% надходить до скарбниці Польщі.’\n Ми в "
                              "більшості своїх вакансій вказуємо ЗП в Нетто. (уважно читайте). "
                         , reply_markup=po)

    elif call.data == 'q11':
        po = telebot.types.InlineKeyboardMarkup()
        po1 = types.InlineKeyboardButton(text='Назад', callback_data='questions')
        po.add(po1)
        bot.send_message(chat_id=call.message.chat.id,
                         text="‘Очікування виготовлення Oświadczenie від 7-10 робочих днів, краще щоб людина "
                              "виїжджала по своєму освядчению і не витрала дні безвізу в Польщі на очікування своїх "
                              "документів. "
                         , reply_markup=po)

    elif call.data == 'q12':
        po = telebot.types.InlineKeyboardMarkup()
        po1 = types.InlineKeyboardButton(text='Назад', callback_data='questions')
        po.add(po1)
        bot.send_message(chat_id=call.message.chat.id,
                         text="Ми намагаємося завжди селити пари разом (двоє в одній кімнаті), але і бувають винятки "
                              "коли не вистачає місця можемо поселити по 2 пари, а пізніше розселяти їх по одній. "
                         , reply_markup=po)

    elif call.data == 'q13':
        po = telebot.types.InlineKeyboardMarkup()
        po1 = types.InlineKeyboardButton(text='Назад', callback_data='questions')
        po.add(po1)
        bot.send_message(chat_id=call.message.chat.id,
                         text="- Україна \n - Молдова\n - Білорусь \n - Росія \n - Грузія"
                         , reply_markup=po)
    elif call.data == 'q14':
        po = telebot.types.InlineKeyboardMarkup()
        po2 = types.InlineKeyboardButton(text='Oświadczenie (піврічне)', callback_data='piv')
        po3 = types.InlineKeyboardButton(text='Zezwolenie (річне)', callback_data='rik')
        po1 = types.InlineKeyboardButton(text='Назад', callback_data='questions')
        po.add(po2)
        po.add(po3)
        po.add(po1)
        bot.send_message(chat_id=call.message.chat.id,
                         text="Для роботи в Польщі іноземцю потрібен дозвіл для роботи: Oświadczenie або Zezwolenie. "
                              "Багато людей помилково думають, що це один і той же документ, або не знають в чому їх "
                              "основні відмінності.\n Важливо знати: \n-	Якщо ви хочете працювати на кількох "
                              "роботодавців одночасно, кожен з них повинен на вас отримати відповідний дозвіл; \n -	"
                              "Oświadczenie дозволяє працювати протягом 180 днів протягом кожних 12 місяців, тобто, "
                              "відпрацювавши пів року чекати ще 6 місяців (так званий піврічний коридор); \n -	"
                              "Роботодавець має право анулювати дозвіл на роботу;\n -	У разі втрати дозволу, "
                              "можна попросити копію з особової справи у відділі кадрів, завірену фірмовою печаткою, "
                              "але держустанови не видають дублікати або копії документів. "
                         , reply_markup=po)

    elif call.data == 'piv':
        po = telebot.types.InlineKeyboardMarkup()
        po1 = types.InlineKeyboardButton(text='Назад', callback_data='q14')
        po.add(po1)
        bot.send_message(chat_id=call.message.chat.id,
                         text="Такий документ реєструється роботодавцем в центрі зайнятості (Urząd Pracy) протягом "
                              "від 7-10 днів. \n Такий документ дозволяє відкрити візу терміном на рік, але працювати "
                              "та перебувати можна не більше 180 днів, що починаються від дня перетину польського "
                              "кордону. "
                         , reply_markup=po)

    elif call.data == 'rik':
        po = telebot.types.InlineKeyboardMarkup()
        po1 = types.InlineKeyboardButton(text='Назад', callback_data='q14')
        po.add(po1)
        bot.send_message(chat_id=call.message.chat.id,
                         text="Такий тип документа оформляється в воєводському управлінні (Urząd Wojewódzki) протягом "
                              "від 2 до 6 місяців. Основна перевага даного документа полягає тому, що консул не може "
                              "відмовити у візі на підставі такого запрошення (якщо на це немає вагомих причин). "
                              "Також воно скасовує коридор від попередньої візи "
                         , reply_markup=po)


    elif call.data == 'questions':
        bt = telebot.types.InlineKeyboardMarkup()
        bt1 = types.InlineKeyboardButton(text='Oświadczenie і Zezwolenie: в чому різниця? ', callback_data='q14')
        bt2 = types.InlineKeyboardButton(text='Документи для наших вакансій ?', callback_data='q1')
        bt3 = types.InlineKeyboardButton(text='Офіційний термін роботи в Польщі', callback_data='q2')
        bt4 = types.InlineKeyboardButton(text='Працевлаштовування по воєводі ?', callback_data='q3')
        bt5 = types.InlineKeyboardButton(text='Документи для працевлання ?', callback_data='q4')
        bt6 = types.InlineKeyboardButton(text='Як нараховують зарплату працівникам ?', callback_data='q5')
        bt7 = types.InlineKeyboardButton(text='Чи доплачують, якщо є своє житло?', callback_data='q6')
        bt8 = types.InlineKeyboardButton(text='Вибір денних/нічних змін?', callback_data='q7')
        bt9 = types.InlineKeyboardButton(text='Фото житла', callback_data='q8')
        bt10 = types.InlineKeyboardButton(text='Фото з місця роботи', callback_data='q9')
        bt11 = types.InlineKeyboardButton(text='Що таке зарплата брутто/нетто?', callback_data='q10')
        bt12 = types.InlineKeyboardButton(text='Коли можна виїжджати по біометрії?', callback_data='q11')
        bt13 = types.InlineKeyboardButton(text='Як проживають пари?', callback_data='q12')
        bt14 = types.InlineKeyboardButton(text='Громадян яких країн ми працевлаштовуємо?', callback_data='q13')
        bt15 = types.InlineKeyboardButton(text='Назад', callback_data='key2')
        bt.add(bt1)
        bt.add(bt2)
        bt.add(bt3)
        bt.add(bt4)
        bt.add(bt5)
        bt.add(bt6)
        bt.add(bt7)
        bt.add(bt8)
        bt.add(bt9)
        bt.add(bt10)
        bt.add(bt11)
        bt.add(bt12)
        bt.add(bt13)
        bt.add(bt14)
        bt.add(bt15)
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=bt)

    elif call.data == 'key2':

        por = telebot.types.InlineKeyboardMarkup()
        por0 = types.InlineKeyboardButton(text="відповіді на поширені запитання ",
                                          callback_data='questions')
        por1 = types.InlineKeyboardButton(text='Як надіслати документи до Ужендів ?', callback_data='yzhden')
        por2 = types.InlineKeyboardButton(text='Воєводське запрошення на рік', callback_data='voevod')
        por3 = types.InlineKeyboardButton(text='Запрошення на 180 днів', callback_data='zap180')
        por4 = types.InlineKeyboardButton(text='Безвіз', callback_data='bezviz')
        por5 = types.InlineKeyboardButton(text='Договір', callback_data='dogovir')
        por6 = types.InlineKeyboardButton(text='Що таке PIT-11?', callback_data='pit11')
        por7 = types.InlineKeyboardButton(text='Що таке PIT-37?', callback_data='pit37')
        por8 = types.InlineKeyboardButton(text='Форма IFT - 1 і IFT-1R ', callback_data="form")
        por10 = types.InlineKeyboardButton(text="Запрошення і біометрія", callback_data="zap")

        por9 = types.InlineKeyboardButton(text='Назад', callback_data='mainmenu')
        por.add(por0)
        por.add(por1)
        por.add(por2)
        por.add(por3)
        por.add(por4)
        por.add(por5)
        por.add(por6)
        por.add(por7)
        por.add(por8)
        por.add(por10)
        por.add(por9)
        bot.send_photo(chat_id=call.message.chat.id, photo=open('img/faq.jpg', 'rb'), reply_markup=por)

    elif call.data == 'zap':
        ds = telebot.types.InlineKeyboardMarkup()
        key1 = types.InlineKeyboardButton(text='Назад', callback_data='key2')
        ds.add(key1)
        bot.send_photo(chat_id=call.message.chat.id, photo=open('img/zap.jpg', 'rb'))
        bot.send_message(chat_id=call.message.chat.id, text="Zezwolenie na pracę typu A  -  це дозвіл на роботу в "
                                                            "Польщу, працівники часто називають 'воєвода', "
                                                            "'річне запрошення', 'воєводське запрошення'.\nТакий "
                                                            "дозвіл дає право будь-якому іноземцю на роботу на "
                                                            "території Республіки Польща. Даний вид дозволу дозволяє "
                                                            "відкрити візу після піврічного перебування в Польщі, "
                                                            "тобто після  оświadczeniа. У документі вказується "
                                                            "конкретний роботодавець, співробітник, посада. Тобто, "
                                                            "якщо змінилися які-небудь дані роботодавця чи іноземця, "
                                                            "то потрібно робити нове Zezwolenie na pracę typu A. "
                                                            "Оформлення Zezwolenie na pracę typu А -  платне ("
                                                            "100zł).\nДля отримання дозволу роботодавець повинен "
                                                            "надати дослідження ринку праці (badania rynku pracy), "
                                                            "що підтверджує неможливість задовольнити потреби "
                                                            "підприємства за допомогою громадян Польщі\nТермін "
                                                            "очікування зазвичай становить від 2 до 6 місяців.",
                         reply_markup=ds)


    elif call.data == 'term':
        ds = telebot.types.InlineKeyboardMarkup()
        key1 = types.InlineKeyboardButton(text='Назад', callback_data='form')
        ds.add(key1)
        bot.send_message(chat_id=call.message.chat.id, text="Декларацію PIT-37 потрібно подати до 30 квітня "
                                                            "наступного року. Наприклад, декларація PIT-37 за 2019 "
                                                            "року повинна бути подана до 30 квітня 2020 року. У той "
                                                            "же термін ви зобов’язані сплатити відповідний податок, "
                                                            "якщо в результаті кінцевого підрахунку виявилося, "
                                                            "що сума відрахувань з ваших доходів була менше податку, "
                                                            "який ви повинні заплатити від загальної суми доходів.і "
                                                            "побачите – чи повинні ви щось доплатити або ви вже "
                                                            "заплатили більше ніж потрібно, і можете отримати назад "
                                                            "цю різницю. Податкова інспекція перевірить, всі дані, "
                                                            "і якщо не знайде помилок, то поверне вам гроші. Або "
                                                            "буде очікувати, що ви заплатите недостачу.",
                         reply_markup=ds)

    elif call.data == 'time':
        ds = telebot.types.InlineKeyboardMarkup()
        key1 = types.InlineKeyboardButton(text='Назад', callback_data='podatok')
        ds.add(key1)
        bot.send_message(chat_id=call.message.chat.id, text="Часто українці, влаштовуючись на роботу за кордоном, "
                                                            "сподіваються, що податкова не дізнається про їх "
                                                            "іноземних доходи. Однак це далеко не так.\n По-перше, "
                                                            "фіскали можуть отримати інформацію про наявність "
                                                            "доходів від українських банків. Наприклад, "
                                                            "якщо іноземний роботодавець перераховує винагороду на "
                                                            "рахунок в український банк, або якщо офіційно "
                                                            "безробітний відкриє депозит на чималу суму. По-друге, "
                                                            "між Україною і багатьма країнами існує обмін податковою "
                                                            "інформацією.",
                         reply_markup=ds)

    elif call.data == 'podatok':
        ds = telebot.types.InlineKeyboardMarkup()
        key1 = types.InlineKeyboardButton(text='Назад', callback_data='form')
        key2 = types.InlineKeyboardButton(text='Що буде, якщо не платити податки вчасно?', callback_data='time')
        key3 = types.InlineKeyboardButton(text='Подати', url='https://www.e-pity.pl/')

        ds.add(key2)
        ds.row(key3, key1)
        bot.send_message(chat_id=call.message.chat.id, text="Декларацію можна подати або в паперовому вигляді в "
                                                            "одному з офісів податкової інспекції. Також можна "
                                                            "подати декларацію в електронному вигляді через "
                                                            "інтернет.\n Подання податкової декларації через "
                                                            "інтернет є найшвидшим і зручним способом. Не будемо "
                                                            "витрачати час на походи в податкову інспекцію і "
                                                            "простоювання в довгих чергах. Ще одним плюсом такого "
                                                            "способу є те, що програма сама автоматично проводить "
                                                            "всі необхідні розрахунки, зводячи до мінімуму "
                                                            "ймовірність будь-якої помилки.",
                         reply_markup=ds)

    elif call.data == 'form':
        ds = telebot.types.InlineKeyboardMarkup()
        key1 = types.InlineKeyboardButton(text='Назад', callback_data='key2')
        key2 = types.InlineKeyboardButton(text="Терміни", callback_data='term')
        key3 = types.InlineKeyboardButton(text="подача податкової в Польші", callback_data="podatok")
        ds.add(key3)
        ds.add(key2)
        ds.add(key1)
        bot.send_message(chat_id=call.message.chat.id, text="Форми IFT-1 і IFT-1R видаються в такому випадку, якщо "
                                                            "іноземець не являється податковим резидентом Польщі. "
                                                            "Тобто, ви будете платити податок в іншій країні.  Якщо "
                                                            "ви платите податки в Польщі, Вам видадуть  PIT-11.\n "
                                                            "Працівник зобов'язаний надати податковій інспекції "
                                                            "інформацію про розмір доходу такого працівника "
                                                            "IFT-1/IFT-1R (в електронному вигляді — до кінця лютого "
                                                            "наступного року, в паперовому — до кінця січня). Копія "
                                                            "залишається працівнику. \n Нерезидентом вважається та "
                                                            "людина, яка пропрацювала менше ніж 183 дні за останній "
                                                            "рік. B тако випадку працівнику видається форма IFT-1 / "
                                                            "IFT-1R і працівник не зобов'язаний подавати PIT-37 в "
                                                            "податкову. \n Податкові органи України схильні вважати "
                                                            "всіх власників українського паспорта податковими "
                                                            "резидентами України. Тому вимагають сплати податків, "
                                                            "якщо виявляють факти отримання доходів за кордоном. Щоб "
                                                            "цього уникнути, обов'язково довести статус нерезидента. "
                                                            "Якщо людина може довести, що вона являється "
                                                            "нерезидентом, то вона звільняється і від  декларації, "
                                                            "і від оплати в Україні податку на закордонні доходи.\n "
                                                            "Якщо особу буде визнано податковим резидентом України, "
                                                            "вона зобов'язана сплатити в Україні податок на доходи "
                                                            "фізичних осіб (ПДФО) від усіх отриманих доходів 18% та "
                                                            "військовий збір 1,5% від доходу, у тому числі й "
                                                            "отриманого за кордоном. Варто знати, що єдиний "
                                                            "соціальний внесок (ЄСB-22%) з зарубіжних доходів не "
                                                            "знімається.\n B більшості випадків Українці які "
                                                            "працюють за кордоном сподіваються, що податкова служба "
                                                            "України не дізнається про ці доходи. Але між Україною "
                                                            "та багатьма країнами існує вибірковий обмін податковою "
                                                            "інформацією за окремими запитами. Оскільки Україна "
                                                            "приєдналася до так званого плану BEPS, то можливе "
                                                            "введення стандартного CRS (автоматичний обмін "
                                                            "податковою інформацією) між країнами", reply_markup=ds)

    elif call.data == 'pit11':
        ds = telebot.types.InlineKeyboardMarkup()
        key1 = types.InlineKeyboardButton(text='Назад', callback_data='key2')
        ds.add(key1)
        bot.send_message(chat_id=call.message.chat.id, text="PIT-11 це документ з таблицею яка містить дані про ваші "
                                                            "доходи за рік і сплачені податки. Якщо ви працюєте в "
                                                            "Польщі, то ваш роботодавець відраховує з вашої "
                                                            "заробітної плати податок на доходи фізичних осіб.\nДо "
                                                            "кінця лютого роботодавець зобов’язаний направити вам "
                                                            "форму PIT-11, тобто документ, в якому міститься "
                                                            "інформація про ваші доходи, які ви отримали, працюючи на "
                                                            "нього, в попередньому податковому році, і інформація про "
                                                            "сплачені відрахування з заробітної плати з податку на "
                                                            "доходи. Якщо ви працювали в декількох місцях (у різних "
                                                            "роботодавців), отримаєте PIT-11 від кожного "
                                                            "роботодавця.\nPIT-11 видається, якщо іноземець є "
                                                            "податковим резидентом Польщі. У ньому вказується місце "
                                                            "проживання платника податків на території Польщі. PIT-11 "
                                                            "буде переданий як працівникові, так і в податкову "
                                                            "інспекцію за місцем проживання працівника в Польщі. "
                                                            "Працівник після отримання PIT-11 повинен подати до "
                                                            "податкової декларації PIT-37", reply_markup=ds)
    elif call.data == 'pit37':
        ds = telebot.types.InlineKeyboardMarkup()
        key1 = types.InlineKeyboardButton(text='Назад', callback_data='key2')
        ds.add(key1)
        bot.send_message(chat_id=call.message.chat.id, text="PIT-37 – податкова декларація за рік, яку ви повинні "
                                                            "подати за минулий рік роботи в Польщі. Якщо ви не "
                                                            "здійснюєте господарської діяльності, то на підставі "
                                                            "PIT-11, вам слід заповнити PIT-37  і подати його до "
                                                            "відповідного управління податкової адміністрації. \n "
                                                            "PIT-37 - податкова декларація за рік, яку Ви повинні "
                                                            "подати за останній рік роботи в Польщі. \n Якщо ви не "
                                                            "здійснюєте господарської діяльності, то на базі PIT-11, "
                                                            "вам слід заповнити PIT-37 (декларація про рівень "
                                                            "отриманих доходів / понесених витрат за даний "
                                                            "податковий рік) і подати його у відповідному управлінні "
                                                            "податкової адміністрації.\n Декларація PIT - 37 "
                                                            "обов'язково подається до 30 квітня наступного (після "
                                                            "декларованого податково) року (наприклад, Декларація "
                                                            "PIT-37 до 2020 року повинна бути подана до 30 квітня "
                                                            "2021 року). B той же термін Ви зобов'язані оплатити "
                                                            "відповідний податок, якщо в якості кінцевого рахунку "
                                                            "виявилося, що сума відрахувань ваших доходів була менше "
                                                            "податку, що ви повинні заплатити від загальної суми "
                                                            "доходів. \n Податкові відрахування в Польщі PIT, "
                                                            "як подати декларацію Pit 37 ? \n Податок на доходи "
                                                            "фізичних осіб- це податок, який платить кожна людина, "
                                                            "яка отримує дохід. B Більше цей рахунок називається PIT "
                                                            "і оплачується всіма працюючими людьми...",
                         reply_markup=ds)

    elif call.data == 'key3':

        keyboar = telebot.types.InlineKeyboardMarkup()
        keyboar.add(telebot.types.InlineKeyboardButton(text="назад", callback_data="mainmenu"))
        bot.send_photo(call.message.chat.id, photo=open('img/photo_2021-02-14_20-00-48.jpg', 'rb'))
        bot.send_message(chat_id=call.message.chat.id,
                         text='Для їх отримання потрібно повідомити за місяць часу до закінчення терміну дії Ваших '
                              'документів\n1.Załącznik nr 1 \n 2. Засвідчення Вашого фактичного місця проживання ('
                              'якщо Ви '
                              'проживаєте на нашому житлі) \n 3. Медичне страхування ZUS \n 4. Інформація '
                              'старости '
                              'або документ який засвідчує звільнення від даного документу. \n 5. Оригінал umowy '
                              'zlecenia ( договір між працівником і роботодавцем )',
                         reply_markup=keyboar)

    elif call.data == 'key4':
        op = telebot.types.InlineKeyboardMarkup()
        key1 = types.InlineKeyboardButton(text='Рекомендації щодо вибору банку', callback_data='recomend')
        key2 = types.InlineKeyboardButton(text='Назад', callback_data='mainmenu')
        op.add(key1)
        op.add(key2)
        bot.send_message(call.message.chat.id, text="Відкрити рахунок у банку Польщі дуже просто. Для цього навіть не "
                                                    "обов'язково мати посвідку на проживання, достатньо просто "
                                                    "візи/біометрії і umowy zlecenia , яка дозволяє вам перебувати "
                                                    "в "
                                                    "Польщі.\n B більшості великих банківських відділень персонал "
                                                    "говорить англійською, так що якщо ви не знаєте польської мови, "
                                                    "це не повинно викликати проблем. \n Але не поспішати "
                                                    "реєструватися "
                                                    "онлайн, найшвидшим і найефективнішим способом буде звернутися "
                                                    "негайно в обраний вами банк, де на місці можна здати всі "
                                                    "документи і заповнити необхідні заяви. \nUmowa zlecenia - це "
                                                    "договір ( між Агенцією і працівником) який Ми підписуємо в "
                                                    "перший день праці. Одне з важливих запитань яке задають "
                                                    "працівники банку- це чи Ви є  резидентом-платником податків в "
                                                    "Польщі чи в Україні ? На це питання слід відповідати, "
                                                    "що Ви платите податки в Польщі, адже від цього залежатиме чи "
                                                    "отримаєте Ви  PIT 11 чи IFT-1 ( про це детальніше в блоці про "
                                                    "розрахунок податків)", reply_markup=op)

    elif call.data == 'recomend':
        ds = telebot.types.InlineKeyboardMarkup()
        key1 = types.InlineKeyboardButton(text='Назад', callback_data='key4')
        ds.add(key1)
        bot.send_message(call.message.chat.id,
                         text="Багато польських банків з метою залучення нових клієнтів надають можливість "
                              "обслуговування російською та українською мовами.\n Міленіум - українська та російська "
                              "'гаряча лінія';\nPekao - є українська 'гаряча лінія', документація українською та "
                              "Мобільний додаток тією ж мовою;\nGetin Bank - у деяких містах і відділеннях є "
                              "російськомовні консультанти, сайт українською мовою і телефонні лінії також "
                              "обслуговуються українською мовою;\nSantander - гаряча лінія на багатьох мовах;\nING "
                              "Bank - російськомовні телефонні консультації;\nRaiffeisenBank - пропонує своїм "
                              "клієнтам українську версію сайту;\nCredit Agricole - брошури, документація, "
                              "інформація про відкриття та стан рахунку, мобільний додаток - все це доступно "
                              "українською мовою", reply_markup=ds)

    elif call.data == 'key5':

        op = telebot.types.InlineKeyboardMarkup()
        key17 = types.InlineKeyboardButton(text='Банківський рахунок Уженду у Познані', callback_data='poznan')
        key18 = types.InlineKeyboardButton(text='Банківський рахунок Уженду у Варшаві', callback_data='warsaw')
        key19 = types.InlineKeyboardButton(text='Банківський рахунок Уженду у Вроцлаві', callback_data='wroclaw')
        key20 = types.InlineKeyboardButton(text='Банківський рахунок Уженду у Кракові', callback_data='krakow')
        key21 = types.InlineKeyboardButton(text='Назад', callback_data='mainmenu')
        op.add(key17)
        op.add(key18)
        op.add(key19)
        op.add(key20)
        op.add(key21)
        bot.send_photo(chat_id=call.message.chat.id, photo=open('img/bank.jpg', 'rb'), reply_markup=op)

    elif call.data == 'doc':
        do = telebot.types.InlineKeyboardMarkup()
        do1 = types.InlineKeyboardButton(text='Назад', callback_data='key6')
        do.add(do1)
        bot.send_photo(chat_id=call.message.chat.id, photo=open('img/doc.jpg', 'rb'))
        bot.send_message(chat_id=call.message.chat.id, text='1.Заповнений Внесок і копія Внеску \nІнформації '
                                                            'стосовно правильного заповнення внеску можете знайти за '
                                                            'допомогою сервісу https://www.youtube.com вписавши в '
                                                            'пошуку “Як заповнювати внесок на карту побиту?”) '
                                                            'Заповнюйте внесок акуратно і достовірно, '
                                                            'не допускаються жодні виправлення чи закреслення. '
                                                            'Старайтесь не пропускати анкетних запитань, від того як '
                                                            'ви заповните внесок залежить результат розгляду вашої '
                                                            'справи.\n2.4 фотографії ( 3, '
                                                            '5cm x 4,5cm зроблені не пізніше 6 місяців до дня подачі '
                                                            'документів)\n3.Копія паспорта (всі сторінки, де є '
                                                            'відмітки; першу сторінку 2 рази). Якщо є два паспорти '
                                                            'то копія обох  паспортів (усі сторінки, де є відмітки, '
                                                            'першу сторінку 2 рази).\n4.Підтвердження оплати 440 '
                                                            'злотих( оригінал і копію оплати вислати з документами, '
                                                            'окремо зробити копію для себе). '
                                                            '\n5.Копія Załącznik Nr 1.\n6.Копія Umowy '
                                                            'zlecenia.\n7.Копія Umowy najmu mieszkania / '
                                                            'Oświadczenie o zapełnieniu zakwaterowania.\n8.   Копія '
                                                            'ZUS ZUA.', reply_markup=do)

    elif call.data == 'dox':
        do = telebot.types.InlineKeyboardMarkup()
        do1 = types.InlineKeyboardButton(text='Назад', callback_data='key6')
        do.add(do1)
        bot.send_document(chat_id=call.message.chat.id, data=open('doc/pobyt_czasowy_2019.docx', 'rb'))
        bot.send_document(chat_id=call.message.chat.id, data=open('doc/pobyt_czaswy_zal_1_2018.docx', 'rb'))
        bot.send_message(call.message.chat.id, text='Документи для заповнення', reply_markup=do)

    elif call.data == 'key6':

        keyb = telebot.types.InlineKeyboardMarkup()
        key12 = types.InlineKeyboardButton(text='Перелік документів потрібний для оформлення', callback_data='doc')
        key13 = types.InlineKeyboardButton(text='Банківськи рахунки', callback_data='bank')
        key14 = types.InlineKeyboardButton(text='Перелік документів які надаються', callback_data='key3')
        key15 = types.InlineKeyboardButton(text='Скачати документи для заповнення', callback_data='dox')
        key16 = types.InlineKeyboardButton(text='Назад', callback_data='mainmenu')

        keyb.add(key12)
        keyb.add(key13)
        keyb.add(key14)
        keyb.add(key15)
        keyb.add(key16)
        bot.send_photo(chat_id=call.message.chat.id, photo=open('img/query.jpg', 'rb'), reply_markup=keyb)
    elif call.data == 'key7':
        keybo = telebot.types.InlineKeyboardMarkup()
        key11 = types.InlineKeyboardButton(text='Назад', callback_data='mainmenu')

        keybo.add(key11)
        bot.send_photo(chat_id=call.message.chat.id, photo=open('img/card.jpg', 'rb'))
        bot.send_message(chat_id=call.message.chat.id,
                         text="Багаторазовий перетин кордону без необхідності оформлення і продовження "
                              "візи;\nПокупка і оформлення нерухомості та автотранспорту;\nВільне переміщення у "
                              "Шенген Зоні (ви можете проживати в будь-якій країні Шенгену протягом 3 місяців у "
                              "півріччі);\nМожливість безкоштовного навчання у вищих навчальних закладах Польщі ("
                              "за виключенням карти czasowego pobytu);\nВідкриття фірми і ведення "
                              "бізнесу;\nМожливість отримати кредит;можливість оформлення довгострокової "
                              "національної візи для членів своєї сім'ї (за виключенням карти czasowego "
                              "pobytu);\nПодача документів для оформлення візи в консульства США і Великобританії "
                              "\n(Дуже актуальна інформація для жителів України, де відсоток відмов у наданні віз "
                              "у США досягає 40% від загального числа заявників. У Польщі ця цифра не більше "
                              "5%);",
                         reply_markup=keybo)
    elif call.data == 'key8':
        keyboa = telebot.types.InlineKeyboardMarkup()
        key9 = types.InlineKeyboardButton(text='Назад', callback_data='mainmenu')
        key10 = types.InlineKeyboardButton(text='Наш сайт', url='https://redwork.com.ua/')
        keyboa.add(key9, key10)
        bot.send_photo(chat_id=call.message.chat.id, photo=open('img/about.jpg', 'rb'))
        bot.send_message(chat_id=call.message.chat.id,
                         text='Red Work Sp. z o. o – це польська фірма по працевлаштуванню, заснована в Кракові '
                              'в 2016 році молодими українцями.\nНашим основним завданням є пошук таких '
                              'роботодавців ,які можуть забезпечити гідну та безпечну роботу для працівників.\nМи '
                              'об’єднуємо найкращих працівників та достойних роботодавців,як в Польщі так і в '
                              'інших Європейських країнах.\nЗ нами ви будете точно впевнені ,що працюєте '
                              'офіційно, '
                              'з можливість кар’єрного росту та індивідуальним підходом до ваших '
                              'кваліфікацій.\nУсі наші послуги безкоштовні та сертифіковані польським урядом.\nЗ '
                              'нами ви знайдете роботу, як без кваліфікації та вимог, так і спеціалізовані '
                              'професії на всій території Польщі й у всіх сферах.Ми пропонуємо довготривалі та '
                              'сезонні контракти для сімейних пар,чоловіків та жінок.\nДякуємо,Вам,за вашу працю!',
                         reply_markup=keyboa)


bot.polling(none_stop=True, interval=0)
