from flask import Blueprint
from ..controllers.server_controller import ServerController

server_bp = Blueprint('server_bp', __name__)

server_bp.route("/servers/<int:server_id>", methods = ['GET'])(ServerController.get_server)
server_bp.route("/all_servers", methods = ['GET'])(ServerController.get_servers)
# user_bp.route("/users", methods = ['POST'])(UserController.create_user)
# user_bp.route("/users/<int:user_id>", methods = ['PUT'])(UserController.update_user)