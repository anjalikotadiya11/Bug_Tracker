# Bug routes placeholder
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from ..models.models import Bug, User
from ..database import get_db
from ..ai.classifier import classify_bug

router = APIRouter()

class BugCreate(BaseModel):
    title: str
    description: str

@router.post("/")
def create_bug(bug: BugCreate, db: Session = Depends(get_db)):
    severity = classify_bug(bug.description)
    new_bug = Bug(title=bug.title, description=bug.description, severity=severity)
    db.add(new_bug)
    db.commit()
    db.refresh(new_bug)
    return {"msg": "Bug created", "severity": severity, "bug": new_bug.id}

@router.get("/")
def get_bugs(db: Session = Depends(get_db)):
    bugs = db.query(Bug).all()
    return bugs
