#from tkinter import EventType
from better_profanity import profanity
from flask import Flask, jsonify
from flask import make_response, abort, request, render_template
 
from flaskext.mysql import MySQL



swearwords={'shit','bad','fack'}
profanity.censor('', censor_char='#')
app = Flask(__name__)


# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root123'
app.config['MYSQL_DATABASE_DB'] = 'usercomments'
app.config['MYSQL_DATABASE_HOST'] = '127.0.0.1'

flag = 0;
afterprocesscomment = '';
mysql = MySQL(app)

@app.route("/")
def Home():
    print("Hello")
    return render_template('index.html')


@app.route('/addcomment', methods=['POST'])
def postComment_entry():
    print("Hello")
    censored = profanity.censor(request.json['comment'])
    censored = profanity.censor(request.json['comment'], '$')
    print(censored)

    if any(word in request.json['comment'] for word in swearwords ):
        flag = True
        afterprocesscomment = censored
    else:
        flag = False

   
    afterprocesscomment = censored
    
    params = (request.json.get('userId'), request.json.get('comment'), afterprocesscomment, request.json.get('language'), flag)
    print(params)
    beforeprocesscomment = request.json.get('comment')
    print(beforeprocesscomment)
    insert_stmt = ("INSERT INTO usercomments.ucomment(userId, bpcomment, apcomment, commentlanguage, flag) "
                   "VALUES(%s, %s, %s, %s, %s)"
                   )
         
                   
    print("Hello World")
    con = mysql.connect()
    cur = con.cursor()
    cur.execute(insert_stmt, params)
    con.commit()
    try:
        cur.execute(insert_stmt, params)
        con.commit()
    except Exception as e:
    	print("there are error in inserting data into database")
        #err_str = "Problem inserting into db: " + str(e)
        #raise InvalidUsage(jsonify({'sql error': 'err_str'}), status_code=500)

    cur.close()
    con.close()

    # 201 Created
    return render_template('index1.html')
    #return make_response(jsonify({'beforeprocesscomment':beforeprocesscomment, 'afterprocesscomment':afterprocesscomment, 'flag':flag }),201)


@app.route('/getallcomments', methods=['GET'])
def get_allcomments():
    r = []
    cur = mysql.connect().cursor()
    cur.execute('''select * from usercomments.ucomment''')
    for row in cur.fetchall():
        r.append({'userId':row[0], 'bpcomment':row[1],'apcomment':row[2], 'language':row[3],'flag':row[4]})
        flag = 1
    cur.close()
    print(r)
    
    return jsonify({'comments' : r})

@app.route('/getoneusercomments/<int:userId>', methods=['GET'])
def get_oneusercomments(userId):
    r = []
    params = (userId)
    select_stmt = ("select * from usercomments.ucomment where userId = %s ")

    con = mysql.connect()
    cur = con.cursor()
  
        
    cur = mysql.connect().cursor()
    cur.execute(select_stmt, params)
    
    for row in cur.fetchall():
        r.append({'userId':row[0], 'bpcomment':row[1],'apcomment':row[2], 'language':row[3],'flag':row[4]})
        flag = 1
    cur.close()
    print(r)
    
    return jsonify({'comments' : r})
    
@app.route('/deletecomment/user/<int:userId>/comments/<int:commentId>', methods=['DELETE'])
def delete_comment(userId, commentId):
    r = []
    params = (userId, commentId)
    delete_stmt = ("delete from usercomments.ucomment where userId = %s && commentId = %s ")

    cur = mysql.connect().cursor()
    cur.execute(delete_stmt, params)
   
    cur.close()


@app.route('/updatecomment/user/<int:userId>/comments/<int:commentId>/<string:comment>', methods=['UPDATE'])
def update_comment(userId, commentId, comment):
    r = []
    params = (userId, commentId, comment)
    update_stmt = ("update from usercomments.ucomment set bpcomment = %s where userId = %s && commentId = %s ")

    cur = mysql.connect().cursor()
    cur.execute(update_stmt, params)
   
    cur.close()


    
    

if __name__ == '__main__':
    app.run( debug=True)
