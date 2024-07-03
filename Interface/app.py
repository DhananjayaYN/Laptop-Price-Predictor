from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
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


        print(feature_list)

    return render_template('interface.html')


if __name__ == '__main__':
    app.run(debug=True)