from flask import Flask,render_template,request
import pickle

app = Flask(__name__)

def prediction_value(array_list):
    filename = 'pred_model.pickle'
    with open(filename, 'rb') as file:
        model = pickle.load(file)
    value = model.predict([array_list])
    return value

@app.route('/', methods=['POST', 'GET'])
def index():
    predictor_with_space ="0.00"
    if request.method == 'POST':  ##Collect the data from user-------------------------------
        Model = request.form['Model_name']
        Processor = request.form['Processor']
        Generation = request.form['Generation']
        Ram = request.form['Ram']
        Hard_drive_type = request.form['Hard_drive_type']
        Hard_drive_size = request.form['Hard_drive_size']

        feature_list = []  # make the arry list from user input, this list will go through the model file. 
        
        model_list = ['ACER', 'ASUS', 'DELL', 'HP', 'LENOVO', 'MACBOOK', 'MSI', 'Others']
        ram_list = ['12GB', '16GB', '32GB', '4GB', '8GB']
        gen_list = ['1', '10','11', '12', '13', '14', '2', '3', '4', '5', '6', '7', '8']
        process_list = ['Apple', 'Others', 'Ryzen5', 'Ryzen7', 'i3', 'i5', 'i7', 'i9']
        hard_type_list = ['HDD', 'SSD']
        hard_size_list = ['128GB', '1TB', '256GB', '512GB']

        def check(list, name):
            for item in list:   
                if item == name:
                    feature_list.append(1)
                else:
                    feature_list.append(0)

        check(model_list,Model) # for store the model name---------------------------------------

        check(ram_list,Ram) # for store the Ram size---------------------------------------------

        check(gen_list,Generation) # for store the Generation------------------------------------

        check(process_list,Processor) # for store the Processor ----------------------------------

        check(hard_type_list,Hard_drive_type) # for store the type of hard drive-------------------

        check(hard_size_list,Hard_drive_size) # for store the size of hard drive-------------------

        predictor = prediction_value(feature_list)
        predictor = str(predictor)
        predictor = float(predictor[1:-1])
        predictor = "{:.2f}".format(round(predictor, 2))

        part1 = predictor[:3]
        part2 = predictor[3:]
        predictor_with_space = part1 + " " + part2

        #print(feature_list)
        #print(predictor)

    return render_template('interface.html', pred = predictor_with_space)


if __name__ == '__main__':
    app.run(debug=True)