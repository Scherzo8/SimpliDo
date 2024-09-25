from sqlalchemy.orm import Session
from app.models.task import Task
from app.schemas.task import TaskCreate



def create_task(db: Session, task: TaskCreate, user_id: int) -> Task:
    """
    Create a new task in the database.

    Args:
        db (Session): SQLAlchemy session for database interaction.
        task (TaskCreate): The task data to be created.
        user_id (int): The ID of the user creating the task.

    Returns:
        Task: The created task object.
    """

    db_task = Task(**task.dict(), owner_id=user_id)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)

    return db_task


def get_tasks_by_user(db: Session, user_id: int) -> list[Task]:
    """
    Retrieve all tasks for a specific user.

    Args:
        db (Session): SQLAlchemy session for database interaction.
        user_id (int): The ID of the user.

    Returns:
        list[Task]: A list of tasks associated with the user.
    """

    return db.query(Task).filter(Task.owner == user_id).all()
    