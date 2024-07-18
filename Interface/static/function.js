function Clear(){
    //get the result 
    var Models = document.getElementsByName("Model_name");
    var Processors = document.getElementsByName("Processor");
    var Generations = document.getElementsByName("Generation");
    var Rams = document.getElementsByName("Ram");
    var Drive_sizes = document.getElementsByName("Hard_drive_size");
    
    // Accessing the first element in the collection
    var Model = Models[0];
    var Processor = Processors[0];
    var Generation = Generations[0];
    var Ram = Rams[0];
    var Drive_size = Drive_sizes[0];
    
    // Clear selected option    
    Model.value = "";
    Processor.value = "";
    Generation.value = "";
    Ram.value = "4GB";
    Drive_size.value = "128GB"; 

    //Clear the price value
    var result = document.getElementsByClassName('result');
    
    for (var i = 0; i < result.length; i++) {
        result[i].innerHTML = "Rs. 0.00";
    }

    //clear the radio button
    var Drive_type = document.getElementsByName('Hard_drive_type');
    
    for (var i = 0; i < Drive_type.length; i++) {
        Drive_type[i].checked = false;
    }


}


//function Submit(){
document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('form').addEventListener('submit', function(event) {
        var Models = document.getElementsByName("Model_name");
        var Processors = document.getElementsByName("Processor");
        var Generations = document.getElementsByName("Generation");

        var Model = Models[0].value;
        var Processor = Processors[0].value;
        var Generation = Generations[0].value;
    

        if ((Model == "MACBOOK") && (Processor != "APPLE")){
            event.preventDefault();
            showAlert('<h1 style="color:red">Alert</h1><hr>System can give only for,<br><br>MACBOOK  --->  APPLE  ---->  1,2<br><br> Please choose these categories for MACBOOK.');
            return 0
        }

        if((Model == "MACBOOK") && !(Generation === '1' || Generation === '2')){
            event.preventDefault();
            showAlert('<h1 style="color:red">Alert</h1><hr>System can give only for,<br><br>MACBOOK   --->   APPLE   ---->   1,2<br><br> Please choose these categories for MACBOOK.');
            return 0
        }

        if((Processor == "Ryzen5" || Processor == "Ryzen7") && (Generation == "1" ||Generation == "2" ||Generation == "10" || Generation == "11" || Generation == "12" || Generation == "13" || Generation == "14" )){
            event.preventDefault();
            showAlert('<h1 style="color:red">Alert</h1><hr>You can Only use,<br><br>Ryzen5,Ryzen7    ---->    3,4,5,6,7,8<br><br>Please choose these categories for "Ryzen" type Processors');
            return 0
        }

        if((Processor == "i3" || Processor == "i5" || Processor == "i7" || Processor == "i9") && !(Generation == "10" || Generation == "11" || Generation == "12" || Generation == "13" || Generation == "14" )){
            event.preventDefault();
            showAlert('<h1 style="color:red">Alert</h1><hr>You can Only use,<br><br>i3,i5,i7,i9    ---->    10,11,12,13,14<br><br>Please choose these categories for "i" type Processors');
            return 0
        }

    });

});

function showAlert(message) {
    const alertBox = document.getElementById('customAlert');
    const alertMessage = document.getElementById('alertMessage');
    alertMessage.innerHTML = message;
    alertBox.classList.add('show');
    document.getElementById('overlay').style.display = 'block';
}

function closeAlert() {
    const alertBox = document.getElementById('customAlert');
    alertBox.classList.remove('show');
    document.getElementById('overlay').style.display = 'none';
}

