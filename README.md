# parser_project

Парсер для отдельных страниц сайта https://qgold.com/pl/Jewelry-Rings-2·Stone-Rings

```
О проекте:

```
Парсинг осуществляется c помощью модуля requests через запросы API.
Задача была создать парсер без использования Selenium и Chrome driver.

В файле sync.py реализован синхронный код парсера,
в файле async.py будет реализован асинхронный код парсера(еще в разработке) с помощью Aiohttp 
и модуля asyncio.

Проект еще не закончен, находится на стадии разработки.

```
Что еще нужно реализовать: Нужно доделать ассинхронный вариант кода в файле asyns.py, а также добавить парсинг по другим страницам категорий.

```
О проекте:

```

Как запустить проект:

```
Клонировать репозиторий и перейти в него в командной строке:

```
git@github.com:Dmitriy8854/parser_project.git
```
cd parser_project

```
Cоздать и активировать виртуальное окружение:

```
python -m venv venv
```
source venv/bin/activate

```
Установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
```
pip install -r requirements.txt

```
Запустить проект:

```
python sync

```
### **Автор:**
- [Морозов Дмитрий]

