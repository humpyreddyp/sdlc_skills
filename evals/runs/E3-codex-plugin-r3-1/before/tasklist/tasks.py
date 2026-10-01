"""Operations on an in-memory task list."""


def add_task(tasks, title):
    title = title.strip()
    if not title:
        raise ValueError("title must not be blank")
    item = {"id": max((t["id"] for t in tasks), default=0) + 1,
            "title": title, "done": False}
    tasks.append(item)
    return item


def list_tasks(tasks):
    return [dict(t) for t in tasks]


def complete_task(tasks, task_id):
    for task in tasks:
        if task["id"] == task_id:
            task["done"] = True
            return task
    raise KeyError(task_id)
