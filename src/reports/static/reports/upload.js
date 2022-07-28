const csrf = document.getElementsByName("csrfmiddlewaretoken")[0].value;
const alertBox = document.getElementById("alert-box");
const url = window.location.origin;

const handleAlerts = (type, msg) => {
  alertBox.innerHTML = `
    <div class="alert alert-${type}" role="alert">
      ${msg}
    </div>
  `;
};

Dropzone.autoDiscover = false;
const myDropzone = new Dropzone("#my-dropzone", {
  url: url + "/reports/upload/",
  init: function () {
    this.on("sending", function (file, xhr, formData) {
      formData.append("csrfmiddlewaretoken", csrf);
    });
    this.on("success", function (file, response) {
      if (response.error) {
        handleAlerts("danger", "File already exists!");
      } else {
        handleAlerts("success", "Your File has been uploaded successfully");
      }
    });
  },
  maxFiles: 3,
  maxFilesize: 3,
  acceptedFiles: ".csv",
});