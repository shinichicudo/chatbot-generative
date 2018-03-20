import httpserver as hs
import chatbot as cb
import config_util

def start_server():
    config_util.load_config_dict()
    cb.start_chat()
    hs.run()

if __name__ == '__main__':
    start_server()