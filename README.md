[![Check code style](https://github.com/JetBrains-Research/formal-lang-course/actions/workflows/code_style.yml/badge.svg)](https://github.com/JetBrains-Research/formal-lang-course/actions/workflows/code_style.yml)
[![Code style](https://img.shields.io/badge/Code%20style-black-000000.svg)](https://github.com/psf/black)
---
# Python course

Курс "Программирование на Python".

Полезные ссылки:
- [Таблица с текущими результатами](https://docs.google.com/spreadsheets/d/1h29GyiGds4PvkNSZqw_1VYGAAcFNKr0j-YzTJLWTHR4/edit?usp=sharing)
- [Список задач](https://github.com/Krekep/spbu-python-course/tree/main/tasks)
- [Стиль кода](https://www.python.org/dev/peps/pep-0008/)

Технологии:
- Python 3.8+
- Pytest для unit тестирования
- GitHub Actions для CI
- Google Colab для постановки и оформления экспериментов
- Сторонние пакеты из `requirements.txt` файла
- Английский язык для документации или самодокументирующийся код

## Работа с проектом

- Для выполнения домашних практических работ необходимо сделать **приватный** `fork` этого репозитория к себе в `GitHub`.
- Рекомендуется установить [`pre-commit`](https://pre-commit.com/#install) для поддержания проекта в адекватном состоянии.
  - Установить `pre-commit` можно выполнив следующую команду в корне вашего проекта:
    ```shell
    pre-commit install
    ```
  - Отформатировать код в соответствии с принятым стилем можно выполнив следующую команду в корне вашего проекта:
    ```shell
    pre-commit run --all-files
    ```
- Ссылка на свой `fork` репозитория размещается в [таблице](https://docs.google.com/spreadsheets/d/1h29GyiGds4PvkNSZqw_1VYGAAcFNKr0j-YzTJLWTHR4/edit?usp=sharing) курса с результатами.
- В свой репозиторий необходимо добавить проверяющих с `admin` правами на чтение, редактирование и проверку `pull-request`'ов.

## Домашние практические работы

### Выполнение домашнего задания

- Каждое домашнее задание выполняется в отдельной ветке. Ветка должна иметь осмысленное название.
- При выполнении домашнего задания в новой ветке необходимо открыть соответствующий `pull-request` в `main` вашего `fork`.
- `Pull-request` снабдить понятным названием и описанием с соответствующими пунктами прогресса.
- Проверка заданий осуществляется посредством `review` вашего `pull-request`.
- Как только вы считаете, что задание выполнено, вы можете запросить `review` у проверяющего. Обратите внимание, что CI должен проходить.
- Количество проверок ограничено тремя. Первый запрос `review` должен быть _до_ **дедлайна**. После трёх неудачных проверок баллы за задачу сгорают.
- Когда проверка будет пройдена, и задание **зачтено**, его необходимо `merge` в `main` вашего `fork`.

### Получение оценки за домашнюю работу

- Если `review` запрошено _до_ **дедлайна** и ваша работа **зачтена**, то вы получаете **полный балл за домашнюю работу**.
- Если `review` запрошено _после_ **дедлайна** и ваша работа **зачтена**, то вы получаете **половину полного балла за домашнюю работу**.

## Код

- Исходный код практических задач по программированию размещайте в папке `project`.
- Файлам и модулям даем осмысленные имена, в соответствии с официально принятым стилем.
- Структурируем код, используем как классы, так и отдельно оформленные функции.
- К функциям, классам, модулям должна быть написана документация.

## Тесты

- Тесты для домашних заданий размещайте в папке `tests`.
- Формат именования файлов с тестами `test_[какой модуль\класс\функцию тестирует].py`.
- Для работы с тестами рекомендуется использовать [`pytest`](https://docs.pytest.org/en/stable/).
- Для запуска тестов необходимо из корня проекта выполнить следующую команду:
  ```shell
  python ./scripts/run_tests.py
  ```

## Структура репозитория

```text
.
├── .github - файлы для настройки CI и проверок
├── project - исходный код домашних работ
├── scripts - вспомогательные скрипты для автоматизации разработки
├── tasks - файлы с описанием домашних заданий
├── tests - директория для unit-тестов домашних работ
├── README.md - основная информация о проекте
└── requirements.txt - зависимости для настройки репозитория
```

## Оценка за курс

Оценка за курс складывается из баллов, полученных за работу в семестре.

Задачи разделены на взвешенные блоки, где коэффициент это баллы за летучку (контрольная работа на 5 минут).
Пусть например, в курсе два блока по 2 задачи и 2 летучки. Пусть за первые две задачи получено 5 баллов, за оставшиеся 1 и 2 соответственно.
Пусть за летучки получено 1 и 0.5 баллов. Тогда оценка за курс: $(5 + 5) * 1 + (1 + 2) * 0.5 = 11.5$

Баллы конвертируются в оценки следующим образом:

|    Балл     | ECTS  | Классика |
| :---------: | :---: | :------: |
| (90 -- 100] |   A   |    5     |
| (80 -- 90]  |   B   |    4     |
| (70 -- 80]  |   C   |    4     |
| (60 -- 70]  |   D   |    3     |
| (50 -- 60]  |   E   |    3     |
|  [0 -- 50]  |   F   |    2     |

## Контакты

- Павел Алимов [@Krekep](https://github.com/Krekep)
- Ссылка на Google Colab [Задание 10](https://colab.research.google.com/drive/1SfcVLStDQWC3ylCNQ790Hed2KRng7VtM?usp=sharing)
