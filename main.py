import httpserver as hs
import chatbot as cb

def start_server():
    cb.chat()
    hs.run()

if __name__ == '__main__':
    start_server()