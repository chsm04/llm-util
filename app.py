from flask import Flask,request
from util.log.log import Log
from env.environment import Environment as env
# import server.api.api_controller as controller
from api import llama_controller

app = Flask(__name__)  
log = Log(app)

log.setting()

app.register_blueprint(llama_controller.bp)


if __name__ == "__main__":
    log.write_start_ascii_art()
    log.write_log(f"Address=http://{env.get_host_addr()}:{env.get_port_num()}")
    app.run(host=env.get_host_addr(), port=int(env.get_port_num()), debug=True,  use_reloader=False)
