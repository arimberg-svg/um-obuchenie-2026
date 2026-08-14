# -*- coding: utf-8 -*-
"""Generate static pages for UM supplier trainings."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent

STORES = [
    "г. Тюмень, ул. Дружбы, 66 (инструмент)",
    "г. Тюмень, ул. Дружбы, 66 (сантехника)",
    "г. Тюмень, ул. Авторемонтная, 49",
    "г. Тюмень, ул. Республики, 256а, корп. 5",
    "г. Тюмень, ул. Бабарынка, 10б",
    "г. Тюмень, Старый Тобольский тракт 3 км, 6А",
    "п. Березняковский, ул. Омутинская, 26а",
    "с/о Чайка, ул. Центральная, 108",
    "г. Тюмень, Московский тракт 6 км, стр. 2",
    "с. Луговое, ул. Ивана Усольцева, 2",
    "с. Червишево, Юбилейный квартал, 1а",
    "рп Винзили, ул. Полевая, 1в",
    "рп Боровский, ул. Набережная, 66",
    "д. Решетникова, ул. Свободы, 12",
    "д. Ожогина, ул. Садовая, 1в",
    "с. Мальково, ул. Юбилейная, 8А",
    "с. Ембаево, ул. Бульварная, 2А",
    "д. Ушакова, ул. Новая, 16",
    "с. Перевалово, ул. Трактовая, 44",
    "с. Успенка, ул. Коммунаров, 3а",
]

# Two nearby stores per day
ROUTES = [
    (0, 1),   # Дружбы инструмент + сантехника
    (2, 3),   # Авторемонтная + Республики
    (4, 8),   # Бабарынка + Московский тракт
    (5, 7),   # Ст. Тобольский + Чайка
    (9, 16),  # Луговое + Ембаево
    (12, 6),  # Боровский + Березняковский
    (10, 18), # Червишево + Перевалово
    (19, 11), # Успенка + Винзили
    (13, 14), # Решетникова + Ожогина
    (15, 17), # Мальково + Ушакова
]

WD = {"пн": "пн", "вт": "вт", "ср": "ср", "чт": "чт", "пт": "пт"}

# 5 weekdays after office: Wed Thu Fri Mon Tue, 10:30 and 12:00
def visits_for(dates, route_ids):
    """dates: list of (date, weekday) length 5; route_ids length 5."""
    rows = []
    times = [("10:30–10:55", "10:30"), ("12:00–12:25", "12:00")]
    for (d, wd), rid in zip(dates, route_ids):
        a, b = ROUTES[rid]
        rows.append((d, wd, times[0][0], STORES[a]))
        rows.append((d, wd, times[1][0], STORES[b]))
    return rows


SUPPLIERS = [
    {
        "slug": "greenworks",
        "theme": "greenworks",
        "short": "Гринворкстулс",
        "title": "Гринворкстулс ООО",
        "inn": "ИНН 9705051762. Официальный представитель Greenworks: аккумуляторная садовая техника и электроинструмент.",
        "card": "Greenworks: аккумуляторная садовая техника",
        "office_iso": "15.09.2026",
        "office_long": "Вторник 15 сентября 2026, 14:00–16:00 (2 часа).",
        "office_prog": "Аудитория: руководители и ключевые продавцы сети. Программа: платформы АКБ, что продавать осенью/зимой, типичные возражения, сервис.",
        "kb_until": "1 сентября 2026",
        "kb_pill": "01.09.2026",
        "kb": "Карточка линейки, совместимость аккумуляторных платформ 24/40/80 В, зимняя техника (снегоуборщики), расходники, гарантия, FAQ для продавца, фото/видео для обучения.",
        "logo": "../img/greenworks-mark.svg",
        "office_topic": "Greenworks",
        "dates": [
            ("16.09.2026", "ср"), ("17.09.2026", "чт"), ("18.09.2026", "пт"),
            ("21.09.2026", "пн"), ("22.09.2026", "вт"),
        ],
        "routes": [0, 1, 2, 3, 4],
    },
    {
        "slug": "finskie-kraski",
        "theme": "tikkurila",
        "short": "ТД Финские краски",
        "title": "ТД Финские краски ООО",
        "inn": "ИНН 7224044053. Лакокрасочные материалы Tikkurila, ТЕКС, Finncolor: краски, лаки, антисептики, колеровка.",
        "card": "Tikkurila, ТЕКС, Finncolor",
        "office_iso": "29.09.2026",
        "office_long": "Вторник 29 сентября 2026, 14:00–16:00 (2 часа).",
        "office_prog": "Программа: что рекомендовать осенью, колеровка, деревозащита, кросс-продажи инструмента.",
        "kb_until": "15 сентября 2026",
        "kb_pill": "15.09.2026",
        "kb": "Линейки интерьер / фасад / дерево, колеровка, расход, типичные ошибки подбора, скрипт продавца, веера и работа со студией цвета.",
        "logo": "../img/tikkurila.svg",
        "office_topic": "Tikkurila",
        "dates": [
            ("30.09.2026", "ср"), ("01.10.2026", "чт"), ("02.10.2026", "пт"),
            ("05.10.2026", "пн"), ("06.10.2026", "вт"),
        ],
        "routes": [1, 2, 3, 4, 5],
    },
    {
        "slug": "professionalnyy-instrument",
        "theme": "knipex",
        "short": "Профессиональный инструмент",
        "title": "Профессиональный инструмент ООО",
        "inn": "ИНН 9729328131. Эксклюзивный импортёр KNIPEX, WERA, BESSEY, RENNSTEIG, ZALTAR. germantools.ru",
        "card": "KNIPEX, WERA, BESSEY, RENNSTEIG, ZALTAR",
        "office_iso": "13.10.2026",
        "office_long": "Вторник 13 октября 2026, 14:00–16:00 (2 часа).",
        "office_prog": "Живой показ инструмента, сценарии для электрика и сантехника, как отличать от масс-маркета.",
        "kb_until": "29 сентября 2026",
        "kb_pill": "29.09.2026",
        "kb": "Для кого какой бренд, диэлектрический инструмент до 1000 В, струбцины BESSEY, металлорежущая оснастка ZALTAR, ходовые наборы, аргументы цены.",
        "logo": "../img/knipex2.svg",
        "office_topic": "KNIPEX / WERA / BESSEY",
        "dates": [
            ("14.10.2026", "ср"), ("15.10.2026", "чт"), ("16.10.2026", "пт"),
            ("19.10.2026", "пн"), ("20.10.2026", "вт"),
        ],
        "routes": [2, 3, 4, 5, 6],
    },
    {
        "slug": "centr-krasok-vostok",
        "theme": "dulux",
        "short": "Центр красок Восток",
        "title": "Центр красок Восток ООО",
        "inn": "ИНН 7204189068. Представитель AkzoNobel: Dulux, Marshall, Hammerite, Pinotex.",
        "card": "Dulux, Marshall, Hammerite, Pinotex",
        "office_iso": "27.10.2026",
        "office_long": "Вторник 27 октября 2026, 14:00–16:00 (2 часа).",
        "office_prog": "",
        "kb_until": "13 октября 2026",
        "kb_pill": "13.10.2026",
        "kb": "Интерьер и фасад Dulux, металл Hammerite, дерево Pinotex, колеровка AkzoNobel, что предлагать к холодам.",
        "logo": "../img/dulux2.svg",
        "office_topic": "Dulux / AkzoNobel",
        "dates": [
            ("28.10.2026", "ср"), ("29.10.2026", "чт"), ("30.10.2026", "пт"),
            ("02.11.2026", "пн"), ("03.11.2026", "вт"),
        ],
        "routes": [3, 4, 5, 6, 7],
        "extra": "4 ноября (День народного единства) в графике свободен.",
    },
    {
        "slug": "trio-diamant",
        "theme": "trio",
        "short": "Трио Диамант ЛТД",
        "title": "Трио Диамант ЛТД ООО",
        "inn": "ИНН 9718083923. Алмазный инструмент Trio Diamond и Hilberg: диски, коронки, оснастка.",
        "card": "Trio Diamond, Hilberg",
        "office_iso": "10.11.2026",
        "office_long": "Вторник 10 ноября 2026, 14:00–16:00 (2 часа).",
        "office_prog": "",
        "kb_until": "27 октября 2026",
        "kb_pill": "27.10.2026",
        "kb": "Подбор диска под материал (плитка, бетон, металл), мокрый и сухой рез, отличие Trio Diamond и Hilberg, коронки и оснастка МФИ.",
        "logo": "../img/trio.svg",
        "office_topic": "Алмазный инструмент",
        "dates": [
            ("11.11.2026", "ср"), ("12.11.2026", "чт"), ("13.11.2026", "пт"),
            ("16.11.2026", "пн"), ("17.11.2026", "вт"),
        ],
        "routes": [4, 5, 6, 7, 8],
    },
    {
        "slug": "esab",
        "theme": "esab",
        "short": "ЭСАБ",
        "title": "ЭСАБ ООО",
        "inn": "Сварка и резка металлов: электроды, проволока, аппараты, СИЗ ESAB. Заводы в России, в том числе в Тюмени.",
        "card": "Сварка и резка ESAB",
        "office_iso": "24.11.2026",
        "office_long": "Вторник 24 ноября 2026, 14:00–16:00 (2 часа).",
        "office_prog": "",
        "kb_until": "10 ноября 2026",
        "kb_pill": "10.11.2026",
        "kb": "Подбор электродов и проволоки для розницы, бытовые и промышленные аппараты, СИЗ, хранение материалов, ходовые позиции зимы.",
        "logo": "../img/esab.svg",
        "office_topic": "Сварка и резка",
        "dates": [
            ("25.11.2026", "ср"), ("26.11.2026", "чт"), ("27.11.2026", "пт"),
            ("30.11.2026", "пн"), ("01.12.2026", "вт"),
        ],
        "routes": [5, 6, 7, 8, 9],
        "dark_logo": True,
    },
    {
        "slug": "severnye-strely",
        "theme": "arrows",
        "short": "Северные Стрелы",
        "title": "Северные Стрелы ООО",
        "inn": "ИНН 7811742366. Электро- и бензоинструмент, садовая техника, сварка, компрессоры, запчасти. arrows.ru",
        "card": "Электро- и бензоинструмент, сад, сварка",
        "office_iso": "08.12.2026",
        "office_long": "Вторник 8 декабря 2026, 14:00–16:00 (2 часа).",
        "office_prog": "",
        "kb_until": "24 ноября 2026",
        "kb_pill": "24.11.2026",
        "kb": "Ходовые позиции сезона, запчасти, компрессоры и тепловые пушки, кросс-продажи, сервис.",
        "logo": "../img/arrows.svg",
        "office_topic": "Инструмент и техника",
        "dates": [
            ("09.12.2026", "ср"), ("10.12.2026", "чт"), ("11.12.2026", "пт"),
            ("14.12.2026", "пн"), ("15.12.2026", "вт"),
        ],
        "routes": [6, 7, 8, 9, 0],
    },
    {
        "slug": "agava",
        "theme": "agava",
        "short": "Агава",
        "title": "Агава ООО",
        "inn": "ИНН 6674378752. Сантехника оптом: смесители, унитазы, душ, трубы, насосы, мебель для ванных. agava-ural.ru",
        "card": "Сантехника оптом",
        "office_iso": "22.12.2026",
        "office_long": "Вторник 22 декабря 2026, 14:00–16:00 (2 часа). До новогодних каникул.",
        "office_prog": "Выезды — 23–29 декабря, до праздников. В маршруте есть зал сантехники на Дружбы, 66.",
        "kb_until": "8 декабря 2026",
        "kb_pill": "08.12.2026",
        "kb": "Бытовая и инженерная сантехника, инсталляции, смесители, типовые комплекты, частые ошибки монтажа для консультации покупателя.",
        "logo": "../img/agava.svg",
        "office_topic": "Сантехника",
        "dates": [
            ("23.12.2026", "ср"), ("24.12.2026", "чт"), ("25.12.2026", "пт"),
            ("28.12.2026", "пн"), ("29.12.2026", "вт"),
        ],
        "routes": [7, 8, 9, 0, 1],  # includes Дружбы сантехника
        "extra": "Новогодние каникулы (31.12–08.01) в графике свободны.",
    },
    {
        "slug": "rusgeokom",
        "theme": "rusgeocom",
        "short": "Русгеоком",
        "title": "Русгеоком ООО",
        "inn": "ИНН 7716540377. Геодезия и измерения: лазерное сканирование, инженерные изыскания, тахеометры, GNSS. rusgeo.com",
        "card": "Геодезия и измерения",
        "office_iso": "12.01.2027",
        "office_long": "Вторник 12 января 2027, 14:00–16:00 (2 часа). После новогодних каникул.",
        "office_prog": "",
        "kb_until": "22 декабря 2026",
        "kb_pill": "22.12.2026",
        "kb": "Что продавать в рознице (уровни, дальномеры), когда вести на спецтехнику, поверка, бытовые vs профессиональные приборы.",
        "logo": "../img/rusgeocom.svg",
        "office_topic": "Геодезия",
        "dates": [
            ("13.01.2027", "ср"), ("14.01.2027", "чт"), ("15.01.2027", "пт"),
            ("18.01.2027", "пн"), ("19.01.2027", "вт"),
        ],
        "routes": [8, 9, 0, 1, 2],
    },
    {
        "slug": "elbin",
        "theme": "elbin",
        "short": "Элбин · Champion",
        "title": "Элбин ООО",
        "inn": "ИНН 7841065030. ООО «Элбин» — расчёты и документы торговой марки Champion: садовая, строительная и силовая техника. champion.ru",
        "card": "Садовая техника Champion",
        "office_iso": "26.01.2027",
        "office_long": "Вторник 26 января 2027, 14:00–16:00 (2 часа).",
        "office_prog": "",
        "kb_until": "12 января 2027",
        "kb_pill": "12.01.2027",
        "kb": "Линейки Champion: косилки, триммеры, пилы, генераторы, расходники, сервис и гарантия, что класть на полку в феврале.",
        "logo": "../img/elbin.svg",
        "office_topic": "Champion",
        "dates": [
            ("27.01.2027", "ср"), ("28.01.2027", "чт"), ("29.01.2027", "пт"),
            ("01.02.2027", "пн"), ("02.02.2027", "вт"),
        ],
        "routes": [9, 0, 1, 2, 3],
    },
    {
        "slug": "onemoto",
        "theme": "n1tools",
        "short": "ИП Миронов · Number One",
        "title": "ИП Миронов Игорь Михайлович",
        "inn": "ИНН 590706361659. Бренд Number One: электроинструмент, бензотехника, садовая техника, сварка и оснастка. n1tools.ru",
        "card": "Электроинструмент Number One",
        "office_iso": "09.02.2027",
        "office_long": "Вторник 9 февраля 2027, 14:00–16:00 (2 часа).",
        "office_prog": "",
        "kb_until": "26 января 2027",
        "kb_pill": "26.01.2027",
        "kb": "Линейки Number One (электро-, бензо-, сад, сварка), ходовые позиции, гарантия и сервис, что предлагать в рознице.",
        "logo": "../img/n1tools.svg",
        "office_topic": "Number One",
        "dates": [
            ("10.02.2027", "ср"), ("11.02.2027", "чт"), ("12.02.2027", "пт"),
            ("15.02.2027", "пн"), ("16.02.2027", "вт"),
        ],
        "routes": [5, 6, 7, 8, 9],
    },
]


def visit_rows(s):
    return visits_for(s["dates"], s["routes"])


def coverage_check():
    from collections import Counter
    c = Counter()
    for s in SUPPLIERS:
        rows = visit_rows(s)
        assert len(rows) == 10, s["slug"]
        stores = [r[3] for r in rows]
        assert len(set(stores)) == 10, (s["slug"], stores)
        c.update(stores)
    print("store coverage:", dict(c))
    print("min/max", min(c.values()), max(c.values()), "n stores", len(c))


def page_html(s):
    rows = visit_rows(s)
    trs = "\n".join(
        f"          <tr><td>{d}, {wd}</td><td>{t}</td><td>Магазин {i}</td></tr>"
        for i, (d, wd, t, _st) in enumerate(rows, 1)
    )
    extra = f"<p>{s['extra']}</p>" if s.get("extra") else ""
    prog = f" {s['office_prog']}" if s.get("office_prog") else ""
    hero_cls = "page-hero dark-logo" if s.get("dark_logo") else "page-hero"
    first = rows[0][0]
    last = rows[-1][0]
    return f"""<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>На согласование — {s['short']}</title>
  <link rel="stylesheet" href="../css/style.css">
