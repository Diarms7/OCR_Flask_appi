import os,cv2,pytesseract
from flask import Flask, render_template, request,jsonify
from PIL import Image
import json
import firebase_admin
import google.cloud
from firebase_admin import credentials, firestore




pytesseract.pytesseract.tesseract_cmd = "C:/Users/COMP2TECH/AppData/Local/Programs/Tesseract-OCR/tesseract.exe"

app = Flask(__name__)

UPLOAD_FOLDER = os.path.basename('.')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# initialize Firestore Database
#cred = credentials.Certificate("./etatfinancierkey.json")
#db = firebase_admin.initialize_app(cred)
#db = firestore.client()


#doc_ref = db.collection(u'users').document()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/ocr', methods=['POST','GET'])
def upload_file():
    if request.method == "GET":
        return "This is the api BLah blah"
    elif request.method == "POST":
        file = request.files['image']

        f = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)

        # add your custom code to check that the uploaded file is a valid image and not a malicious file (out-of-scope for this post)
        file.save(f)
        # print(file.filename)

        image = cv2.imread(UPLOAD_FOLDER+"/"+file.filename)
        os.remove(UPLOAD_FOLDER+"/"+file.filename)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # check to see if we should apply thresholding to preprocess the
        # image
        preprocess = request.form["preprocess"]
        if  preprocess == "thresh":
            gray = cv2.threshold(gray, 0, 255,
                                 cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

        # make a check to see if median blurring should be done to remove
        # noise

        elif preprocess == "blur":
            gray = cv2.medianBlur(gray, 3)
        print(preprocess)
        # write the grayscale image to disk as a temporary file so we can
        # apply OCR to it
        filename = "{}.png".format(os.getpid())
        cv2.imwrite(filename, gray)
        # load the image as a PIL/Pillow image, apply OCR, and then delete
        # the temporary file
        # print("C:/Users/mzm/PycharmProjects/My_website/ocr_using_video/"+filename,Image.open("C:\\Users\mzm\PycharmProjects\My_website\ocr_using_video\\"+filename))
        text = pytesseract.image_to_string(Image.open(filename))
        os.remove(filename)
        with open('Test.json', 'w', encoding='utf-8') as json_data:
            json.dump(text, json_data, indent= 14)
            #data_dict = json.load(json_data)
            #print (data_dict)
            
        #f = open('Test.json')
        #z = json.loads(f.read())
        #z['CVE_Items'][42]['cve']['description']['description_data'][0]['value']
        
        #print(json.dumps("Text in Image :\n",text))
        #doc_ref.set({u'text': z})
        return jsonify({"text" : text})
# Then query for documents
#users_ref = db.collection(u'users')

app.run('localhost',3000,threaded=True,debug=True)

