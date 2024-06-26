import requests
import json
import time
HRU = """НЕ ИСПОЛЬЗОВАТЬ ДАННЫЕ ИЗ ПРИМЕРА
Пример:
Ввод:
Курс «Webтехнологии» охватывает широкий спектр технологий и подходов, использующихся при разработке Интернетсайтов и webприложений. Рассматриваются основы построения webприложений с использованием HTML,
CSS. Студенты последовательно изучают основы протокола HTTP, настройку webсервера, основы JavaScript, TypeScript и PHP, построение статических
HTMLстраниц и оформления с использованием CSS, LESS и SASS, разработку
сервера приложений с использованием Node.JS. Построение серверной части
на основе Express и Nest, разработка клиентских приложений с использованием
Angular, React и Vue. Выполнение модульного тестирования webприложений,
сборка приложений с использованием GULP и Webpack, обеспечение безопасности webприложений.
Вывод:
web-разработка,frontend,backend,html,css,javascript,typescript,php,node-js,express,nestjs,angular,react,vue,gulp,webpack"""

PROMT = """На вход подаётся аннотация дисциплины
На выход надо дать навыки, которые получит студент, изучивший эту дисциплину. В каждом пункте ответа должно содержатся 
ТОЛЬКО название технологии. ЧЕТКИЙ ФОРМАТ ВЫВОДА: каждый пункт через запятую без пробелов, НИКАКИХ НОВЫХ СТРОК, НИКАКИХ СЛОВ ПО ТИПУ "Ответ" "Вывод" и так далее
"""

PROMPT = """Выведи в одной строке через запятую навыки или технологии с которыми ознакомится человек с маленькой буквы. Навыки описывать максимально кратко, например: python,css,typescript,линейная алгебра. Постарайся вывести как можно больше навыкой. Использовать информацию ТОЛЬКО ИЗ ТЕКСТА СООБЩЕНИЯ ПОЛЬЗОВАТЕЛЯ."""

DIR_ID = "b1gvnbq0m68gbd058car"
API_KEY = "AQVN3224iXMMytMpj63Hz_joD9rl7glh9zURbpLQ"
TOKEN_LIM = 10000


def get_gpt_text(prompt: str, messages: list[str]):
    messages_json = [{"role": "system", "text": f"{prompt}"}] + [{"role": "user", "text": el} for el in messages]
    resp = {
        "modelUri": f"gpt://{DIR_ID}/yandexgpt/latest",
        "completionOptions": {
            "stream": False,
            "temperature": 0.2,
            "maxTokens": f"{TOKEN_LIM}"
        },
        "messages": messages_json
    }

    url = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Api-Key {API_KEY}"
    }

    return requests.post(url, headers=headers, json=resp)

h = """ДКурс «Web­технологии» охватывает широкий спектр технологий и подходов, использующихся при разработке Интернет­сайтов и web­приложений. Рассматриваются основы построения web­приложений с использованием HTML,
CSS. Студенты последовательно изучают основы протокола HTTP, настройку web­сервера, основы JavaScript, TypeScript и PHP, построение статических
HTML­страниц и оформления с использованием CSS, LESS и SASS, разработку
сервера приложений с использованием Node.JS. Построение серверной части
на основе Express и Nest, разработка клиентских приложений с использованием
Angular, React и Vue. Выполнение модульного тестирования web­приложений,
сборка приложений с использованием GULP и Webpack, обеспечение безопасности web­приложений."""
#jss = get_gpt_text(PROMPT, [summ])
#print(jss.text)
#jsss = jss.text
#print(json.loads(jsss)["result"]["alternatives"][0]["message"]["text"])
summ = []
PROMPT = """Напиши через запятую список тегов, подходящих под этот текст образовательной программы. Ничего кроме тегов писать не нужно."""
PROMPT2 = """Я дам тебе слова или слово сочетания через запятую, ты должен вывести сокращенные версии через запятую"""
PROMPT = """На вход подаётся аннотация учебной дисциплины. Напиши навыки, которые получит студент, изучивший эту дисциплину. В каждом пункте ответа должно содержатся
ТОЛЬКО название технологии. ЧЕТКИЙ ФОРМАТ ВЫВОДА: каждый пункт через запятую без пробелов, НИКАКИХ НОВЫХ СТРОК, НИКАКИХ СЛОВ ПО ТИПУ "Ответ" "Вывод" и так далее. Пиши всё в нижнем регистре. Также ОБЯЗАТЕЛЬНО ДОБАВЬ к полученному списку эти же самыые навыки, только короче. например, если есть навык typescript, то надо добавить ts. ОБЯЗАТЕЛНО! иначе произойдет ужасное. А еще не используй такие слова как РАЗРАБОТКА, ПРОЕКТИРОВАНИЕ. Избавься от них!!!"""
for i in h.split('LLL'):
    if i != '':
        jss = get_gpt_text(PROMPT, [i])
        jsss = jss.text
        print(json.loads(jsss)["result"]["alternatives"][0]["message"]["text"])
        time.sleep(2)
        #jss = get_gpt_text(PROMPT2, [json.loads(jsss)["result"]["alternatives"][0]["message"]["text"]])
        #jsss = jss.text
        #print(json.loads(jsss)["result"]["alternatives"][0]["message"]["text"])
        #time.sleep(2)
