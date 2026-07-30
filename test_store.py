import inspect
from app.database.connection import store

print(inspect.signature(store.search))