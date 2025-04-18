## Установка python

sudo apt update
sudo apt install python3 python3-pip

## Установка PyCharm

sudo snap install pycharm-community --classic

## Запуск PyCharm

pycharm

## Установка Far Manager
# Установка wime для работы с Far Manager

sudo apt install wine

# Загрузка Far Manager

wget https://www.farmanager.com/Far30b.x64.20240510.msi

# Версия python

python3 -V

# Просмотр списка установленных пакетов

pip list

# Создание репозитория в котором будет установленно виртуальное окружение

mkdir Projects Projects/django
cd Projects/django

# Запуск PyCharm

pycharm-community

# Создание виртуального окружения

python3 -m venv djvenv

# Если возникает ошибка при создании

#sudo apt install python3.10-venv

# Запуск вирутального окружения

source djvenv/bin/activate

# При успешном выполнении появится надпись "djvenv"
# При просмотре установленных пакетов внутри виртуального окружения мы увидим всего два пакета

pip list

# Команда для выхода из виртуального окружения

deactivate

## Установка Django

pip install django==4.2.1

# При просмотре установленных пакетов теперь будут добавлены дополнительные пакеты

pip list

# Просмотр команд ядра

gjango-admin

## Создание сайта
#django-admin startproject <site_name>

django-admin startproject sitewomen
cd sitewomen

# Применение маграции к базе данных
#python manage.py migrate

python manage.py runserver

python manage.py startapp women