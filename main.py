import sqlite3
from interface import *

create_bills_table()

interface = GUI()
interface.geometry('1200x600')
interface.mainloop()
