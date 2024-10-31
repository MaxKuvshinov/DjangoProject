# Проект: Интернет-магазина

## Описание проекта: 
Создаем проект интернет-магазина, который будете дорабатывать на каждом уроке в течение всего курса.

## Основные задачи:
- `Задание 1.` Настройка проекта. Создать новую директорию для проекта и настроить виртуальное окружение. 
Инициализировать новый проект Django внутри этой директории.
- `Задание 2.` Создание и настройка приложения. Создать новое приложение под названием `catalog` в проекте. Зарегистрировать приложение в настройках проекта. Настроить маршрутизацию для нового приложения, добавив соответствующие URL-адреса.
- `Задание 3.` Создание шаблонов. Подготовить два HTML-шаблона: для домашней страницы и для страницы с контактной информацией. Для стилизации страниц используйте Bootstrap.
- `Задание 4.` Реализация контроллеров. Создать контроллер для отображения домашней страницы. Создать контроллер для отображения страницы с контактной информацией. Настроить маршрутизацию для этих контроллеров.
- `Дополнительное задание.` Реализовать форму обратной связи на странице контактов. Настроить обработку данных формы в контроллере, чтобы отображать сообщение об успешной отправке данных.
- `Задание 5.` Подключить СУБД PostgreSQL для работы в проекте. Создайте базу данных в ручном режиме. Внесите изменения в настройки подключения в файле settings.py.
- `Задание 6.`В приложении каталога создать модели Product и Category и опишите для них базовые настройки.
- `Задание 7.`Перенести отображение моделей в базу данных с помощью инструмента миграций. Для этого создать миграции для новых моделей и примените миграции.
- `Задание 8.`Создайте суперпользователя. Зарегистрируйте модели Product и Category в админке.
- `Задание 9.`Через инструмент shell заполнить список категорий, а также выбрать список категорий, применив произвольные рассмотренные фильтры.
- `Задание 10.`Сформировать фикстуры для моделей Category и Product.
- `Задание 11.`Создать кастомную команду для добавления тестовых продуктов. В команде удалить все существующие данные из базы перед добавлением новых продуктов.
- `Задание 12.`Создать новый контроллер и шаблон для отображения страницы с подробной информацией о товаре. На этой странице должна быть показана вся информация о товаре.
- `Задание 13.`Добавить в шаблон главной страницы код для отображения списка товаров с помощью цикла. Чтобы карточки товаров выглядели одинаково, обрежьте отображаемое описание до первых 100 символов.
- `Задание 14.`Выделить общий (базовый) шаблон, который будет включать общие элементы страницы, такие как шапка, подвал и стили. Также создать подшаблон для главного меню, который можно будет включать в другие шаблоны.
- `Задание 15.`Перевести имеющиеся в проекте контроллеры с FBV на CBV.
- `Задание 16.`Создать новое приложение для блога и добавьте его в файл settings.py. Создать новую модель блоговой записи со следующими полями:заголовок, содержимое, превью (изображение), дата создания, признак публикации (булевое поле), количество просмотров. Для работы с блогом реализуйте полный CRUD для новой модели, используя CBV
- `Задание 17.`Модифицировать вывод и обработку запросов, добавив следующую логику на уровне контроллеров: Увеличение счетчика просмотров: при открытии отдельной статьи увеличивать счетчик просмотров. Фильтрация опубликованных статей: выводить в список статей только те, которые имеют положительный признак публикации. Перенаправление после редактирования: после успешного редактирования записи необходимо перенаправлять пользователя на просмотр этой статьи.
- `Задание 18.`Реализовать механизм CRUD для модели продуктов, используя модуль django.forms. При этом необходимо обезопасить сайт от спама и не разрешать присваивать продуктам названия и добавлять в описание слова, которые включены в список запрещенных слов. Реализуйте валидацию формы, чтобы проверять отсутствие этих слов (в любом регистре) в данных полях.
- `Задание 19.`Добавить кастомную валидацию для поля price в форме создания и редактирования продуктов. Валидация должна проверять, что цена продукта не может быть отрицательной. Реализовать это с использованием метода clean_price в форме. Если цена введена неправильно, отобразите соответствующее сообщение пользователю.
- `Задание 20.`Добавить стилизацию форм для продуктов, используя метод__init__. Убедитесь, что формы соответствуют общей стилистике платформы.
- `Задание 21.`Реализовать механизм, при котором пользователи могут загружать изображения продуктов. Добавить валидацию для поля загрузки изображения, чтобы проверить формат и размер загружаемого файла. Убедитесь, что загружаемые файлы имеют формат JPEG или PNG и не превышают размер 5 МБ.
- - `Задание 21.`
- `Задание 21.`
- - `Задание 21.`
- 
## Установка:
1. Клонируйте репозиторий.

 `git@github.com:MaxKuvshinov/DjangoProject.git`

2. Установите зависимости (Для установки зависимостей используется Poetry).

 `poetry install`

3. Активируйте виртуальное окружение.

 `poetry shell`

## Проект выполнил: Кувшинов Максим

