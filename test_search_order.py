# Дарья Аниськина, 29-я когорта — Финальный проект. Инженер по тестированию плюс
# Ссылка на скрин с запуском теста: https://drive.google.com/file/d/13AlfPIOy8w2fnGbNgeTZS6Fjl8coz713/view?usp=sharing
# Ссылка на скрин с заданиями по БД: https://drive.google.com/file/d/1vwmKe_tlcFyhUAWRkdIoyerD-sGa9PHm/view?usp=sharing
import pytest
import requests
import sender_stand_request
import data
import json # подключаем модуль json для работы с данными в формате JSON

def test_status_200_get_order_info():
    post_response = sender_stand_request.post_create_order(data.order_data) # Получаем ответ от запроса на создание заказа
    response_text = post_response.text # Текст ответа от сервера записываем в переменную response_text
    response_data = json.loads(response_text) # Преобразуем в Python-объект данные JSON
    track = response_data.get('track', None)  # Извлекаем номер заказа
    # track = post_response.json()['track'] # Вариант 2 - Извлекаем номер заказа из ответа с помощью метода post_response.json() и записываем в переменную track
    get_response = sender_stand_request.get_order_info(track) # Получаем ответ на запрос поиска инфо по номеру заказа
    print("\nНомер заказа:", track)  # Выводим номер для наглядности работы теста
    print("Статус ответа:", get_response.status_code)  # Выводим номер для наглядности работы теста
    assert get_response.status_code == 200, f"Статус ответа не совпадает с ожидаемым! Ожидалось: 200, получено: {get_response.status_code}" # Проверяем равен ли статус ответа 200

test_status_200_get_order_info() # Вызываем тест

