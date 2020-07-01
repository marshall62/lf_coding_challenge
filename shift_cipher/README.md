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

_Requirements:_ 

--Python 3.6 or above

--Verify Python version:

`python --version`
OR
`python3 --version`

--You have cloned lf_coding_challenge
 
Execute these commands in your Terminal/Shell

`cd lf_coding_challenge/shift_cipher`

`python3 -m venv venv`

`source venv/bin/activate` (Mac OS/Linux)
`.venv/Scripts/activate` (Windows)

`pip install -r requirements.txt`

`flask run --port 23456 &`

Server is now running:

**Test:**

`curl -X POST --header "Content-Type: application/json" --data '{"Message":"The quick red fox jumped over the lazy brown dog and charged him $123.03!","Shift": 4}' http://localhost:23456/api/encode
`

CTRL-C to kill server

Finally: Type "deactivate" to exit virtual environment

