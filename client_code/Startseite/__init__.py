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
    data = anvil.server.call("get_jugendherbgergen", "name, JID")
    self.drop_down_1.items = data
    # item_list = []
    # for x in data:
    #   list = [x[1], x[0]]
    #   item_list.append(list)
    # self.drop_down_1.items = item_list
