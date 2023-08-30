from ..models.servers_models import Server
from flask import request, session

class ServerController:
  @classmethod
  def get_server(cls,server_id):
    server = Server.get_server(Server(server_id = server_id))
    return server.serialize(),200
  
  @classmethod
  def get_servers(cls):
    result = Server.get_servers()
    servers=[]
    for server in result:
      servers.append({
        "server_id" : server[0],
        "server_name" : server[1],
        "description" : server[2],
        "img_server" : server[3]
      })
    return {"Servers":servers, "total":len(servers)},200