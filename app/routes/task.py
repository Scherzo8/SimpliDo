from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.task import TaskCreate, TaskOut
from app.services.task_service import create_task, get_tasks_by_user
from app.database.db import get_db
from app.core.security import get_current_user
from app.models.user import User, Task



router = APIRouter()


@router.post("/", response_model=TaskOut)
def create_new_task(task: TaskCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)) -> TaskOut:
    """
    API endpoint to create a new task.
    
    Args:
        task (TaskCreate): The task to be created.
        db (Session): SQLAlchemy session for database interaction.
        current_user (User): The current authenticated user.
        
    Returns:
        TaskOut: The created task information.
    """

    return create_new_task(db, task, current_user.id)


@router.get("/", response_model=list[TaskOut])
def read_task(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)) -> TaskOut:
    """
    API endpoint to fetch all tasks for current user.
    
    Args:
        db (Session): SQLAlchemy session for database interaction.
        current_user (User): The currently authenticated user.
    
    Returns:
        list[TaskOut]: List of tasks for the user.
    """

    return get_tasks_by_user()


@router.put("/{task_id}", response_model=TaskOut)
def update_task(task_id: int, task: TaskCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)) -> TaskOut:
    """
    API endpoint to update an existing task.

    Args:
        task_id (int): The ID of the task to update.
        task (TaskCreate): The updated task data.
        db (Session): SQLAlchemy session for database interaction.
        current_user (User): The currently authenticated user.

    Returns:
        TaskOut: The updated task information.

    Raises:
        HTTPException: If the task does not exist or does not belong to the current user.
    """

    db_task = db.query(Task).filter(Task.id == task_id, Task.owner_id == current_user.id).first()

    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found or you don't have permission to modify this task")

    db_task.title = task.title
    db_task.description = task.description
    db_task.completed = task.completed

    db.commit()
    db.refresh(db_task)

    return db_task


@router.delete("/{task_id}", response_model=dict)
def delete_task(task_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)) -> dict:
    """
    API endpoint to delete a task.

    Args:
        task_id (int): The ID of the task to delete.
        db (Session): SQLAlchemy session for database interaction.
        current_user (User): The currently authenticated user.

    Returns:
        dict: Confirmation message.
    """

    db_task = db.query(Task).filter(Task.id == task_id, Task.owner_id == current_user.id).first()
    
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")

    db.delete(db_task)
    db.commit()
    
    return {"message": "Task deleted successfully"}