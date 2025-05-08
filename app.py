from flask import Flask, render_template, request
import os
from estimator import estimate_people_by_logic

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/estimate', methods=['POST'])
def estimate():
    container_type = request.form['container']
    food_type = request.form['food']
    image = request.files['image']

    image_path = os.path.join(app.config['UPLOAD_FOLDER'], image.filename)
    image.save(image_path)

    people = estimate_people_by_logic(container_type, food_type)

    return render_template('index.html', people=people, image_url=image_path)

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
    
