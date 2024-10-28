import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.files
from anvil.files import data_files
import anvil.server
import sqlite3

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
@anvil.server.callable
def get_jugendherbergen(rows="*"):
    conn = sqlite3.connect(data_files['jugendherbergen_verwaltung.db'])
    cursor = conn.cursor()
    res = list(cursor.execute(f"SELECT {rows} FROM jugendherbergen"))
    # Premium Lösung: SELECT name, LID FROM jugendherbergen
    conn.close()
    return res

@anvil.server.callable
def get_zimmer_for_jugendherberge(jid, rows="*"):
    conn = sqlite3.connect(data_files['jugendherbergen_verwaltung.db'])
    cursor = conn.cursor()
    res = list(cursor.execute(f"SELECT {rows} FROM zimmer WHERE JID = {jid}"))
    conn.close()
    return res

@anvil.server.callable
def get_gast_for_jugendherberge(rows="*"):
    conn = sqlite3.connect(data_files['jugendherbergen_verwaltung.db'])
    cursor = conn.cursor()
    res = list(cursor.execute(f"SELECT {rows} FROM gast"))
    conn.close()
    return res

@anvil.server.callable
def set_buchmit_for_jugendherberge(bid, gid):
    conn = sqlite3.connect(data_files['jugendherbergen_verwaltung.db'])
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO buchtmit (BID, GID) VALUES ({bid}, {gid})")
    conn.commit()
    conn.close()

@anvil.server.callable
def set_bucht_for_jugendherberge(gid, zid, datum):
    conn = sqlite3.connect(data_files['jugendherbergen_verwaltung.db'])
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO bucht (GID, ZID, Datum) VALUES ({gid}, {zid}, '{datum}')")
    conn.commit()
    conn.close()

@anvil.server.callable
def get_zimmerid(zimmernummer):
    conn = sqlite3.connect(data_files['jugendherbergen_verwaltung.db'])
    cursor = conn.cursor()
    res = cursor.execute(f"SELECT ZID FROM zimmer WHERE zimmernummer={zimmernummer}").fetchone()
    conn.close()
    return res[0]

@anvil.server.callable
def get_bid(zid, datum):
    conn = sqlite3.connect(data_files['jugendherbergen_verwaltung.db'])
    cursor = conn.cursor()
    res = cursor.execute(f"SELECT BID FROM bucht WHERE ZID={zid} AND Datum='{datum}'").fetchone()
    conn.close()
    return res[0]

@anvil.server.callable
def get_gid(vorname, nachname):
    conn = sqlite3.connect(data_files['jugendherbergen_verwaltung.db'])
    cursor = conn.cursor()
    res = cursor.execute(f"SELECT GID FROM gast WHERE vorname='{vorname}' AND nachname='{nachname}'").fetchone()
    conn.close()
    return res[0]

@anvil.server.callable
def update_zimmer(zid):
    conn = sqlite3.connect(data_files['jugendherbergen_verwaltung.db'])
    cursor = conn.cursor()
    cursor.execute(f"UPDATE zimmer SET gebucht=1 WHERE ZID={zid}")
    conn.commit()
    conn.close()

@anvil.server.callable
def getdata1():
    conn = sqlite3.connect(data_files['jugendherbergen_verwaltung.db'])
    cursor = conn.cursor()
    res = list(cursor.execute("select * from bucht"))
    conn.close()
    return res

@anvil.server.callable
def getdata2():
    conn = sqlite3.connect(data_files['jugendherbergen_verwaltung.db'])
    cursor = conn.cursor()
    res = list(cursor.execute("select * from buchtmit"))
    conn.close()
    return res


