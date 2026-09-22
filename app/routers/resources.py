from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.auth import get_current_user
from app.db import get_db
from app.models import LedgerEntry
from app.schemas import LedgerEntryIn, LedgerEntryOut

router = APIRouter(prefix="/entries", tags=["entries"])


@router.get("", response_model=list[LedgerEntryOut])
def list_items(db: Session = Depends(get_db), _: str = Depends(get_current_user)):
    return db.query(LedgerEntry).order_by(LedgerEntry.id.desc()).all()


@router.post("", response_model=LedgerEntryOut, status_code=status.HTTP_201_CREATED)
def create_item(body: LedgerEntryIn, db: Session = Depends(get_db), _: str = Depends(get_current_user)):
    row = LedgerEntry(**body.model_dump())
    db.add(row)
    db.commit()
    db.refresh(row)
    return row


@router.get("/{item_id}", response_model=LedgerEntryOut)
def get_item(item_id: int, db: Session = Depends(get_db), _: str = Depends(get_current_user)):
    row = db.get(LedgerEntry, item_id)
    if not row:
        raise HTTPException(status_code=404, detail="not found")
    return row
