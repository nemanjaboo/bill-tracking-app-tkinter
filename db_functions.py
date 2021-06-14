import sqlite3

def refresh_database():
    print('Radi')

def open_database():
    """Creates and connects to a database"""
    return sqlite3.connect('bills_database')

def create_bills_table():
    """Creates a table in the bills database
    with values month, bill_name, bill_cost,
    bill_status
    """
    conn = open_database()
    c = conn.cursor()
    with conn:
        try:
            c.execute("""
                CREATE TABLE bills (
                    month TEXT NOT NULL,
                    bill_name CHAR(25) NOT NULL,
                    bill_cost INT NOT NULL,
                    bill_status CHAR(10) NOT NULL
                )
            """)
        except:
            pass
    conn.commit()
    c.close()
    conn.close()

def insert_bill_to_table(bill):
    """Adds a bill to the bills table"""
    conn = open_database()
    c = conn.cursor()
    with conn:
        c.execute("""INSERT INTO bills VALUES (:month, :bill_name, :bill_cost, :bill_status)""",
                  {'month': bill.month, 'bill_name': bill.name, 'bill_cost': bill.cost, 'bill_status': bill.status})


def get_bills():
    """
    :return: list of all bills
    """
    conn = open_database()
    c = conn.cursor()
    with conn:
        c.execute("""SELECT * FROM bills""")
        return c.fetchall()


def get_bill_names():
    """
    :return: list of all bill names from the bills table
    """
    conn = open_database()
    c = conn.cursor()
    with conn:
        c.execute("""SELECT bill_name FROM bills""")
        return c.fetchall()


def get_bill_dates():
    """
    :return: list of all months from the bills table
    """
    conn = open_database()
    c = conn.cursor()
    with conn:
        c.execute("""SELECT month FROM bills""")
        return c.fetchall()


def get_paid_bills():
    """
    :return: list of all paid bills from the bills table
    """
    conn = open_database()
    c = conn.cursor()
    with conn:
        c.execute("""SELECT * FROM bills WHERE bill_status='Paid'""")
        return c.fetchall()


def get_not_paid_bills():
    """
    :return: list of all unpaid bills from the bills table
    """
    conn = open_database()
    c = conn.cursor()
    with conn:
        c.execute("""SELECT * FROM bills WHERE bill_status='Not Paid'""")
        return c.fetchall()


def get_bill_by_name(name):
    """
    :param name: name parameter string
    :return: list of all bills named as parameter
    """
    conn = open_database()
    c = conn.cursor()
    with conn:
        c.execute("""SELECT * FROM bills WHERE bill_name='{}'""".format(name))
        return c.fetchall()


def get_bill_by_month(month):
    """
    :param month: month parameter
    :return: list of all bills from the month parameter
    """
    conn = open_database()
    c = conn.cursor()
    with conn:
        c.execute("""SELECT * FROM bills""")
        all = c.fetchall()
        results = []
        for i in range(len(all)):
            if all[i][0][0:4] == month:
                results.append(all[i])
        return results


def get_bill_by_year(year):
    """
    :param year: year parameter
    :return: list of all bills from the year parameter
    """
    conn = open_database()
    c = conn.cursor()
    with conn:
        c.execute("""SELECT * FROM bills""")
        all = c.fetchall()
        results = []
        for i in range(len(all)):
            if all[i][0][-4:] == year:
                results.append(all[i])
        return results


def get_exact_bill(m, bn, bc, bst):
    """
    Function that returns exact bill from the input parameters
    :param m: month
    :param bn: bill_name
    :param bc: bill_cost
    :param bst: bill_status
    :return: bill
    """
    conn = open_database()
    c = conn.cursor()
    with conn:
        c.execute("""SELECT * FROM bills WHERE month=:month AND bill_name=:bill_name AND bill_cost=:bill_cost
         and bill_status=:bill_status""", {'month': m, 'bill_name': bn, 'bill_cost': bc, 'bill_status': bst})
        bill = c.fetchone()
        return bill


def update_bill(m, bn, bc, bst):
    """
    Function that changes unpaid bill's status to Paid
    :param m: month
    :param bn: bill_name
    :param bc: bill_cost
    :param bst: bill_status
    """
    conn = open_database()
    c = conn.cursor()
    with conn:
        c.execute("""
            UPDATE bills SET bill_status='Paid' WHERE month=:month AND bill_name=:bill_name AND bill_cost=:bill_cost AND
            bill_status ='Not Paid'
        """, {'month': m, 'bill_name': bn, 'bill_cost': bc, 'bill_status': bst})
