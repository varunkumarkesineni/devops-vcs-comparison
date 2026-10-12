import unittest

import taskmanager as tm


class TaskManagerTests(unittest.TestCase):
    def test_add_task(self):
        tasks = []
        task = tm.add_task(tasks, "Write report")
        self.assertEqual(task["id"], 1)
        self.assertFalse(task["done"])

    def test_add_empty_title_fails(self):
        with self.assertRaises(ValueError):
            tm.add_task([], "   ")

    def test_complete_task(self):
        tasks = []
        tm.add_task(tasks, "Push code")
        tm.complete_task(tasks, 1)
        self.assertTrue(tasks[0]["done"])

    def test_complete_missing_task(self):
        with self.assertRaises(KeyError):
            tm.complete_task([], 99)

    def test_list_pending(self):
        tasks = []
        tm.add_task(tasks, "A")
        tm.add_task(tasks, "B")
        tm.complete_task(tasks, 1)
        self.assertEqual(len(tm.list_tasks(tasks, only_pending=True)), 1)


if __name__ == "__main__":
    unittest.main()
