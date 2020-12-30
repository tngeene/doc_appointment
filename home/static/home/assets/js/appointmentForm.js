const getDepartments = async () => {
  try {
    await axios.get("users/departments/").then((response) => {
      if (response.status === 200) {
        response.data.forEach((department) => {
          value = department.id;
          text = department.name;
          $("#department").append(`<option value="${value}"> 
                                       ${text} 
                                  </option>`);
        });
      }
    });
  } catch (err) {
    console.log(err);
  }
};

const getDoctors = async (department) => {
  $("#doctor")
    .find("option")
    .remove()
    .end()
    .append('<option value="">Select Doctor</option>');
  try {
    await axios
      .get(`users/doctors/?department=${department}`)
      .then((response) => {
        if (response.status === 200) {
          response.data.forEach((doctor) => {
            value = doctor.id;
            text = `${doctor.first_name} ${doctor.last_name}`;
            $("#doctor").append(`<option value="${value}"> 
                                       ${text} 
                                  </option>`);
          });
        }
      });
  } catch (err) {
    console.log(err);
  }
};

$(document).ready(function () {
  getDepartments();
  $("#department").on("change", function () {
    getDoctors(this.value);
  });
});

function formData(){
  const name = $("#name").val();
  const email = $("#email").val();
  const phone = $("#phone").val();
  const date = $("#date").val();
  const doctor = $("#doctor").val();
  const department = $("#department").val();
  const message = $("#message").val();
  return { name, email, phone, date, doctor, department, message }
}

function clearFormData(){
  $("#doctor").val('');
  $("#department").val('');
  $("#name").val('');
  $("#email").val('');
  $("#phone").val('');
  $("#date").val('');
  $("#message").val('');
}

const createAppointment = async() => {
  try {
    await axios.post('core/create-appointment/', formData()).then((response)=>{
      if(response.status === 200){
        swal({
          title: 'Appointment booked successfully',
          icon: "success",
          timer: 2000,
      });
        clearFormData()
      }
    })
  }catch(error){
    swal({
      title: 'Appointment could not be booked at this time',
      icon: "error",
      timer: 2000,
  });
  }
}
$('#appoinment-form').on('submit',function(event){
  // block form submit event
  event.preventDefault();

  // Do some stuff here
  createAppointment()

  // Continue the form submit
  // event.currentTarget.submit();
});

$('.datepicker').datetimepicker({
  format: 'DD-MM-YYYY HH:mm:ss'
});