## Запуск приложения

```
flask --app main.py run
```

## Postman тестирование

### Добавление нового поста

**URL:** http://127.0.0.1:5000/api/v1/post/

**Метод:** POST

**Тело запроса (JSON):**
```
{   
    "title": "Заголовок поста 1",
    "text": "Текст поста 1",
    "author_id": 1   
}
```

### Получение списка постов

**URL:** http://127.0.0.1:5000/api/v1/post/

**Метод:** GET

### Получение поста по идентификатору (ID == 1)

**URL:** http://127.0.0.1:5000/api/v1/post/1/

**Метод:** GET

### Обновление текста поста по идентификатору (ID == 1)

**URL:** http://127.0.0.1:5000/api/v1/post/1/

**Метод:** PUT

**Тело запроса (JSON):**
```
{   
    "title": "Заголовок поста 1",
    "text": "Новый текст поста 1"
}
```
### Удаление поста по идентификатору (ID == 1)

**URL:** http://127.0.0.1:5000/api/v1/post/1/

**Метод:** DELETE




