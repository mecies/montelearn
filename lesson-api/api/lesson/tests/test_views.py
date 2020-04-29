import pytest

from django.urls import reverse

from .factories import LessonFactory
from .helpers import get_lesson_detail_expected_response, get_lesson_list_expected_response


@pytest.mark.django_db
def test_lesson_list_view_success(api_client):
    lessons = [LessonFactory() for _ in range(3)]

    response = api_client.get(reverse("lesson:lesson-list"))

    assert response.status_code == 200
    assert response.json() == get_lesson_list_expected_response(lessons, response)


@pytest.mark.django_db
def test_lesson_detail_view_success(api_client):
    lesson = LessonFactory()

    response = api_client.get(reverse("lesson:lesson-detail", args=[lesson.uuid]))

    assert response.status_code == 200
    assert response.json() == get_lesson_detail_expected_response(lesson)


@pytest.mark.django_db
def test_lesson_create_view_success(api_client):
    with open("api/lesson/tests/pdf_test.pdf", "rb") as pdf_file:
        data = {
            "name": "Test lesson",
            "description": "Test description",
            "pdf_file": pdf_file,
            "url": "https://some-url.com",
        }
        response = api_client.post(reverse("lesson:lesson-list"), data=data, format="multipart")

        assert response.status_code == 201
        assert response.json()["name"] == data["name"]


@pytest.mark.django_db
def test_lesson_patch_update_view_success(api_client):
    lesson = LessonFactory()

    data = {"name": "Test lesson", "url": "https://some-url.com"}
    response = api_client.patch(reverse("lesson:lesson-detail", args=[lesson.uuid]), data=data)
    assert response.status_code == 200
    assert response.json()["name"] == data["name"]


@pytest.mark.django_db
def test_lesson_put_update_view_success(api_client):
    lesson = LessonFactory()

    with open("api/lesson/tests/pdf_test.pdf", "rb") as pdf_file:
        data = {
            "name": "Test lesson new",
            "description": "New description",
            "pdf_file": pdf_file,
            "url": "https://some-url.com",
        }
        response = api_client.put(
            reverse("lesson:lesson-detail", args=[lesson.uuid]), data=data, format="multipart"
        )

        response_json = response.json()
        assert response.status_code == 200
        assert response_json["name"] == data["name"]
        assert response_json["description"] == data["description"]


@pytest.mark.django_db
def test_lesson_delete_view_success(api_client):
    lesson = LessonFactory()

    response = api_client.delete(reverse("lesson:lesson-detail", args=[lesson.uuid]))
    assert response.status_code == 204