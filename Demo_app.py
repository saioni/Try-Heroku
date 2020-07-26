# -*- coding: utf-8 -*-



from flask import Flask, request, render_template
app = Flask(__name__)
@app.route('/')
def index(): 
    return render_template('index.html')


@app.route('/keyword',methods=['POST','GET'])
def get_response():
    #val = request.form.get("val")
    val=request.form["keyword"]
    word=[]
    if(val=='Python'):
		word=['pandas','numpy']
    elif(val=='Data Science'):
		word=['machine learning','python']
    return render_template('index.html',prediction=word)
    


if __name__ == "__main__":
    app.run()
    
