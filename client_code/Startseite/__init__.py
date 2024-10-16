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

    self.data_grid_1.columns = [
      { "id": "A", "title": "Zimmer ID", "data_key": "zimmerid" },
      { "id": "B", "title": "Bettenanzahl", "data_key": "bettenanzahl" },
      { "id": "C", "title": "Preis pro Nacht", "data_key": "preis" }
    ]
    # Any code you write here will run before the form opens.
    data = anvil.server.call("get_jugendherbergen", "name, JID")
    self.drop_down_1.items = data

    # item_list = []
    # for x in data:
    #   list = [x[1], x[0]]
    #   item_list.append(list)
    # self.drop_down_1.items = item_list

  def drop_down_1_change(self, **event_args):
    """This method is called when an item is selected"""
    jid = self.drop_down_1.items[self.drop_down_1.selected_value - 1][1]
    data = anvil.server.call("get_zimmer_for_jugendherberge", jid, "ZID, bettenanzahl, preis_pro_nacht")
    row = DataRowPanel()
    row.item = data
    self.data_grid_1.add_component(row)
    
    
