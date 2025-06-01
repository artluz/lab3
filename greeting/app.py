from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/greeting', methods=['GET'])
def greeting():
    name = request.args.get('name', 'Друг')  # По умолчанию "Друг", если имя не указано
    return Response(f"Привет, {name}!", status=200, mimetype='text/plain')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5001)
