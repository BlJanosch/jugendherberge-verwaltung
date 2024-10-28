from ._anvil_designer import StartseiteTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server


class Startseite(StartseiteTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
    # Any code you write here will run before the form opens.
    data = anvil.server.call("get_jugendherbergen", "name, JID")
    self.drop_down_1.items = data
    print(anvil.server.call("getdata1"))
    print("Data2")
    print(anvil.server.call("getdata2"))
    self.LoadZimmerData()
    self.LoadGaeste()
    

  def LoadZimmerData(self):
    jid = self.drop_down_1.items[self.drop_down_1.selected_value - 1][1]
    data = anvil.server.call("get_zimmer_for_jugendherberge", jid, "zimmernummer, bettenanzahl, preis_pro_nacht, gebucht")
    listfordata = []
    ZimmerNumber = []
    for item in data:
      toAdd = {'zimmerid': item[0], 'bettenanzahl': item[1], 'preis': item[2], 'status': "nicht gebucht" if item[3] == 0 else "gebucht"}
      listfordata.append(toAdd)
      if (item[3] == 0):
        ZimmerNumber.append(str(item[0]))
    self.repeating_panel_1.items = listfordata
    self.drop_down_2.items = ZimmerNumber
    
  def drop_down_1_change(self, **event_args):
    self.LoadZimmerData()
    
  def LoadGaeste(self):
    gäste = anvil.server.call("get_gast_for_jugendherberge")
    self.check_box_1.text = f"{gäste[0][2]} {gäste[0][3]}"
    self.check_box_2.text = f"{gäste[1][2]} {gäste[1][3]}"
    self.check_box_3.text = f"{gäste[2][2]} {gäste[2][3]}"

  def button_1_click(self, **event_args):
    # Befüllen der Tabelle bucht mit den Daten
    ZimmerNummer = self.drop_down_2.selected_value
    ZID = anvil.server.call("get_zimmerid", ZimmerNummer)
    OldDatum = str(self.date_picker_1.date)
    Datum = OldDatum.replace("-", ".")
    print(Datum)
    anvil.server.call("set_bucht_for_jugendherberge", 10, ZID, Datum)
    anvil.server.call('update_zimmer', ZID)
    # Befüllen der Tabelle buchtmit mit den Daten
    BID = anvil.server.call("get_bid", ZID, Datum)
    Begleiter = []
    if (self.check_box_1.checked):
      vorname, nachname = self.check_box_1.text.split(" ")
      Begleiter.append(anvil.server.call("get_gid", vorname, nachname))
    if (self.check_box_2.checked):
      vorname, nachname = self.check_box_2.text.split(" ")
      Begleiter.append(anvil.server.call("get_gid", vorname, nachname))
    if (self.check_box_3.checked):
      vorname, nachname = self.check_box_3.text.split(" ")
      Begleiter.append(anvil.server.call("get_gid", vorname, nachname))
    print(Begleiter)
    for x in Begleiter:
      anvil.server.call("set_buchmit_for_jugendherberge", BID, x)

    open_form('Gebucht')

    
