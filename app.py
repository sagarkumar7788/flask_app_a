from flask import Flask,render_template,request,jsonify
app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def home_page():
    return render_template("index.html")

#API using html page
@app.route("/math",methods =['POST'])
def math_operation():
    if(request.method == 'POST'):
        ops = request.form['operation']
        num1 = int(request.form['num1'])
        num2= int(request.form['num2'])
        if (ops=='add'):
            r= num1+num2
            result="The sum of  "+str(num1) + " and " + str(num2) + " is " +str(r)

        elif (ops=='subtract'):
            r= num1-num2
            result="The subtract of  "+str(num1) + " and " + str(num2) + " is " +str(r)

        elif (ops=='multiply'):
            r= num1*num2
            result="The multiply of  "+str(num1) + " and " + str(num2) + " is " +str(r)
        
        elif (ops=='divide'):
            r= num1/num2
            result="The divide of  "+str(num1) + " and " + str(num2) + " is " +str(r)

        return render_template("results.html",result=result)

#API using postman
@app.route("/postman_data",methods =['POST'])
def math_operation1():
    if(request.method == 'POST'):
        ops = request.json['operation']
        num1 = int(request.json['num1'])
        num2= int(request.json['num2'])
        if (ops=='add'):
            r= num1+num2
            result="The sum of  "+str(num1) + " and " + str(num2) + " is " +str(r)

        elif (ops=='subtract'):
            r= num1-num2
            result="The subtract of  "+str(num1) + " and " + str(num2) + " is " +str(r)

        elif (ops=='multiply'):
            r= num1*num2
            result="The multiply of  "+str(num1) + " and " + str(num2) + " is " +str(r)
        
        elif (ops=='divide'):
            r= num1/num2
            result="The divide of  "+str(num1) + " and " + str(num2) + " is " +str(r)

        return jsonify(result)



if __name__=="__main__":
    app.run(host="0.0.0.0")
