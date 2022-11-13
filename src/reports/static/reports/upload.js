const csrf = document.getElementsByName("csrfmiddlewaretoken")[0].value;
const alertBox = document.getElementById("alert-box");
const url = window.location.origin;

const handleAlerts = (type, msg) => {
    alertBox.innerHTML = `
    <div class="alert alert-${type} text-center" role="alert">
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
            if (response.loc === 1) {
                handleAlerts("danger", "File has already been uploaded!");
            } else if (response.loc === 2) {
                handleAlerts("danger", "Some other user has already uploaded the same file! (Note: Because this is a Multi-tenancy application with shared storage.)");
            } else if (response.loc === 3) {
                handleAlerts("success", "Your File has been uploaded successfully");
            }
        });
    },
    maxFiles: 3,
    maxFilesize: 3,
    acceptedFiles: ".csv",
});