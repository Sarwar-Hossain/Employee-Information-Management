function showLoader() {
    document.getElementById("preloader").style.display = "block";
}

function showWarningToasty(message) {
    Toastify({
        text: message,
        duration: 4000,
        close: true,
        backgroundColor: "#0000FF",
    }).showToast();
}

function myFunc() {

    const employee_name = $("#id_employee_name").val();
    const mobile_no = $("#id_mobile_no").val();
    const date_of_service = $("#id_date_of_service").val();
    const medicaid_id = $("#id_medicaid_id").val();
    const pa_name = $("#id_pa_name").val();
    const employee_id = $("#id_employee_id").val();
    const email = $("#id_email").val();
    const password = $("#id_password").val();
    const user_role = $("#id_user_role").val();

    if (!employee_name) {
        $("#employee_name").addClass("has-danger");
        showWarningToasty('Employee field is blank!')
        return false;
    } else if (!mobile_no) {
        $("#employee_name").removeClass("has-danger")
        $("#mobile_no").addClass("has-danger");
        showWarningToasty('Mobile No field is blank!')
        return false;
    } else if (!date_of_service) {
        $("#mobile_no").removeClass("has-danger")
        $("#date_of_service").addClass("has-danger");
        showWarningToasty('Date of service field is blank!')
        return false;
    } else if (!medicaid_id) {
        $("#date_of_service").removeClass("has-danger")
        $("#medicaid_id").addClass("has-danger");
        showWarningToasty('Medicaid id field is blank!')
        return false;
    } else if (!pa_name) {
        $("#medicaid_id").removeClass("has-danger")
        $("#pa_name").addClass("has-danger");
        showWarningToasty('PA name field is blank!')
        return false;
    } else if (!employee_id) {
        $("#pa_name").removeClass("has-danger")
        $("#employee_id").addClass("has-danger");
        showWarningToasty('Employee id field is blank!')
        return false;
    } else if (!email) {
        $("#employee_id").removeClass("has-danger")
        $("#email").addClass("has-danger");
        showWarningToasty('Email field is blank!')
        return false;
    } else if (!password) {
        $("#email").removeClass("has-danger")
        $("#password").addClass("has-danger");
        showWarningToasty('Password field is blank!')
        return false;
    } else if (!user_role) {
        showWarningToasty('User Role is not selected!')
        return false;
    } else {
        showLoader();
    }
}

// Reset Form
function ClearFields() {

    document.getElementById("id_employee_name").value = "";
    document.getElementById("id_mobile_no").value = "";
    document.getElementById("id_date_of_service").value = "";
    document.getElementById("id_medicaid_id").value = "";
    document.getElementById("id_pa_name").value = "";
    document.getElementById("id_employee_id").value = "";
    document.getElementById("id_email").value = "";
    document.getElementById("id_password").value = "";
}

// Client Side form validation while submitting form

// $("#user_form").submit(function () {
//     const employee_name = $("#employee_name").val();
//
//     if (!employee_name) {
//         $("#id_employee_name").addClass("has-danger");
//         showWarningToasty('Employee Field is blank')
//         return false; // no submission
//     }
//
//     alert("Field is filled. The form will submit.");
//     return true; // form submits
// });