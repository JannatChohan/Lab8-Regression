from task_manager import TaskManager

def test_add_task():
    tm = TaskManager()
    tm.add_task("Study")
    assert len(tm.tasks) == 1

def test_complete_task():
    tm = TaskManager()
    tm.add_task("Study")
    tm.complete_task(0)
    assert tm.tasks[0]["completed"] == True

def test_completion_rate():
    tm = TaskManager()
    tm.add_task("A")
    tm.add_task("B")
    tm.complete_task(0)
    assert tm.get_completion_rate() == 0.5
