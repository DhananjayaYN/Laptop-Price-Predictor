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

