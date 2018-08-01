from app import create_app

app=create_app('testing')#development

if __name__=='__main__':
    app.run(debug=True,port=6002)