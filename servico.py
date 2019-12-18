from flask import Flask
import serial
#Realiza a leitura na porta serial
ser = serial.Serial('/dev/ttyUSB0', 9600)

app = Flask(__name__)

num = {}
while true:
   data = ser.readline(); 
        
@app.route('/', methods=['GET'])
def test():
    return 'It works!'

@app.route('/temp/<int:v1>/<int:v2>', methods=['POST'])
def temperatura(v1,v2):
   
    return jsonify(v1+v2)

#Envia os dados lidos do Arduino
@app.route('/dados', methods=['GET'])
def dados():
    #Realiza a leitura na porta serial
    #data = ser.readline();
    #data = ser.readline();
    data = data.replace("\r\n","");
    #ser.close();
    return data

@app.route('/move/<int:direcao>', methods=['POST'])
def move(direcao):
    #ser = serial.Serial('/dev/ttyUSB0', 9600)
    if direcao < 0 or direcao > 5:
        #ser.close();
        return 'Comando nao reconhecido!'
    else:
        ser.write(str(direcao));
        return 'Comando reconhecido!'
        #ser.close();
@app.route('/stop', methods=['POST'])
def stop():
   shutdown_server()
   return 'Server shutting down...'

def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()

if __name__ == '__main__':
    app.run(host='0.0.0.0')
