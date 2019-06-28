from app import app
from flask import render_template, request
from app.models import model, formopener

name=""
gender=""
region=""

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')
    
@app.route('/results', methods = ['GET', 'POST'])
def results():
    userdata = (dict(request.form))

    print(userdata)
    global gender
    global region
    letter = userdata['letter'][0]
    gender = userdata['gender'][0]
    region = userdata['region'][0]
    names = model.get_names(gender, region)
    print(names)
    final_names=[]
    # print(names)
    for name in names:
        if name['name'][0].upper() == letter.upper():
            if name['name'] not in final_names:
                if name['gender']== gender:
                    final_names.append(name['name'])
    if len(final_names) == 0:
        return render_template('results.html', final_names=final_names, no_names=True)
    return render_template('results.html', names = names, letter = letter, final_names= final_names, gender=gender, region = region)
    
@app.route('/name-and-gif', methods = ['GET', 'POST'])
def name_and_gif():
    userdata = (dict(request.form))
    # print(userdata)    
    name = userdata['chosen_name'][0]
    gif_results = model.get_gif(name)
    # print(gif_results)
    giphy_link = gif_results[0]['images']['fixed_width']['url']
    return render_template('name-and-gif.html', data=giphy_link, name=name, gender=gender, region=region)