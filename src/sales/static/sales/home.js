const url = window.location.origin;
const csrf = document.getElementsByName("csrfmiddlewaretoken")[0].value;

const reportImg = document.getElementById("report-img");
const reportBtn = document.getElementById("report-btn");

const modalBody = document.getElementById("modal-body");
let reportFormImg;
const alertBox = document.getElementById("alert-box");
const reportForm = document.getElementById("report-form");

const reportName = document.getElementById("id_name");
const reportRemarks = document.getElementById("id_remarks");

const handleAlerts = (type, msg) => {
    const wrapper = document.createElement('div')
    wrapper.innerHTML = [
        `<div class="alert alert-${type} alert-dismissible" role="alert">`,
        `   <div>${msg}</div>`,
        '   <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>',
        '</div>'
    ].join('')
    alertBox.append(wrapper)
};

if (reportImg) {
    reportBtn.classList.remove("not-visible");
}

reportBtn.addEventListener("click", () => {

    if (reportFormImg) {
        if (reportFormImg.src !== reportImg.src) {
            reportFormImg.remove()
            let reportFormImg = reportImg.cloneNode(true);
            reportFormImg.setAttribute("class", "w-100");
            modalBody.prepend(reportFormImg)
        }
    } else {
        reportFormImg = reportImg.cloneNode(true);
        reportFormImg.setAttribute("class", "w-100");
        modalBody.prepend(reportFormImg)
    }

    reportForm.addEventListener("submit", (e) => {
        e.preventDefault();
        const formData = new FormData();
        formData.append("csrfmiddlewaretoken", csrf);
        formData.append("name", reportName.value);
        formData.append("remarks", reportRemarks.value);
        formData.append("image", reportImg.src);

        $.ajax({
            type: "POST",
            url: url + "/reports/save/",
            data: formData,
            success: function (response) {
                handleAlerts("success", "Report created successfully");
                reportForm.reset();
            },
            error: function (error) {
                handleAlerts("danger", "Oops.. Something went wrong! (Note: Give a unique name.)");
            },
            processData: false,
            contentType: false,
        });
    })
})
