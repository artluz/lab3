from flask import Flask, request

app = Flask(__name__)

@app.route('/sum', methods=['GET'])
def sum_numbers():
    
    a = request.args.get('a', default=0, type=int)
    b = request.args.get('b', default=0, type=int)
    
    
    result = a + b
    return f"Result: {result}!", 200

if __name__ == '__main__':
    
    app.run(host='0.0.0.0', port=5002)
