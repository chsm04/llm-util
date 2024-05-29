# from server.api.api_service import ApiService
from flask import request, Blueprint, send_file, current_app
from util.log.log import Log
from llama.llama import LLaMa

bp = Blueprint('api_controller', __name__)

# service = ApiService()
log = Log(current_app)
llama = LLaMa()

@bp.route("/")
def hello():
    return 404

@bp.route("/api/chat", methods=['POST'])
def chat():
    current_app.logger.info("api/chat 요청")

    content = request.form['content']
    log.write_log("USER    : " + content)

    answer = llama.chat(content)
    log.write_log("SYSTEM  : " + answer)

    json = {
        "input" : content,
        "answer" : answer
    }
    return json