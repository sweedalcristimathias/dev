from flask import Flask,request,jsonify
import json

app=Flask(__name__)
#import json file
with open('main.json') as f:
    data=json.load(f)
#default route
@app.route('/',methods=['GET'])
def welcome():
    return 'welcome to the Crud application'

# get users
@app.route('/user',methods=['GET'])
def get_users():
    return jsonify(data['user'])

# get userbyid
@app.route('/user/<int:user_id>',methods=['GET'])
def get_user_byid(user_id):
    for users in data['user']:
        if users['id']==user_id:
            return users
    return {'error': 'user not found'} 

#create a user
@app.route('/user',methods=['POST'])
def create_user():
    new_user={'id':len(data['user'])+1,'name':request.json['name'],'email':request.json['email'],'age':request.json['age'],}
    data['user'].append(new_user)
    return new_user

#update a user
@app.route('/user/<int:user_id>',methods=['PUT'])
def update_user(user_id):
    for users in data['user']:
        if users['id']==user_id:
            users['name']=request.json['name']
            users['email']=request.json['email']
            users['age']=request.json['age']
            return users
    return {'error':'User not found'}

#delete a user
@app.route('/user/<int:user_id>',methods=['DELETE'])
def delete_user(user_id):
    for users in data['user']:
        if users['id']==user_id:
            data['user'].remove(users)
            return {'data':'User deleted successfully'}
    return {'error':'User not found'}


#run flask
if __name__=='__main__':
    app.run(debug=True)