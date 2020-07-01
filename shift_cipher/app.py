from flask import request
from flask_api import FlaskAPI, exceptions
from ShiftCipher import ShiftCipher

app = FlaskAPI(__name__)

def get_message (json):
    message = json.get('Message')
    if message == None or type(message) != str:
        raise exceptions.ParseError("Message string must be provided") # HTTP status 400
    return message

def get_shift (json):
    shift = json.get('Shift')
    if shift != None:
        try:
            shift = int(shift)
            return shift
        except:
            raise exceptions.ParseError("Illegal Shift amount: must provide integer")
    raise exceptions.ParseError("Missing Shift amount") # HTTP status 400


def save_to_file (message):
    f = open('messages.txt', 'a')
    f.write(message + '\n')
    f.close()

@app.route('/api/encode', methods=['POST'])
def encrypt():
    try:
        json = request.get_json(force=True)

    except:
        raise exceptions.ParseError("Malformed JSON request") # HTTP status 400

    message = get_message(json)
    shift = get_shift(json)
    cipher = ShiftCipher(shift)
    try:
        encoded_msg = cipher.encode(message)
        save_to_file(message)
        return {'EncodedMessage': encoded_msg} # HTTP status 200
    except:
        raise exceptions.APIException("Internal Error: Cipher could not encrypt") # HTTP status 500






