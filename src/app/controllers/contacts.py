from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from src.app.services.contacts import ContactsService
from src.app.database.models import Contact

class ContactsController:
  def __init__(self, db: AsyncSession):
    self.db = ContactsService(db)

  def create_contact(self, contact: Contact):
    return self.db.create_contact(contact)

  def get_contacts(self, skip: int = 0, limit: int = 10):
    return self.db.get_contacts(skip, limit)
  
  def get_by_id(self, id: int):
    return self.db.get_by_id(id)
  
  def update_contact(self, id: int, name: str = None, email: str = None, phone: str = None, birthdate: str = None, notes: str = None):
    contact = Contact(name=name, email=email, phone=phone, birthdate=birthdate, notes=notes)
    return self.db.update_contact(id, contact)
  
  def delete_contact(self, id: int):
    return self.db.delete_contact(id)

  