</head>
<body class="theme-{s['theme']}">
  <div class="wrap">
    <div class="{hero_cls}">
      <p class="eyebrow">У Михалыча · Тюмень · на согласование</p>
      <img class="logo-mark" src="{s['logo']}" alt="">
      <h1>{s['title']}</h1>
      <p class="lede">{s['inn']}</p>
      <p style="margin:12px 0 0"><a href="../index.html">← Общий план</a></p>
    </div>

    <div class="pills">
      <span class="pill">БЗ до {s['kb_pill']}</span>
      <span class="pill">Офис {s['office_iso']}, 14:00–16:00</span>
      <span class="pill">10 магазинов {first}–{last}</span>
    </div>

    <h2>Что просим согласовать</h2>
    <div class="task">
      <div class="n">Задание 1 · база знаний</div>
      <h3>Сдать материалы до {s['kb_until']}</h3>
      <p>{s['kb']}</p>
    </div>
    <div class="task">
      <div class="n">Задание 2 · офис</div>
      <h3>Провести обучение в офисе</h3>
      <p><strong>{s['office_long']}</strong>{prog}</p>
    </div>
    <div class="task">
      <div class="n">Задание 3 · магазины</div>
      <h3>Мини-обучения в 10 магазинах, по 20–30 мин</h3>
      <p>После офиса: 2 соседние точки в день, 10:30 и 12:00, пять рабочих дней. Сеть проводит выезды по согласованной подаче. Просим подтвердить, нужен ли тренер с вашей стороны на точках.</p>
      <table>
        <thead><tr><th>Дата</th><th>Время</th><th>Магазин</th></tr></thead>
        <tbody>
{trs}
        </tbody>
      </table>
      {extra}
    </div>

    <div class="ok">
      <h3>Подтверждение поставщика</h3>
      <p>Просим ответить письмом: даты подходят / предложить другие слоты; кто ведёт офис; будете ли на выездах в магазины; когда пришлёте пакет для базы знаний.</p>
    </div>
    <footer>Страница для согласования графика обучений сети «У Михалыча».</footer>
  </div>
