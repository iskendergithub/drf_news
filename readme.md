## drf_news
Project name endpoints:

###  Получения списка новостей по методу GET --> http://pw2222.pythonanywhere.com/news/

 {
        "id": 7,
        "title": "updated",
        "description": "today",
        "date": "2022-10-14T04:32:43.079788Z",
        "published": true
    }

###  Создаем новости (create) по методу POST --> http://pw2222.pythonanywhere.com/news-create/

[
    "Created: News is created !"
]

###  Обновление новостей (update) по методу POST --> http://pw2222.pythonanywhere.com/news-update/
{
    "id": 7,
    "title": "updated second time",
    "description": "today",
    "date": "2022-10-14T04:32:43.079788Z",
    "published": true
}
###  удаление новостей (delete) по методу DELETE --> http://pw2222.pythonanywhere.com/news-delete/

{
    "info": "News was deleted"
}
