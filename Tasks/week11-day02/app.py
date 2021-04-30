from flask import Flask,render_template,request

app=Flask(__name__)

mylist=[]
@app.route('/',methods=['GET','POST'])
def index():
    if request.method=='POST':
        ad=request.form['ad']
        mylist.append(ad)
        return render_template('index.html',data=mylist)
    return render_template('index.html')


if __name__=='__main__':
    app.run(debug=True)