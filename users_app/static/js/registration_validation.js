$().ready(function(){
    $('#registration_form').validate({
        rules:{
            client_name:{
                required:true,
                minlength:2
            },
            email:{
                required:true,
                email=true
            },
            phone_number:{
                required:true,
                minlength:10,
                number:true
            },
            client_type:"required",
            user_category:{
                required: "#client_type:2"
            },
            password:{
                required:true,
                minlength:8
            },
            confirm_password:{
                required:true,
                minlength:8,
                equalTo: "#password"
            },
            city:{
                required:true,
                minlength:4
            },
            street:{
                required:true,
                minlength:2
            },
            building_number:{
                required:true,
                minlength:1
            }
        },
        messages:{
            client_name:{
                required: "Please insert your workspace name",
                minlength: "workspace name must be 2 character at least"
            },
            email:{
                required:"Please insert your email address",
                email="a valid email address required"
            },
            phone_number:{
                required:"Please enter your phone number",
                minlength:"A valid number required",
                number:"Please enter numbers only"
            },
            client_type:"Please select your work type",
            user_category:"Please enter category type",
            password:{
                required:"Please create your password",
                minlength:"Your password must be 8 digits at least"
            },
            confirm_password:{
                required:"Please confirm your password",
                minlength:"Your cinfirmation password must be 8 digits at least",
                equalTo: "Confirmation password should equal the password"
            },
            city:{
                required:"Please enter your city",
                minlength:"There is no city less than 4 characters"
            },
            street:{
                required:"Please enter your street",
                minlength:"There is no street name less than 2 characters"
            },
            building_number:{
                required:"Please enter the number of your building",
                minlength:"Please enter your building number"
            }
        }
    });
    var client_category = $("#client_type").val();
    var initial = client_type == wholesaler;
    
});