import unittest
from tasklist.tasks import add_task, list_tasks, complete_task


class TaskTests(unittest.TestCase):
    def test_add_trims_and_assigns_id(self):
        tasks = []
        self.assertEqual(add_task(tasks, "  Read  "),
                         {"id": 1, "title": "Read", "done": False})

    def test_blank_title_rejected(self):
        with self.assertRaises(ValueError):
            add_task([], "   ")

    def test_list_returns_copies(self):
        tasks = [{"id": 1, "title": "Read", "done": False}]
        listed = list_tasks(tasks)
        listed[0]["done"] = True
        self.assertFalse(tasks[0]["done"])

    def test_complete_marks_done(self):
        tasks = [{"id": 1, "title": "Read", "done": False}]
        self.assertTrue(complete_task(tasks, 1)["done"])
        self.assertTrue(tasks[0]["done"])

    def test_repeat_completion_is_idempotent(self):
        tasks = [{"id": 1, "title": "Read", "done": True}]
        self.assertTrue(complete_task(tasks, 1)["done"])

    def test_missing_id_rejected(self):
        with self.assertRaises(KeyError):
            complete_task([], 9)


if __name__ == "__main__":
    unittest.main()
