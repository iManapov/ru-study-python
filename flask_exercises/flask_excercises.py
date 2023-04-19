from flask import Flask, request
from http import HTTPStatus


class FlaskExercise:
    """
    Вы должны создать API для обработки CRUD запросов.
    В данной задаче все пользователи хранятся в одном словаре, где ключ - это имя пользователя,
    а значение - его параметры. {"user1": {"age": 33}, "user2": {"age": 20}}
    Словарь (dict) хранить в памяти, он должен быть пустым при старте flask.

    POST /user - создание пользователя.
    В теле запроса приходит JSON в формате {"name": <имя пользователя>}.
    Ответ должен вернуться так же в JSON в формате {"data": "User <имя пользователя> is created!"}
    со статусом 201.
    Если в теле запроса не было ключа "name", то в ответ возвращается JSON
    {"errors": {"name": "This field is required"}} со статусом 422

    GET /user/<name> - чтение пользователя
    В ответе должен вернуться JSON {"data": "My name is <name>"}. Статус 200

    PATCH /user/<name> - обновление пользователя
    В теле запроса приходит JSON в формате {"name": <new_name>}.
    В ответе должен вернуться JSON {"data": "My name is <new_name>"}. Статус 200

    DELETE /user/<name> - удаление пользователя
    В ответ должен вернуться статус 204
    """

    @staticmethod
    def configure_routes(app: Flask) -> None:
        user_store: dict = {}

        @app.post("/user")
        def create_user() -> tuple[dict, HTTPStatus]:
            if request.json.get("name"):
                user_name = request.json["name"]
                user_store[user_name] = {}
                return {"data": f"User {user_name} is created!"}, HTTPStatus.CREATED
            else:
                return {
                    "errors": {"name": "This field is required"}
                }, HTTPStatus.UNPROCESSABLE_ENTITY

        @app.get("/user/<name>")
        def get_user(name: str) -> tuple[dict, HTTPStatus]:
            if name in user_store:
                return {"data": f"My name is {name}"}, HTTPStatus.OK
            else:
                return {
                    "errors": {"name": f"User with name {name} not found"}
                }, HTTPStatus.NOT_FOUND

        @app.patch("/user/<name>")
        def update_user(name: str) -> tuple[dict, HTTPStatus]:
            if request.json.get("name"):
                new_name = request.json["name"]
                user_store[new_name] = user_store.pop(name)
                return {"data": f"My name is {new_name}"}, HTTPStatus.OK
            else:
                return {
                    "errors": {"name": "This field is required"}
                }, HTTPStatus.UNPROCESSABLE_ENTITY

        @app.delete("/user/<name>")
        def delete_user(name: str) -> tuple[str, HTTPStatus]:
            user_store.pop(name)
            return "", HTTPStatus.NO_CONTENT
