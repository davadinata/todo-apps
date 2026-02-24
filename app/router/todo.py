from sqlmodel import select, Session
from fastapi import APIRouter, status, Depends, HTTPException
from app.utils.standard_query_param import standard_query_param
from app.models.engine import get_db
from app.models.database import Todo
from app.schema.todo import TodoRequest, TodoResponse, TodoUpdateRequest
from uuid import UUID

todo_router = APIRouter(
    prefix="/todo",
    tags=   ["Todo"]
)

# Get all todo
@todo_router.get("/", response_model=list[TodoResponse])
def get_todo(param = Depends(standard_query_param), 
             db =  Depends(get_db)):
    stmt = select(Todo)
    stmt = stmt.limit(param["limit"])
    todos = db.exec(stmt).all()
    
    return todos

# Get todo by id
@todo_router.get("/{id}", response_model=TodoResponse)
def get_todo_by_id(id : UUID, db : Session = Depends(get_db)):
    todo = db.get(Todo, id)
    if not todo:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")
    
    return todo


# Create new todo
@todo_router.post("/", status_code=status.HTTP_201_CREATED, response_model=TodoResponse)
def create_todo(todo: TodoRequest,
                db : Session = Depends(get_db)
):
    try:  
        db_todo = Todo(**todo.model_dump())
        db.add(db_todo)
        db.commit()
        db.refresh(db_todo)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_CONTENT, detail=str(e))
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    return db_todo 

# Update todo
@todo_router.put("/{id}", response_model=TodoResponse)
def update_todo(id : UUID,
                todo : TodoUpdateRequest,
                db : Session  = Depends(get_db)):
    db_todo = db.get(Todo, id)
    if not db_todo:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found") 
    
    todo_data = todo.model_dump(exclude_unset=True)
    
    for key, value in todo_data.items():
        setattr(db_todo, key, value)
    try:
        db.add(db_todo)
        db.commit()
        db.refresh(db_todo)
        
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    return db_todo

# Delete todo
@todo_router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_todo(id: UUID, 
                db: Session = Depends(get_db)):
    
    db_todo = db.get(Todo, id)
    
    if not db_todo:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")
    try:
        db.delete(db_todo)
        db.commit()
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))