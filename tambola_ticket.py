from peewee import * 
from database import db

class BaseModel(Model):
    class Meta:
        database = db
        only_save_dirty = True

class TambolaTicket(BaseModel):
    id = UUIDField(constraints=[SQL("DEFAULT gen_random_uuid()")], primary_key=True)
    set_id = CharField(max_length=50,index = True)
    ticket_number = IntegerField(index = True)
    row1 = CharField(max_length=50)
    row2 = CharField(max_length=50)
    row3 = CharField(max_length=50)

    def save(self, *args, **kwargs):
        return super(TambolaTicket, self).save(*args, **kwargs)

    class Meta:
        table_name = 'tambola_ticket'
