from peewee import *

#database = MySQLDatabase('today_if_ua', **{'password': 'root', 'user': 'root'})
#database = PostgresqlDatabase('today', user='madao')

database = PostgresqlDatabase('today', **{'password': 'u7VRZJnyzJw7FsTHMe', 'user': 'madao', 'host':'localhost'})
class BaseModel(Model):
    class Meta:
        database = database


class CoreGategories(BaseModel):
    icon = CharField()
    slug = CharField(unique=True)
    title = CharField()

    class Meta:
        db_table = 'core_gategories'

# class CoreEvent(BaseModel):
#     category = ForeignKeyField(db_column='category_id', null=True, rel_model=CoreGategories, to_field='id')
#     contact_number = CharField()
#     description = TextField(null=True)
#     event_day = DateField(null=True)
#     event_time = TimeField(null=True)
#     latitude = CharField()
#     location = CharField()
#     longitude = CharField()
#     photo = CharField(null=True)
#     price = CharField()
#     publish = DateField()
#     slug = CharField(unique=True)
#     source = CharField()
#     source_href = CharField()
#     status = CharField()
#     ticket = CharField()
#     title = CharField()

#     class Meta:
#         db_table = 'core_event'

class CoreEvent(BaseModel):
    category = ForeignKeyField(db_column='category_id', null=True, rel_model=CoreGategories, to_field='id')
    contact_number = CharField()
    description = TextField(null=True)
    event_day = DateField(null=True)
    event_time = TimeField(null=True)
    latitude = CharField()
    location = CharField()
    location_false = CharField(null=True)
    longitude = CharField()
    photo = CharField(null=True)
    price = CharField()
    publish = DateField()
    slug = CharField(unique=True)
    source = CharField()
    source_href = CharField()
    status = CharField()
    ticket = CharField()
    title = CharField()
    vk_href=CharField()
    fb_href =CharField()

    class Meta:
        db_table = 'core_event'