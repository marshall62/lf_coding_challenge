**REST API for Shift Cipher**


POST http://localhost:23456/api/encode
Send a JSON of the form
{"Message": String, "Shift": Integer}

Applies Caesar cipher to the message and shifts it by the number positions to the right.

Cipher will wrap lower case letter within the lower case alphabet and
will wrap upper case letters within upper case alphabet.  All other characters
are left intact.

_Server keeps track of all messages it has encrypted in messages.txt file._
 
**Example:**

 

 
 `curl -X POST --header "Content-Type: application/json" \
   --data '{"Message":"String of text to encrypt","Shift": 4}' \
   http://localhost:23456/api/encode`
   
 Returns JSON of form:
  
` {
     "EncodedMessage": "Wxvmrk sj xibx xs irgvctx"
 }`
 
 
 
Built in Intellij/PyCharm IDE 
 
**How to run server:**

Requirements: 

_Python 3.6 or above_

verify you are running it either
python --version
or 
python3 --version

Clone repo to a directory <my-dir>

`cd <my-dir>`

`python3 -m venv venv`

`source venv/bin/activate`

`pip install -r requirements.txt`

`flask run --port 23456`


