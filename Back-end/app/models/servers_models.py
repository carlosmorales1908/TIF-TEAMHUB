from ..database import DatabaseConnection

class Server:
  def __init__(self, **kwargs):
      self.server_id = kwargs.get('server_id')
      self.server_name = kwargs.get('server_name')
      self.description = kwargs.get('description')
      self.img_server = kwargs.get('img_server')

  def serialize(self):
    return {
      "server_id": self.server_id,
      "server_name": self.server_name,
      "description": self.description,
      "img_server": self.img_server,
    }
  
  @classmethod
  def get_server(cls, server):
    """
    """
    query = """SELECT * FROM servers 
    WHERE server_id = %(server_id)s"""
    params = server.__dict__
    result = DatabaseConnection.fetch_one(query, params=params)

    if result is not None:
      return cls(
        server_id = result[0],
        server_name = result[1],
        description = result[2],
        img_server = result[3]
      )
    return None
  
  @classmethod
  def get_servers(cls):
    sql = "SELECT * FROM servers;"
    result = DatabaseConnection.fetch_all(sql)
    if result is not None:
      return result
    else:
      return None