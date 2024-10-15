import pytest
from tasks import add_task, remove_task, list_tasks


def test_add_task():
    # Test adding a valid task
    assert add_task("Write tests") == "Task 'Write tests' added."
    assert "Write tests" in list_tasks()

    # Test adding an empty task
    assert add_task("") == "Cannot add an empty task."
    assert "" not in list_tasks()


def test_remove_task():
    # Add a task to remove
    add_task("Go jogging")
    assert "Go jogging" in list_tasks()

    # Test removing an existing task
    assert remove_task("Go jogging") == "Task 'Go jogging' removed."
    assert "Go jogging" not in list_tasks()

    # Test removing a non-existing task
    assert remove_task("Non-existing task") == "Task not found."


def test_list_tasks():
    # Clear tasks and add new ones
    tasks = list_tasks()
    tasks.clear()
    add_task("Task 1")
    add_task("Task 2")

    # Test listing tasks
    assert list_tasks() == ["Task 1", "Task 2"]

    # Test listing tasks when empty
    tasks.clear()
    assert list_tasks() == []