</body>
</html>
"""


def month_key(date):
    d, m, y = date.split(".")
    names = {
        "09": ("Сентябрь", "2026"),
        "10": ("Октябрь", "2026"),
        "11": ("Ноябрь", "2026"),
        "12": ("Декабрь", "2026"),
        "01": ("Январь", "2027"),
        "02": ("Февраль", "2027"),
    }
    return f"{names[m][0]} {names[m][1]}", m + y


def index_html():
    cards = []
    office_rows = []
    months = {}
    order = ["092026", "102026", "112026", "122026", "012027", "022027"]
    labels = {
        "092026": "Сентябрь 2026",
        "102026": "Октябрь 2026",
        "112026": "Ноябрь 2026",
        "122026": "Декабрь 2026",
        "012027": "Январь 2027",
        "022027": "Февраль 2027",
    }
    for k in order:
        months[k] = {"kb": [], "office": []}

    for s in SUPPLIERS:
        cards.append(f"""      <a class="card" href="p/{s['slug']}.html">
        <div class="meta">{s['office_iso']} · офис 14:00–16:00 · 10 магазинов</div>
        <h3>{s['short']}</h3>
        <p>{s['card']}</p>
      </a>""")
        office_rows.append(
            f"        <tr><td>{s['office_iso']}, вт</td><td>14:00–16:00</td>"
            f"<td>{s['short']}</td><td>{s['office_topic']}</td>"
            f"<td><a href=\"p/{s['slug']}.html\">открыть</a></td></tr>"
        )
        om = s["office_iso"][3:5] + s["office_iso"][6:]
        months[om]["office"].append(f"{s['short']} {s['office_iso'][:5]}")
        kb = s["kb_pill"]
        km = kb[3:5] + kb[6:]
        if km in months:
            months[km]["kb"].append(s["short"])

    month_trs = []
    for k in order:
        m = months[k]
        kb = ", ".join(m["kb"]) or "—"
        of = ", ".join(m["office"]) or "—"
        month_trs.append(
            f"        <tr><td>{labels[k]}</td><td>{kb}</td><td>{of}</td></tr>"
        )

    return f"""<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Общий план обучений — У Михалыча, Тюмень</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>
  <div class="wrap">
    <div class="topbar">
      <img class="logo" src="img/um-mikhalych.png" alt="У Михалыча">
      <div class="tag">Тюмень · сентябрь 2026 — февраль 2027</div>
    </div>

    <header class="site">
      <div>
        <p class="eyebrow">Сеть магазинов «У Михалыча»</p>
        <h1>Общий план обучений по поставщикам</h1>
        <p class="lede">Сначала материал в базу знаний, затем обучение в офисе (вторник 14:00–16:00), затем выезды: каждый поставщик — минимум в 10 магазинах. Ниже сводка и ссылки на страницы для согласования.</p>
      </div>
      <div class="pills">
        <span class="pill">11 поставщиков</span>
        <span class="pill">11 офисных сессий</span>
        <span class="pill">110 выездов</span>
      </div>
    </header>

    <div class="stats">
      <div class="stat"><b>11</b><span>материалов в базу знаний</span></div>
      <div class="stat"><b>11 × 2 ч</b><span>офис, вторник 14:00–16:00</span></div>
      <div class="stat"><b>110</b><span>выездов: 11 × 10 магазинов</span></div>
      <div class="stat"><b>20 точек</b><span>Тюмень и Тюменский район</span></div>
    </div>

    <div class="note">
      <strong>Порядок по каждому поставщику:</strong> сдать материалы для базы знаний → провести обучение в офисе → мини-обучения в залах. После офиса — 5 рабочих дней, по 2 соседние точки (10:30 и 12:00, по 25 мин). Выезды не ставятся на день офиса этой компании. 4 ноября 2026 и новогодние каникулы свободны.
    </div>

    <h2>Страницы для согласования</h2>
    <p class="lede">Откройте страницу поставщика и отправьте ссылку. На ней даты, задания и блок подтверждения.</p>
    <div class="grid">
{chr(10).join(cards)}
    </div>

    <h2>Сводка по месяцам</h2>
    <table>
      <thead>
        <tr>
          <th>Месяц</th>
          <th>База знаний</th>
          <th>Офис, вт 14:00–16:00</th>
        </tr>
      </thead>
      <tbody>
{chr(10).join(month_trs)}
      </tbody>
    </table>

    <h2>Полный календарь офиса</h2>
    <table>
      <thead>
        <tr><th>Дата</th><th>Время</th><th>Поставщик</th><th>Тема</th><th>Страница</th></tr>
      </thead>
      <tbody>
{chr(10).join(office_rows)}
      </tbody>
    </table>

    <footer>
      Адреса магазинов: <a href="https://gvozditut.ru/stores/">gvozditut.ru/stores</a>, только Тюмень и Тюменский район. Склад/ПВЗ на Тимуровцев, 1а стр. 8 в выезды зала не включён.
    </footer>
  </div>
