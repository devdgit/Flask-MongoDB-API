from flask import Flask, request, jsonify
from flask_pymongo import PyMongo

app = Flask("__name__")

app.config["MONGO_DBNAME"] = "telecom"#teelecom is the database
app.config["MONGO_URI"] = "mongodb://localhost:27017/telecom"

mongo = PyMongo(app)

@app.route('/') #to check whether the application is running correctly on port
def hello_world():
    return 'flask is running correctly'

@app.route('/api/plan/create', methods=['POST']) #adding new plans
def add_item():
	bucketList = mongo.db.plan#plan is the collection name
	planname = request.json['pname']
	data = request.json['data']
	sms = request.json['psms']
	call = request.json['pcall']
	validity = request.json['pvalidity']
	price = request.json['pprice']
	p_id = bucketList.insert({'pname' : planname, 'data' : data, 'psms' : sms, 'pcall' : call, 'pvalidity' : validity, 'pprice' : price})
	new_plan = bucketList.find_one({'_id' : p_id})
	output = {'pname' : new_plan['pname'], 'data' : new_plan['data'], 'psms' : new_plan['psms'], 'pcall' : new_plan['pcall'], 'pvalidity' : new_plan['pvalidity'], 'pprice' : new_plan['pprice']}
	return jsonify({'output' : output})

@app.route('/api/plan/list_all', methods=['GET']) #retrieving all plans
def get_all_plans():
	bucketList = mongo.db.plan
	output = []
	for q in bucketList.find():
		output.append({'pname' : q['pname'], 'data' : q['data'], 'psms' : q['psms'], 'pcall' : q['pcall'], 'pvalidity' : q['pvalidity'], 'pprice' : q['pprice']})
	return jsonify({'output' : output})

@app.route('/api/plan/<string:pname>/update', methods=['PUT']) #updating a plan
def update_plan(pname):
	bucketList = mongo.db.plan
	data = raw_input('\nEnter data value to be updated:')
	sms = raw_input('\nEnter sms value to be updated:')
	call = raw_input('\nEnter pcall value to be updated:')
	validity = raw_input('\nEnter validity value to be updated:')
	price = raw_input('\nEnter price value to be updated:')
	mongo.db.plan.update_one({'pname' : pname}, {'$set' : {'data' : data, 'psms' : sms, 'pcall' : call, 'pvalidity' : validity, 'pprice' : price}})
	return jsonify({'output' : "Updated Successfully!!"})

@app.route('/api/new_user', methods=['POST']) #adding new user
def add_user():
	bucketList = mongo.db.plan
	username = request.json['uname']
	userplan = request.json['uplan']
	u_id = bucketList.insert({'uname' : username, 'uplan' : userplan})
	new_plan = bucketList.find_one({'_id' : u_id})
	output = {'uname' : new_plan['uname'], 'uplan' : new_plan['uplan']}
	return jsonify({'output' : output})

@app.route('/api/<string:uname>/<string:pname>/plan', methods=['GET']) #retrieving a user's plan
def get_a_plan(uname,pname):
	bucketList = mongo.db.plan
	q = bucketList.find_one({'pname' : pname})
	q1 = bucketList.find_one({'uname' : uname})
	if q:
		output = {'pname' : q['pname']}
	else:
		output = 'No such plan!!'
	if q1:
		output1 = {'uname' : q1['uname']}
	else:
		output1 = 'No such user!!'
	return jsonify({'output' : output , 'output1' : output1})

@app.route('/api/<string:uname>/<string:pname>/feature/limit', methods=['GET']) #retrieving a user's plan limit
def get_plan_limit(uname,pname):
	bucketList = mongo.db.plan
	q = bucketList.find_one({'pname' : pname})
	if q:
		output = {'data' : q['data'], 'psms' : q['psms'], 'pcall' : q['pcall'], 'pvalidity' : q['pvalidity']}
	else:
		output = 'No such plan!!'
	return jsonify({'output' : output})

	
if __name__ == "__main__":
    app.debug = True
app.run()
