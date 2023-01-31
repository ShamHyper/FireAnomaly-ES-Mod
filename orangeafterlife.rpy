init:
    $ mods["orangeafterlife"]=u"{color=#FF4500}{b}{i}Огненная Аномалия"    
    $ save_name = ("Огненная Аномалия")
    $ config.developer = True

label orangeafterlife:

    show daundev_logo with dissolve2
    pause 3
    hide daundev_logo

    $ prolog_time()
    $ persistent.sprite_time = "night"
    play ambience ambience_forest_night

    th "Почему так тихо?"
    th "Что за..{w} где я вообще?"
    me "АЙ!" with hpunch
    "Я заорал от резкой боли в голове, ощущалась она так, как будто мне на голову упал кирпич"

    window hide
    pause 0.5
    show bg ext_bus_night 
    show prologue_dream
    with dissolve
    $ night_time()

    me "Что за шутка!{w} Где я?!"

    hide ext_bus_night

    th "Что я тут делаю?{w} Какого чёрта так жарко?"
    th "Так много вопросов, ещё и боль адская.."

    window hide
    stop ambience fadeout 3
    pause 0.5

    show bg ext_bus_night with dissolve
    show sl normal pioneer at cleft with dissolve 
    play music music_list["everlasting_summer"] fadein 1

    sl "Привет!"
    sl "Это ты новенький?{w} Что-то у тебя автобус задержался.."

    window hide
    show bg ext_bus_night with dissolve2
    show sl surprise pioneer at cleft with dspr
    show blink
    pause 1
    hide blink
    show unblink

    "Не может быть..{w} снова.."

    window hide    
    show bg ext_bus_night with dissolve2
    show sl surprise pioneer at cleft with dissolve
    show blink
    pause 1
    hide blink
    show unblink

    "Я {b}всё{/b} вспомнил.."
    
    window hide
    show bg ext_bus_night with dissolve2
    show sl surprise pioneer at cleft with dissolve
    show blink
    pause 1
    hide blink
    show unblink   

    "{b}Алиса..!"

    hide ext_bus_night
    hide sl surprise pioneer at cleft
    window hide   
    $ day_time()
    pause 0.5
    
    th "Это был сон?"
    th "Или реальность.."

    window hide
    show blink
    pause 1
    hide blink
    show unblink  

    "Я уже не понимаю..{w} как же болит голова.."
    th "Нужно просыпаться.."

    show blink
    pause 1
    hide blink
    show unblink 
    hide prologue_dream
    show bg ext_road_sunset with dissolve  
    pause 0.5


    "Пару лет назад я попал в аномалию"
    "Так вышло, что я до сих пор не понимаю что происходит, если быть честным"
    "Своё состояние сейчас я могу описать, как будто нахождение в какой-то {i}червоточине{/i}"
    "После попадания в неё, каждый раз как будто напиваюсь.{w} Самый настоящий “День Сурка”!"
    "На счёт этой аномалии.."

    $ prolog_time()
    $ persistent.sprite_time = "day"
    window hide
    hide ext_road_sunset
    show bg intro_xx with dissolve 
    pause 0.5

    "Началась она два года назад, в Январе"

    window hide
    hide intro_xx 
    show bg bus_stop with dissolve 
    pause 0.5

    "Я как обычно садился в автобус до колледжа, на 410-й маршрут"
    "Но всю ночь до этого я провёл с другом и бутылкой рома"
    "И по этой причине я и уснул во время рейса"

    window hide
    show blink
    pause 3
    stop music fadeout 6
    $ backdrop = "dv"
    $ new_chapter(1, u"День 1")
    hide bus_stop
    hide blink
    show unblink
    show bg int_bus
    play ambience ambience_old_camp_outside fadein 5
    $ day_time()

    "А когда открыл глаза..{w} увидел автобус"
    "Но он был уже совсем другим..{w} новым чтоли?"
    "Без жвачек на каждом сиденье, без грязи на полу.."
    "Ещё и голова раскалывалась"

    window hide
    hide int_bus
    show bg ext_bus with dissolve2
    pause 0.5

    "Я всё таки решился и вышел из автобуса на свежий воздух"
    "И с этого момента я поподал в эту злосчастную петлю, у которой всегда был один исход"
    "Алиса погибала из-за меня..{w} или из-за каких-то других обстоятельств"
    "Но в этот раз я должен её спасти, чего бы мне это не стоило."

    window hide
    stop ambience fadeout 3
    hide ext_bus with dissolve
    show bg ext_camp_entrance_day with flash
    show sl normal pioneer at center with dissolve
    play ambience ambience_ext_road_day fadein 5
    play music music_list["i_want_to_play"] fadein 5
    pause 0.5

    sl "Ау-у!"
    sl "Ты меня вообще слушаешь!?"

    show sl angry pioneer at center with dspr
    pause 0.5

    "Это был первый раз, когда я увидел Славю злой"
    "Может быть я не один в этой петле?"
    "Такое ощущение что ей это тоже надоело.."
    "А может у меня начинает крыша ехать.."
    me "Да, извини!"
    me "Меня Семён зовут, а тебя как?"

    show sl smile pioneer at center with dspr

    sl "Меня Славя! Приятно познакомится.{w} Давай покажу что тут и где?"
    "Знала бы ты сколько раз я слышал эту фразу"
    "Каждый раз, когда я возвращался из этого лагеря"
    "История повторялась."
    "Честно говоря, Славя для меня стала как швейцаром что-ли"
    "Но особого интереса она для меня не представляла"
    me "Да я бывал тут уже пару раз, спасибо, сам разберусь"
    "Пару десятков..{w} или уже сотен раз?"
    "Вообщем слушать её мне не хотелось"

    stop ambience fadeout 2
    stop music fadeout 2
    pause 0.5
    window hide 
    hide sl with dissolve
    hide ext_camp_entrance_day with dissolve
    play music music_list["get_to_know_me_better"] fadein 3
    pause 0.5
    play ambience ambience_day_countryside_ambience fadein 3
    pause 0.5
    show bg ext_house_of_dv_day with dissolve2

    "Решил я сразу пойти к домику Алисы, вдруг встретимся внезапно"

    window hide 
    hide sl 
    hide ext_house_of_dv_day with dissolve
    show bg ext_houses_day with dissolve2
    pause 0.5
    show dv angry pioneer2 at cleft with flash_red

    dv "Что встал посреди дороги!{w} Уйди пока зубы не повыбивала!"
    "Я очень старался сдерживать смех, но после всего что между нами было.."
    th "И я засмеялся"
    
    show dv guilty pioneer2 at cleft with dspr

    dv "Ну и что смешного.."
    "Я не знал что ответить"
    "Мне казалось что я знаю её лучше чем себя"
    "И все её агрессивные уловки были для меня не больше чем детская игра"
    me "Да ничего.."
    
    show dv normal pioneer2 at left with dissolve
    show us smile pioneer at right with dissolve 

    us "О, приветик, а ты кто?"
    me "Семён, а ты кто будешь?"
    "Ульяна уже перестала меня бесить давно, но видимо не до конца, такой уж у неё характер"
    "Наглая и ведёт себя как маленькая"
    
    show dv angry pioneer2 at left with dspr
    show us dontlike pioneer at right with dspr

    "Алиса вмешалась в наш диалог"
    dv "Ульяна, иди отсюда! Не видишь, взрослые общаются!"
    "Ну тут нельзя не поддержать тебя, моя хорошая"
    "Пока смотрел как они ругаются, задумался"
    "Есть ли способ как вернуть память Алисе?"
    "Не только же я всё должен помнить!"
    us "Ну и пожалуйста!"

    hide us with dissolve
    show dv normal pioneer2 at cleft with dissolve

    "Резкая тишина ввела меня в заблуждение"
    "Сам не заметил, как уставился на убегающую Ульянку.."
    "..и как близко ко мне подошла Алиса"

    show dv normal pioneer2 close at center with dissolve

    dv "Ты что, влюбился в неё?"
    th "Нет."
    me "Может быть, а ты что ревнуешь?"

    show dv smile pioneer2 far at center with dissolve

    dv "Почему у меня такое ощущение, что я знаю тебя?"
    "Потому что так оно и есть"
    me "Может быть мы были знакомы в другом мире?"
    th "Да Сёма, шутник из тебя, как из.."
    th "..даже тут шутку не смог придумать"

    show dv laugh pioneer2 at cleft with dissolve

    dv "Ха-Ха"
    dv "Вот ты идиот конечно!"

    hide dv laugh pioneer2 with dissolve

    th "Немного обидно, что так и не вышло пообщаться с ней"

    play sound dindin

    th "Надеюсь за обедом что нибудь придумаю"

    hide ext_houses_day with dissolve
    show bg int_dining_hall_people_day with dissolve
    stop ambience fadeout 5
    stop music fadeout 5
    pause 1
    play ambience ambience_dining_hall_full fadein 5

    "Да.. сколько же раз я ел эти долбанные рыбные котлеты.."
    "Это наверное худшее что я ел в своей жизни"
    "Такое ощущение что их делают не из рыбы, а из того чем рыба испражняется"
    "Ладно, стоит думать о другом"
    "Об Алисе.."
    "Они как раз сидели вместе с Леной в дальнем углу столовой"
    "Я решил сесть к ним"
    
    window hide
    stop ambience fadeout 3
    pause 1
    play sound scary3
    show pi far at center with dspr
    pause 0.05
    hide pi at center with dissolve
    play music doo33 fadein 2

    "Что..?"
    th "Я чуть не умер со страху.."
    "Это же я!"
    "Он так странно и быстро прошёл мимо меня, что я даже не успел рот открыть"
    "КАКОГО ЧЁРТА ЗДЕСЬ ПРОИСХОДИТ!" with vpunch
    "Это точно не к добру.{w} Я чувствую это"
    "Или у меня паранойя.."
    "Но лучше стоит проследить за ним"

    stop music fadeout 3
    pause 0.25

    "Чёрт!"
    "Он как сквозь землю провалился"
    "Ладно, подойду к девочкам.."

    play ambience ambience_dining_hall_full fadein 3
    play music music_list["silhouette_in_sunset"] fadein 3

    th "Странно это всё"

    show dv normal pioneer at cleft with dissolve
    show un normal pioneer at cright with dissolve

    dv "О, чудной, здарова!"
    me "Привет, Алиса"
    "Чёрт.. я же не спрашивал как её зовут"
    "Каждый раз эту ошибку допускаю"
    "Правильно она сказала - идиот"
    dv "Чё шуганный такой? Меня боишься?"
    me "Да щас! Девчонку мне ещё бояться!"
    "Я чувствую себя героем реиграбельного симулятора свиданий, и каждый раз стараюсь говорить одно и то же"
    "Но иногда, по каким-то причинам"
    "Ответы от других людей меняются"
    
    show dv angry pioneer at cleft with dspr 

    dv "Ну ничего.{w} Мы это быстро исправим!"
    "Не думаю"

    hide dv angry pioneer at cleft with dissolve 
    show un normal pioneer at center with dissolve

    "Я остался наедине с Леной"
    "Не знаю о чём с ней заговорить"
    "Она всегда казалась мне странной"
    me "Ты тоже новенькая? Меня Семён зовут, а тебя?"
    
    show un shy pioneer at center with dspr 

    un "Я.."
    un "Меня Лена зовут.."
    "Еле слышно ответила она.."

    hide un shy pioneer at center with dissolve

    "..и сразу ушла"

    window hide
    show edasuka with dissolve 
    pause 0.5

    th "Ну выбора у меня нет, придётся есть что дают"
    th "Хотя..{w} это лучше чем пельмени за 30 рублей из магазина у дома"

    stop ambience fadeout 5
    window hide
    hide edasuka with dissolve 
    hide int_dining_hall_people_day with dissolve

    "Я вышел на улицу"
    
    window hide
    show bg ext_dining_hall_near_sunset with dissolve
    play ambience ambience_camp_center_day fadein 2
    $ sunset_time()

    "Хорошо что я больной на голову, и ходил зимой в одной кофте и джинсах"
    "Иначе бы меня уже можно было выжимать от пота"
    "Но всё равно, стоило бы переодеться"
    "Интересно, в этот раз будет тоже самое?"
    "Ульяна заболеет и уедет домой.. а меня поселят к Алисе"
    "Буду надеятся"
    "Я конечно не желаю зла Ульяне, но она действительно третий лишний"
    "И так будет безопасней для Алисы..{w} учитывая, что тут ходит моё Альтер-Эго"

    show dv normal pioneer2 far at cleft with dissolve

    dv "Ну что?"
    "Я так погряз в своих мыслях, что не заметил как Алиса подошла ко мне"
    me "Что?"

    show dv angry pioneer2 at cleft with dissolve

    dv "Ты придурок, скажи честно?"
    "Я уже забыл, что она там говорила в столовой"
    me "Местами да"
    
    show dv normal at cleft with dspr 

    dv "Ладно, напомню"
    dv "Я сказала, что заставлю тебя меня бояться!"
    me "А, точняк"
    me "И как же ты это будешь делать?"
    

    show dv smile at cleft with dspr

    dv "Посмотрим, чудик"
    "Она мило улыбнулась и куда-то ушла"

    hide dv smile at cleft with dissolve
    stop music fadeout 3
    stop ambience fadeout 3

    "Пойду-ка я заселяться, а то уже темнеть начинает"
    "Жаль на ужин не успею, но чёрт с ним"
    "Алиса важнее чем булки с кефиром"

    hide ext_dining_hall_near_sunset with dissolve
    $ night_time()
    show bg ext_house_of_mt_sunset with dissolve
    play ambience ambience_forest_evening fadein 5
    play music music_list["i_dont_blame_you"] fadein 5

    "Дом Вожатой.."
    voice "~Беги~"
    "Что?"
    th "Кажется мне послышалось"
    "Ладно, пожалуй постучусь, и спрошу куда мне поселиться"

    play sound tuktuk 
    pause 0.5
    hide ext_house_of_mt_sunset with dissolve
    show bg int_house_of_mt_sunset with dissolve 
    play sound opendoor
    pause 0.5
    show mt normal pioneer far at center with dissolve

    me "Здравствуйте, я Семён, новенький"

    show mt smile pioneer far at center with dspr

    mt "Привет, пионер!{w} Я - Ольга Дмитриевна, вожатая твоего отряда.{w} Давно ты приехал?"
    me "Днём.{w} На обеде уже был.{w} Где я могу получить форму и поселиться?"

    show mt normal pioneer at center with dissolve 

    mt "Форму я тебе выдам.{w} А жить ты будешь.."
    th "Бог, если ты есть, ты знаешь что делать!"
    mt "..с Алисой!{w} Её соседка заболела и уехала.{w} Ты уже знаком с ней?"
    th "Ещё как"
    me "Да, пару раз виделись.{w} Куда мне идти?"
    "Я знал куда мне идти, спросил просто, чтобы не было лишних вопросов"
    mt "Живёт она в 23 доме, окола поворота на лодочную станцию"
    mt "Сам сможешь дойти?"
    me "Да, спасибо!"

    play sound opendoor
    window hide
    hide int_house_of_mt_sunset with dissolve 
    hide mt normal pioneer at center with dissolve
    show bg ext_house_of_dv_night with dissolve
    stop ambience fadeout 2
    stop music fadeout 3

    "К этому месту уже подойдёт фраза.."
    "..дом, милый дом!"

    hide ext_house_of_dv_day with dissolve
    play sound tuktuk
    pause 0.5
    play sound opendoor
    show bg int_house_of_dv_night with dissolve

    "Я вошёл"
    "Алиса сидела на кровати.."
    "..в нижнем белье"

    play music music_list["that_s_our_madhouse"] fadein 5
    play ambience ambience_camp_entrance_night
    show dv surprise swim far at center with flash
    pause 1
    show dv shocked swim at center with dissolve

    dv "Ты..{w} ты.."
    "А вот этого раньше не было!"
    "Похоже я пришёл слишком рано!"
    "МНЕ КОНЕЦ!" with vpunch
    
    show blink
    pause 1
    hide dv shocked swim at center

    
    me "Я ЗАКРЫЛ ГЛАЗА!{w} ИЗВИНИ, АЛИСА!{w} Я НЕ ХОТЕЛ!"

    hide blink
    show unblink

    "Когда я открыл глаза она уже была одета"

    show dv angry pioneer2 close at center with dissolve

    dv "ТЕБЯ СТУЧАТЬСЯ НЕ УЧИЛИ!?"
    me "Я стучался!"
    me "Успокойся! Я сразу закрыл глаза!"

    show dv laugh pioneer2 close at center with dspr

    dv "Хотя ладно, будет как раз за что тебе отомстить!"
    me "Извини.."
    dv "Да ладно тебе, с кем не бывает"
    "Я уже очень хотел спать"

    show dv smile pioneer2 far at cleft with dissolve
    stop music fadeout 10

    dv "Я ложусь спать, твоя кровать справа. {w} Я знала, что тебя поселят ко мне, чудик, я видела планировку расселения на столе вожатой!"
    "Неудивительно что она уже всё проверила у Ольги дома. {w}Странно но вещи Ульяны всё ещё здесь..{w} ну ладно, переложу куда-нибудь"
    me "Спокойной ночи.."
    me "{i}..любимая"
    "Сказал я шёпотом"
    dv "Ага"
    
    play music music_list["reflection_on_water"] fadein 2
    hide dv smile pioneer2 far at cleft with dissolve
    show blink
    hide int_house_of_dv_day
    
    "Я долго не мог уснуть"
    "И слышал что Алиса тоже всё ещё ворочилась"
    "Я решил заговорить с ней. {w}Днём шанса не выдалось"
    me "Алиса?"
    "Спросил я шёпотом"
    dv "Да?"
    me "Я не отвлекаю тебя от сна?"
    dv "Нет, не спится всё равно что-то"
    me "Ты никогда не чувствовала что забыла что-то важное?"
    dv "Бывало. Я думаю у всех такое бывает"
    me "Ты первый раз в этом лагере?"
    dv "Да.. {w}но.."
    me "Что?"
    dv "Я чувствую себя здесь так.."
    "Она сделала минутную паузу, прежде чем продолжить свою речь"
    dv "Такое ощущение что я не первый раз здесь.{w} Всё кажется таким знакомым, как будто уже жила в этом лагере..{w} и была со всеми знакома.."
    "Я был рад услышать то, что не у одного меня крыша едет.{w} Вдруг Алиса тоже попадает сюда из другого места, просто не помнит этого?{w} В первые циклы {color=#FF4500}аномалии{/color} я тоже чувствовал, что место знакомое.."
    "А с каждым новым циклом появлялись чувства дежавю на каждом углу"
    "А потом память не стала упускать не единой секунды нахождения в лагере"
    "Я надеюсь"
    "Но иногда, при начале цикла, то есть во время выхода из автобуса, голова становилась более пустой"
    "Как будто часть мыслей утерялась где-то на нижних этажах моей памяти"
    "Может быть я забываю что-то очень важное, что помогло бы спасти Алису?.."
    me "Я тоже это чувствую"
    me "Алиса.."
    "Я услышал посапывание с соседней койки, и понял что уже я общался сам с собой"
    "В голове промелькнули воспоминания из прошлого цикла.."

    show alisa_bg 
    show prologue_dream
    with dissolve2
    pause 3
    hide blink
    show unblink

    "Как же хорошо было рядом с ней.."
    "И сейчас хорошо"
    "От одного ощущения что она рядом.. {w}становится тепло на душе"
    "Наступает умиротворение и покой"
    "И все проблемы забываются"
    th "Ладно.. {w}время спать"

    pause 1.5
    show blink
    pause 1.5
    stop ambience fadeout 2
    stop music fadeout 3
    hide alisa_bg
    hide prologue_dream
    $ day_time()
    $ backdrop = "dv"
    $ new_chapter(2, u"День 2")
    show bg int_house_of_dv_day 
    hide blink
    show unblink
    play ambience ambience_camp_entrance_day fadein 5
    pause 2
    
    "Новый день"
    "Приятное утро"
    "Наконец-то, за долгое время я почувствовал покой на душе"       
    "Я сел на край кровати"
    th "Алиса ещё спит.."
    "Завтрак через 40 минут"
    "Надо бы разбудить её"
    
    play sound krovat

    "Я сел на край её кровати"
    th "Я хотел бы любоваться её безмятежной красотой вечно.."
    "Я набрался смелости и решил нежно погладить её по волосам"
    
    play sound krovat

    "Чёрт, кровать заскрипела"
    "Алиса начала просыпаться, и кажется заметила мою руку у себя на голове"

    show dv shy pioneer2 close at center with dissolve
    stop music fadeout 2
    pause 3
    play music music_list["i_want_to_play"] fadein 2
    show dv surprise pioneer2 close at center with vpunch

    dv "Ты что делаешь, извращенец!?"
    me "Я..{w} я..{w} я просто хотел тебя разбудить!"
    me "Завтрак проспишь!"
    
    pause 0.5
    show dv shy pioneer2 close at center with dspr

    "Сидя у неё на кровати, я ненадолго провалился в свои мысли"
    "И не заметил её смущённое лицо"
    th "Какая же она милая.."
    
    show dv smile pioneer2 close at cleft with dissolve

    dv "Ладно, извращенец, пойдём на завтрак уже!"

    hide dv smile pioneer2 close at cleft with dissolve
    play sound opendoor

    "Когда я успел стать извращенцем?!"
    "Ах.. да, она же не помнит меня.."
    "Ладно, после завтрака всё обдумаю получше"
    "Вся информация важная к размышлению у меня есть"
    "Алиса всегда была в порядке в первый день в лагере"
    "Но после завтрака во второй день начаналось что-то странное"

    stop music fadeout 5

    "Ещё и этот Лже-Семён.."
    "Фух.."

    play sound opendoor

    "Надо идти"

    window hide
    hide int_house_of_dv_day with dissolve
    play music music_list["eat_some_trouble"] fadein 2
    play ambience ambience_camp_center_day fadein 5
    show bg ext_washstand2_day with dissolve

    "День я решил начать с умывания"
    "Да, вода здесь как и раньше ледяная"
    "Вот что-что, а вода здесь не меняется!"

    window hide
    hide ext_washstand2_day
    show bg ext_dining_hall_away_day with dissolve

    "А теперь отправлюсь завтракать"
    "И надеюсь на этот раз смогу поговорить с Алисой"

    stop music fadeout 3

    "..."

    play sound scary3
    show pi far at center with dspr
    hide pi far at center with dspr

    "Чёрт!"
    "Опять он!"
    "Надо скорее идти в столовую и проверить Алису!"

    hide ext_dining_hall_away_day with dissolve
    stop ambience fadeout 3
    play ambience ambience_dining_hall_full fadein 2
    play music music_list["silhouette_in_sunset"] fadein 3
    play sound opendoor 

    "Надеюсь с ней всё хорошо"

    show bg int_dining_hall_people_day with dissolve

    "Самое страшное, что я не знаю от чего её спасать"
    "Каждый раз воспоминания об этом у меня пропадают"
    "Помню только картину перед глазами..{w} лучше бы её тоже забыл"
    me "Алиса.."
    dv "Да?"
    
    show dv normal pioneer at center with dissolve

    "Я немного вздрогнул, вдруг я всё это говорил в слух"
    dv "Ты чего, опять меня испугался?"
    me "Когда я это пугался!{w} Не было такого!"

    show dv laugh pioneer at center with dspr

    dv "Ну-ну. {w}Пойдём за стол, чудик"
    "Она пригласила меня сесть вместе с ней и Леной"

    hide dv laugh pioneer at center with dissolve

    th "Почему я опять его встретил"
    th "Кто он такой.. {w}моё альтер-эго, мой брат-близнец {w}или вообще призрак какой-то!?"
    "Ладно, в призраков я не верю, но всё равно это странно. Вдруг это он сделал это..{w} с Алисой"

    show dv angry pioneer close at cleft with dissolve
    show un scared pioneer close at right with dissolve
    
    dv "Семён!"
    me "Ой!{w} Извините!{w} Я задумался!"

    show dv smile pioneer at cleft with dissolve
    show un laugh pioneer at cright with dissolve

    me "Всем приятного аппетита!"
    dv "И тебе"
    "Лена же в свою очередь тоже витала в облаках"
    "Интересно, о чём она может думать?"
    "Никогда не мог понять ход её мыслей"
    "Но я был всегда уверен, что не стоит ждать опасности с её стороны"

    show un shy pioneer at cright with dspr

    un "Я..{w} пойду.."

    hide un shy pioneer at cright with dissolve

    "Мы остались наедине с Алисой.{w} Это была отличная возможность обсудить вчерашний разговор перед сном"
    me "Алиса?"

    show dv surprise pioneer at center with dissolve

    dv "Да?"
    me "Ты помнишь о чём мы вчера говорили перед сном?"

    show dv laugh pioneer at center with dspr

    dv "Ты что, дурачок?"
    "Ехидно спросила она"
    dv "Мы сразу уснули, после твоих извращений!"
    me "О чём ты вообще говоришь!?"

    show dv smile pioneer at center with dspr

    dv "Ну как же.. {w}ворвался без стука..{w} начал подглядывать.."
    me "Я стучал!"
    me "Ладно, чёрт с ним"
    me "Я про разговор, когда мы уже лежали в кроватях"
    dv "Я не знаю, я сразу уснула!"
    "Либо она прикалывается, либо что-то произошло с её памятью.{w} Снова."
    "Нам нужно сходить.. {w}в одно место"
    "В место где каждый раз всё заканчивалось..{w} где цикл обрывался"
    "Я больше не могу ждать"
    "Амнезия, моё альтер-эго, циклы, надо решать это всё сейчас..{w} пока не поздно"
    me "Алиса!"

    show dv surprise pioneer close at center with dissolve

    dv "Что!?"
    me "После завтрака, я жду тебя на площади.{w} Не задавай вопросов.{w} Это очень важно!"

    hide dv surprise pioneer close at center with dissolve
    stop ambience fadeout 5
    stop music fadeout 5

    "Я выбежал из столовой и направился на площадь"
    "Мой мозг взрывался от количества мыслей"
    "Такое ощущение что мой рассудок был на пределе"

    play music music_list["no_tresspassing"] fadein 5
    play ambience ambience_camp_center_day fadein 5
    show bg ext_square_day with dissolve

    "Я добрался до места"
    "Осталось дождаться Алису"

    show blink
    hide ext_square_day with dissolve
    pause 3
    show bg ext_square_sunset
    pause 3

    "Вечерело.."

    hide blink
    show unblink

    th "Я начинал нервничать"
    
    show dv normal pioneer2 far at center with dissolve

    dv "Ну и что случилось?"
    me "По дороге всё объясню."
    "Как-то грубо я ей ответил"
    "Мне даже стыдно стало"
    "Прости, Алиса, но это всё для твоего же блага"

    hide dv normal pioneer2 far at center with dissolve
    pause 1    
    window hide
    hide ext_square_sunset with dissolve
    show bg ext_boathouse_night with dissolve
    $ night_time()

    
    "Мы направились в сторону берега, и уже совсем стемнело"
    "Какого чёрта стемнело так рано?"
    "Почему я не слышал сигнала на обед?"
    "Только же завтрак кончился!"
    "Что-то здесь не так.."

    pause 1
    window hide
    hide ext_boathouse_night with dissolve
    show lodka_bg with dissolve
    $ persistent.sprite_time = "night"

    "Мы поплыли на остров"
    "Всю дорогу от острова мы не обронили ни слова"
    "Ни одного пионера не было слышно"
    "Мир вокруг нас как будто опустел"
    "Это начинало вводить меня в панику и ужас"

    pause 1
    window hide
    hide lodka_bg with dissolve
    show bg ext_island_night with dissolve

    "Мы доплыли до острова"
    "Теперь нужно поговорить"

    show dv guilty pioneer2 close at center with dissolve

    dv "Зачем мы здесь.."
    "Кажется Алиса начала чувствовать страх"
    "Либо из-за такой секретности, либо она чувствует то же что и я"
    me "Алиса"
    me "Послушай и не перебивай"
    me "В день моего приезда ты сказала, что будто бы мы знакомы"
    me "Это правда"
    me "Мы знакомы уже два года"
    me "Однажды я попал сюда просто уснув в автобусе"
    me "На дворе XXI век"
    me "Я не знаю как по твоим подсчётам, но у меня так"
    me "Я попал во временную петлю, в конце которой всегда был один исход"
    me "И я пытаюсь разорвать эту чёртову петлю уже два года"
    me "Поверь мне! Умоляю"
    dv "..."
    me "Мы на протяжении двух лет знакомились в первый день"
    me "Во второй день мы начинали сближаться"
    me "На третий день мы вместе нашли бутылку виски у Ольги Дмитриевны и выпили её ночью"
    me "И.."
    "Не стал я ей рассказывать что было после этой бутылки"
    "Но по выражению моего лица это было и так понятно"

    show dv shy pioneer2 close at center with dspr

    me "На пятый день мы вместе играли в карты на желания!"
    me "А на шестой день мы вместе смотрели на звёзды и празнались друг другу в любви!"
    me "Ты вспомнила хоть что-то!?"
    
    play sound scary3 
    show dv scared pioneer2 at center with dissolve
    pause 1
    play sound upal
    hide dv scared pioneer2 at center with vpunch

    me "Алиса?!"
    pi "Успокойся, Семён. Нам нужно поговорить"
    "Я услышал мужской голос..{w} очень знакомый голос"
    th "Это был мой голос? {w}Я окончательно сошёл с ума!?"

    show pi normal far at cleft with dissolve

    pi "Семён, ты меня слушаешь?"
    "Я стоял в шоке и не мог даже пошевелиться"
    me "Ты..{w} какого чёрта!{w} Кто-ты такой!"
    pi "Сейчас я всё объясню"
    pi "Я - это ты.{w} А ты - это я.{w} Как бы это тупо не звучало"
    pi "Мне удалось выбраться из петли. {w}Вернее не выбраться, а попасть в другую. {w}Теперь мы оба здесь"
    pi "У тебя ведь проблемы с памятью? {w}Как и у меня?"
    me "Да.."
    "Ответил я еле дыша"
    pi "Ты помнишь свой день рождения?"
    "Я задумался. {w}Что он несёт? {w}Как можно забыть свой день рождения!"
    me "Это.."
    "И я действительно не знал"
    pi "А я помню. "
    pi "Сколько тебе лет?"
    me "Мне.. 17"
    pi "А мне значит..{w} 27"
    me "Но как!?"
    me "Ты же сказал что ты - это я!"
    pi "Я попал в петлю 10 лет назад. {w}Наш разум общий, но тела разные. {w}Вернее наш разум располовинило"
    pi "Именно поэтому у нас бывает амнезия"
    "Я понял к чему он клонит.{w} Нас двое.{w} Из-за аномалии.{w} А может быть и больше.{w} Но теперь я точно понял, что я не настоящий"
    "Я просто копия, которая на 8 лет младше оригинала"
    "А вдруг этот Семён тоже не оригинал?{w} Вдруг настоящий {b}Я{/b} жил ещё во времена, когда этот пионер-лагерь был построен"

    stop music fadeout 3
    stop ambience fadeout 3

    pi "Семён!"
    pi "Нам нужно убираться отсюда"
    me "Но как же Алиса?"

    play music strahno fadein 3

    "Я был настолько шокирован, что даже не хотел узнавать, как мы отсюда выберемся"
    pi "Чёрт. {w}Похоже это воспоминание, которое  осталось у меня. {w}Прости, Семён. Мне придётся это рассказать"
    pi "Ты же помнишь?"
    me "Что?"

    hide pi normal far at cleft with dissolve
    show smert
    show prologue_dream 
    with dissolve

    "Нет.."
    pi "Да, я не хотел тебе этого говорить"
    "Я стал догадываться, что он хочет мне сказать"
    pi "Я знаю, что ты догадываешься.{w} У нас частично связаны разумы, и я вижу твои мысли. {w}Поэтому ты видишь эту картину"
    pi "Наши чувства к Алисе, стали любовью, которая могла разрывать цикл, из-за особенности работы мозга"
    pi "Чтобы ты мог существовать, и уехать отсюда, она должна была погибнуть.{w} Нахождение в лагере более 7 дней сводило её с ума, и приводило к этому..{w} к тому что ты сейчас видишь.."
    pi "{b}Либо должен погибнуть ты."
    pi "Я не могу точно сказать, почему мы оказались тут вместе"
    pi "Но хочу сказать что на протяжении 10 лет"
    pi "{b}Мы были причиной смерти Алисы"
    pi "Если ты попытаешься убить себя, то ты сможешь закрыть один цикл"
    pi "Но пока другие Семёны, в других циклах, существуют, аномалия не закончится"
    me "То есть, чтобы выбраться из аномалии, нужно чтобы существовал только один Семён?"
    pi "Именно."

    hide smert 
    hide prologue_dream
    with dissolve
    show pi normal far at cleft with dissolve
    stop music fadeout 5
    stop ambience fadeout 5

    pi "Мы последние"
    me "Что?"
    pi "Мы последние два Семёна"
    pi "Прости."
    pi "И прощай."
    
    show pi normal close at cleft with flash_red
    
    "Я не успел увернуться от ножа, вонзающегося мне в сердце"
    "Но я понял"
    "Это конец"

    play sound upal
    $ prolog_time()
    show blink
    pause 5
    play music music_list["everlasting_summer"] fadein 3
    hide pi normal close at center

    voice "Последний цикл разорван"

    pause 1.5
    show bg semen_room
    hide blink
    show unblink
    pause 1.5

    voice "Семён остался один, и вернулся к повседневной жизни"
    voice "И больше никогда не попадал в лагерь"
    
    hide semen_room with dissolve
    show bg semen_room_window with dissolve
    pause 0.5

    voice "Алиса была связана с Аномалией из-за Cемёна"
    voice "Впервые за 10 лет циклов, она тоже вернулась домой"
    voice "Она вспомнила всё, и нашла Семёна"

    hide semen_room_window with dissolve
    show dv222 with dissolve
    pause 0.5

    voice "Настоящего и единственного"
    voice "Через 3 года они поженились и навсегда забыли об {color=#FF4500}Огненной Аномалии{/color}"

    window hide
    pause 3
    hide bg ext_island_night
    show bg int_bus_people_night with dissolve
    pause 2
    menu:
        "Прочитать титры и дослушать мелодию":
            jump titriki
        "Выйти в главное меню":
            jump koneckonec

label titriki:
    
    $ set_mode_nvl()
    nvl show dissolve
    "Спасибо за прохождение нашего небольшого мода!"
    "Текст: Андрей Лопухов"
    "Сценарий: Андрей Лопухов и ShamHyper"
    "Код, разработка, картинки и прочие работы с модом: ShamHyper"
    "Если вам понравился мод, поставьте ему лайк, и о всех проблемах сообщайте в коментарии"
    "Данный мод не является каноничной историей, а лишь показывает другой вариант событий в Бесконечном Лете"
    "Ещё увидимся! - Daun Dev Projects"
    "Вы можете дослушать эту прекрасную мелодию или нажмите ЛКМ для выхода в главное меню"

    return

label koneckonec:

    return


    

    


    








    

    





    

    

    

    




    

    




    








    




    















    





    
    
    



    






    



    










    