</body>
</html>
"""


def readme():
    lines = [
        "# План обучений поставщиков — «У Михалыча», Тюмень",
        "",
        "Сентябрь 2026 — февраль 2027. Каждый поставщик: материалы в базу знаний, офис (вт 14:00–16:00) и **минимум 10 магазинов**.",
        "",
        "## Публичные ссылки",
        "",
        "**Общий план:** https://arimberg-svg.github.io/um-obuchenie-2026/",
        "",
        "Репозиторий: https://github.com/arimberg-svg/um-obuchenie-2026",
        "",
        "### Страницы для согласования с поставщиками",
        "",
        "| Поставщик | Офис | Магазины | Ссылка |",
        "|---|---|---|---|",
    ]
    for s in SUPPLIERS:
        rows = visit_rows(s)
        span = f"{rows[0][0]}–{rows[-1][0]}"
        url = f"https://arimberg-svg.github.io/um-obuchenie-2026/p/{s['slug']}.html"
        lines.append(f"| {s['short']} | {s['office_iso']}, 14:00–16:00 | 10 точек, {span} | [открыть]({url}) |")
    lines.append("")
    return "\n".join(lines) + "\n"


def main():
    coverage_check()
    (ROOT / "index.html").write_text(index_html(), encoding="utf-8")
    for s in SUPPLIERS:
        (ROOT / "p" / f"{s['slug']}.html").write_text(page_html(s), encoding="utf-8")
    (ROOT / "README.md").write_text(readme(), encoding="utf-8")
    print("written", 1 + len(SUPPLIERS), "html + readme")


if __name__ == "__main__":
    main()
