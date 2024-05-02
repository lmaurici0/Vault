from src.app import app

host = 'localhost'
port = 4000
debug = True

@app.route('/helloworld')
def helloworld():
    return "Hello World"
    
        

if __name__ == '__main__':
    app.run(host, port, debug)