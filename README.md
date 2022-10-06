# Parsing - Парсер на тренировочном сайте https://scrapingclub.com.

## Описание:
После запуска файла code.py записывает данные в xlsx файл(exel-таблицу), парсит наименование товара, описание, цену и ссылку на фото товара, также если раскомментировать строки то будут сохраняться фото товара в папку image.

### Использованный стек технологий:
- XlsxWriter~=3.0.3
- requests~=2.28.1
- beautifulsoup4~=4.11.1

### Настройка и запуск на компьютере
Клонируем проект:
```
https://github.com/32Aleksey32/Parsing.git
```
Устанавливаем виртуальное окружение:
```
python -m venv venv
```
Активируем виртуальное окружение:
```
source venv/Scripts/activate
```
Устанавливаем зависимости:
```
python -m pip install --upgrade pip
pip install -r requirements.txt
```
Запускаем парсер:
```
python code.py
```
