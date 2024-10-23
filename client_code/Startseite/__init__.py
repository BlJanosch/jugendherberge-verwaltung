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
  
  
    
