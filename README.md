# Проект Homework_11_2.

## Описание:
Данный проект создан для разработки программы по работе с банковскими операциями клиента.

## Установка:
1. Клонируйте репозиторий:
```
git clone https://github.com/Elena041/homework_11_2
```

В ветке feature/homework_11_1 ,в файле tests присутвуют предложные изменения по данному проекту

2. Установите зависимости
```
poetry install
```
## Тестирование
Производятся из пакета tests в котором находятся модули (test_ + имя тестируемго модуля из src)
1.Запуск теста
```
pytest 
```
2.Запуск всех тестов с оценкой покрытия
```
pytest --cov
```

## Обновление
1. Созданы генераторы в src/generators.py
2. Созданы тесты к этому файлу (tests/test_generators.py)
3. Создан декоратор @log в src/decorators.py и тест к нему(tests/test_decorators.py)