{% extends 'base.html' %} {% block content %} {% load static %}

<style>
  .modal-lg {
    max-width: 48%;
  }
  .modal.left .modal-dialog,
  .modal.right .modal-dialog {
    position: fixed;
    margin: auto;
    width: 80%;
    height: 100%;
    -webkit-transform: translate3d(0%, 0, 0);
    -ms-transform: translate3d(0%, 0, 0);
    -o-transform: translate3d(0%, 0, 0);
    transform: translate3d(0%, 0, 0);
  }

  .modal.left .modal-content,
  .modal.right .modal-content {
    height: 100%;
    overflow-y: auto;
  }

  .modal.left .modal-body,
  .modal.right .modal-body {
    padding: 15px 15px 80px;
  }

  /*Left*/
  .modal.left.fade .modal-dialog {
    left: -320px;
    -webkit-transition: opacity 0.3s linear, left 0.3s ease-out;
    -moz-transition: opacity 0.3s linear, left 0.3s ease-out;
    -o-transition: opacity 0.3s linear, left 0.3s ease-out;
    transition: opacity 0.3s linear, left 0.3s ease-out;
  }

  .modal.left.fade.show .modal-dialog {
    left: 0;
  }

  * {
    box-sizing: border-box;
  }
  body {
    font-family: "Quicksand", sans-serif;
    height: 100%;
    margin: 0;
  }

  input[type="text"] {
    width: 100%;
    padding: 12px 20px;
    margin: 8px 0;
    display: block;
    /* border: 1.5px solid rgb(14, 12, 12); */
    border-radius: 4px;
    box-sizing: border-box;
  }

  input[type="submit"] {
    width: 40%;
    text-align: center;
    background-color: #4caf50;

    padding: 14px 20px;
    margin: 8px 0;
    border: none;
    border-radius: 4px;
    cursor: pointer;
  }

  input[type="submit"]:hover {
    background-color: #45a049;
    text-align: center;
  }

  input[type="button"]:hover {
    background-color: #45a049;
    text-align: center;
  }
  /* #viewbtn{
        margin-left:1050px;
      } */

  .inputtag {
    height: 20px;
  }
  .button {
    padding: 15px 25px;
    font-size: 12px;
    text-align: center;
    margin-left: 2em;
    cursor: pointer;
    outline: none;
    color: #fff;
    background-color: #04aa6d;
    border: none;
    border-radius: 15px;
  }

  .button:hover {
    background-color: #3e8e41;
  }

  .button:active {
    background-color: #3e8e41;
    box-shadow: 0 5px #666;
    transform: translateY(4px);
  }
</style>
<style>
  #viewbtn {
    margin-left: 1200px;
    margin-right: 10px;
  }

  /* Add Animation */
  @-webkit-keyframes animatetop {
    from {
      top: -300px;
      opacity: 0;
    }
    to {
      top: 0;
      opacity: 1;
    }
  }

  @keyframes animatetop {
    from {
      top: -300px;
      opacity: 0;
    }
    to {
      top: 0;
      opacity: 1;
    }
  }

  /* The Close Button */
  .close {
    color: white;
    float: right;
    font-size: 28px;
    font-weight: bold;
  }

  .inpt-container {
    background-image: linear-gradient(#cce3fc, #ffffff);
    border-bottom: 2px solid #b0d8f5;
    margin-bottom: 1rem;
  }

  .close:hover,
  .close:focus {
    color: #000;
    text-decoration: none;
    cursor: pointer;
  }
</style>
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <!-- <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css"> -->
  <!-- <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.4/jquery.min.js"></script> -->
  <!-- <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script> -->
  <script src="https://cdnjs.cloudflare.com/ajax/libs/jspdf/2.4.0/jspdf.umd.min.js"></script>

  <script
    src="https://cdnjs.cloudflare.com/ajax/libs/bootstrap/5.0.1/js/bootstrap.min.js"
    integrity="sha512-EKWWs1ZcA2ZY9lbLISPz8aGR2+L7JVYqBAYTq5AXgBkSjRSuQEGqWx8R1zAX16KdXPaCjOCaKE8MCpU0wcHlHA=="
    crossorigin="anonymous"
    referrerpolicy="no-referrer"
  ></script>
  <link
    rel="stylesheet"
    href="https://cdnjs.cloudflare.com/ajax/libs/bootstrap/5.0.1/css/bootstrap-grid.min.css"
    integrity="sha512-Aa+z1qgIG+Hv4H2W3EMl3btnnwTQRA47ZiSecYSkWavHUkBF2aPOIIvlvjLCsjapW1IfsGrEO3FU693ReouVTA=="
    crossorigin="anonymous"
    referrerpolicy="no-referrer"
  />

  <link
    rel="stylesheet"
    type="text/css"
    media="screen"
    href="{% static '/css/forms_common.css' %}"
  />
  <link
    rel="stylesheet"
    type="text/css"
    media="screen"
    href="{% static '/css/forms_common.css' %}"
  />
  <link
    rel="stylesheet"
    type="text/css"
    href="{% static '/css/datatables/jquery.dataTables.min.css' %}"
  />
  <script src="https://cdn.datatables.net/1.10.22/js/jquery.dataTables.min.js"></script>
  <script src="https://cdn.datatables.net/buttons/1.6.5/js/dataTables.buttons.min.js"></script>
  <script src="https://cdn.datatables.net/buttons/1.6.5/js/buttons.flash.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/jszip/3.1.3/jszip.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/pdfmake/0.1.53/pdfmake.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/pdfmake/0.1.53/vfs_fonts.js"></script>
  <script src="https://cdn.datatables.net/buttons/1.6.5/js/buttons.html5.min.js"></script>
  <script src="https://cdn.datatables.net/buttons/1.6.5/js/buttons.print.min.js"></script>
  <link
    rel="stylesheet"
    type="text/css"
    href="https://cdn.datatables.net/1.13.3/css/jquery.dataTables.min.css"
  />
  <link
    rel="stylesheet"
    type="text/css"
    href="https://cdn.datatables.net/buttons/2.3.5/css/buttons.dataTables.min.css"
  />
</head>
<style>
  table.dataTable tfoot th,
  table.dataTable tfoot td {
    /* padding: 10px 18px; */
    border-bottom: none;

  }
  .loader {
    display: none;
    position: sticky;
    left: 45%;
    top: 45%;
    border: 16px solid #f3f3f3;
    border-radius: 50%;
    border-top: 16px solid #3498db;
    width: 120px;
    height: 120px;
    z-index: 999;
    --webkit-animation: spin 2s linear infinite;
    animation: spin 2s linear infinite;
  }
  @-webkit-keyframes spin {
    0% {
      -webkit-transform: rotate(0deg);
    }
    100% {
      -webkit-transform: rotate(360deg);
    }
  }
  @keyframes spin {
    0% {
      -webkit-transform: rotate(0deg);
    }
    100% {
      -webkit-transform: rotate(360deg);
    }
  }
</style>

<h3 class="report_heading">Inspection Report Officer Wise</h3>
<div class="loader"></div>
<br/>
<div class="container">
  <div class="inpt-container" id="container1">
    <form action="{% url 'search_location' %}" method="POST" id="indexForm">
      {% csrf_token %}

      <div class="row" style="margin-left: 1em; margin-right: 5em">
        <div class="col-2 form-group">
          <label for="rly_id" class="lbl-caption">Rly./Org. Wise</label>
          <select
            class="form-control self-control"
            id="location_code"
            name="location_code"
            class="custom-select"
            data-placeholder="Rly/Org..."
            multiple
            required
          >
            <option value="" disabled hidden>All</option>
            {% for z in zone %}
            <option value="{{z}}">{{z}}</option>
            {% endfor %}
          </select>
        </div>

        <div class="col-2 form-group">
          <label for="div_id" class="lbl-caption">Div./Unit Wise</label>

          <select
            class="form-control self-control"
            id="location_type"
            name="location_type"
            class="custom-select"
            data-placeholder="Div/Unit..."
            multiple
          >
            <option value="" disabled hidden>All</option>
            {% for d in division %}
            <option value="{{d.location_code}}-{{d.location_type}}">
              {{d.location_code}}-{{d.location_type}}
            </option>

            {% endfor %}
          </select>
        </div>

        <div class="col-2 form-group" hidden>
          <label for="department_name" class="lbl-caption">Department</label>
          <select
            class="form-control sel-control"
            id="dept"
            name="dept"
            class="custom-select"
            data-placeholder="Department..."
            multiple
            hidden
          >
            <option value="" disabled hidden>select</option>
            {% for d in dept %}
            <option value="{{d}}">{{d}}</option>
            {% endfor %}
          </select>
        </div>

        <div class="col-2 form-group">
          <label for="designation" class="lbl-caption">Designation Wise</label>
          <select
            class="form-control sel-control"
            id="designation"
            name="designation"
            class="custom-select"
            multiple
            data-placeholder="Designation..."
          >
            <option value="" disabled hidden>select</option>
            {% for d in desi %}
            <option value="{{d}}">{{d}}</option>
            {% endfor %}
          </select>
        </div>

        <div class="col-2 form-group">
          <label for="date" class="lbl-caption">Date Range</label>
          <input
            class="form-control"
            id="created_on"
            name="created_on"
            value="{{new_date}}"
            autocomplete="off"
            placeholder="Select Daterange"
            style="margin-top: 0em; background-color: #fff"
            readonly
          />
        </div>

        <div class="col-2 form-group" style="margin-top: 2%">
          <input
            type="radio"
            class="form_control"
            name="data"
            id=""
            value="Issues By Officer"
            onchange="myFunction()"
          />
          <label for="data">Issues By Officer</label><br />
          <input
            type="radio"
            class="form_control"
            name="data"
            id=""
            value="Marked By Officer"
            onchange="MarkedByOfficer()"
          />
          <label for="data">Marked By Officer</label>
        </div>

        <div class="col-2">
          <div class="btn-toolbar" role="toolbar">
            <div class="btn-group" role="group">
              <!-- <button
                type="button"
                onclick="myFunction()"
                style="margin-top: 30%"
                class="btn btn-warning btn-sm"
                id="search_ob"
              >
                Continue
              </button> -->

              <a
                class="btn btn-secondary btn-sm"
                href="/NewInspectionReport/"
                style="margin-top: 15%; border-radius: 3px;"
                >Reset</a
              >

              <button type="button" id="generate_excel_btn" style="/* margin: auto; */margin-left: 10px;border-radius: 3px;margin-top: 15%;background-color: grey;border-color: gray;"  class="btn btn-primary" align="right" onclick="generate_pdf_Inspection_report();">Generate PDF</button>

            </div>
          </div>
          <br />
        </div>
      </div>
    </form>
  </div>
</div>
<br />

<!-- NAV BAR -->
<div class="container">
  <nav>
    <div class="nav nav-tabs" id="nav-tab" role="tablist">
      <a
        class="nav-link active"
        id="nav-home-tab"
        data-bs-toggle="tab"
        data-bs-target="#nav-home"
        type="button"
        role="tab"
        aria-controls="nav-home"
        aria-selected="true"
        >INSPECTION REPORT</a
      >
      <a
        class="nav-link"
        id="nav-accept-tab"
        data-bs-toggle="tab"
        data-bs-target="#nav-accept"
        type="button"
        role="tab"
        aria-controls="nav-accept"
        aria-selected="false"
        >MOM</a
      >
      <a
        class="nav-link"
        id="nav-reject-tab"
        data-bs-toggle="tab"
        data-bs-target="#nav-reject"
        type="button"
        role="tab"
        aria-controls="nav-reject"
        aria-selected="false"
        >DO</a
      >
      <a
        class="nav-link"
        id="nav-task-tab"
        data-bs-toggle="tab"
        data-bs-target="#nav-task"
        type="button"
        role="tab"
        aria-controls="nav-task"
        aria-selected="false"
        >TASKS</a
      >
    </div>
  </nav>
  <div class="tab-content" id="nav-tabContent">
    <div
      class="tab-pane fade show active"
      id="nav-home"
      role="tabpanel"
      aria-labelledby="nav-home-tab"
    >
      <br />
      <!-- inspection report -->
      <div class="row" id="1" style="overflow-x: auto">
        <form method="POST" id="indexForm">
          {% csrf_token %}
          <div id="tablediv" class="box-body no-padding">
            <table
              id="tableid"
              name="tableid"
              class="table table-entry table-bordered"
              cellspacing="0"
              style="width: 100%"
            >
              <thead
                style="
                  color: white;
                  background-color: #1e90ff;
                  text-align: left;
                "
              >
                <tr>
                  <th>Officer Desig</th>
                  <th>Created Inspection Notes</th>
                  <th>Fully Complied Inspection Notes</th>
                  <th>Pending Compliance Inspection Note</th>
                  <th>Total Inspection Points</th>
                  <th>Pending Inspection Points</th>
                  <th>Overdue Inspection Points</th>
                  <th>% complied</th>
                </tr>
              </thead>

              <tbody></tbody>
              <tfoot></tfoot>
            </table>
          </div>
          <div class="container-fluid" id="summarybuttons">
            <p class="btn btn-lg btn-primary" id="total_total_inspection">
              Total Inspection : <b>{{total_lodged_count|default:0}}</b>
            </p>
            <p class="btn btn-lg btn-primary" id="total_closed">
              Total Closed : <b>{{total_closed|default:0}}</b>
            </p>
            <p class="btn btn-lg btn-primary" id="total_total_open">
              Total Open: <b>{{total_pending|default:0}}</b>
            </p>
            <p class="btn btn-lg btn-primary" id="total_total_item">
              Total Item: <b>{{total_total_item|default:0}}</b>
            </p>
            <p class="btn btn-lg btn-primary" id="total_total_item_pending">
              Total Item Pending: <b>{{total_total_item_pending|default:0}}</b>
            </p>
            <p class="btn btn-lg btn-primary" id="total_total_item_overdue">
              Total Item Overdue: <b>{{total_pendingatudm|default:0}}</b>
            </p>
          </div>
        </form>
      </div>
    </div>
    <div
      class="tab-pane fade"
      id="nav-accept"
      role="tabpanel"
      aria-labelledby="nav-accept-tab"
    >
      <br />
      <!-- mom -->
      <div class="row" id="1" style="overflow-x: auto">
        <form method="POST" id="indexForm">
          {% csrf_token %}
          <div id="tablediv" class="box-body no-padding">
            <table
              id="momtableid"
              name="momtableid"
              class="table table-entry table-bordered"
              cellspacing="0"
              style="width: 100%"
            >
              <thead
                style="
                  color: white;
                  background-color: #1e90ff;
                  text-align: left;
                "
              >
                <tr>
                  <th>Officer Desig</th>
                  <th>MOM Created Inspection Notes</th>
                  <th>MOM Fully Complied Inspection Notes</th>
                  <th>MOM Pending Compliance Inspection Note</th>
                  <th>MOM Total Inspection Points</th>
                  <th>MOM Pending Inspection Points</th>
                  <th>MOMOverdue Inspection Points</th>
                  <th>MOM % complied</th>
                </tr>
              </thead>

              <tbody></tbody>
              <tfoot></tfoot>
            </table>
          </div>
          <div class="container-fluid" id="summarybuttons">
            <p class="btn btn-lg btn-primary" id="mom_total_total_inspection">
              Total Inspection : <b>{{total_lodged_count|default:0}}</b>
            </p>
            <p class="btn btn-lg btn-primary" id="mom_total_closed">
              Total Closed : <b>{{total_closed|default:0}}</b>
            </p>
            <p class="btn btn-lg btn-primary" id="mom_total_total_open">
              Total Open: <b>{{total_pending|default:0}}</b>
            </p>
            <p class="btn btn-lg btn-primary" id="mom_total_total_item">
              Total Item: <b>{{total_total_item|default:0}}</b>
            </p>
            <p class="btn btn-lg btn-primary" id="mom_total_total_item_pending">
              Total Item Pending: <b>{{total_total_item_pending|default:0}}</b>
            </p>
            <p class="btn btn-lg btn-primary" id="mom_total_total_item_overdue">
              Total Item Overdue: <b>{{total_pendingatudm|default:0}}</b>
            </p>
          </div>
        </form>
      </div>
    </div>
    <div
      class="tab-pane fade"
      id="nav-reject"
      role="tabpanel"
      aria-labelledby="nav-reject-tab"
    >
      <br />

      <div class="row" id="1" style="overflow-x: auto">
        <form method="POST" id="indexForm">
          {% csrf_token %}
          <div id="tablediv" class="box-body no-padding">
            <table
              id="dotableid"
              name="dotableid"
              class="table table-entry table-bordered"
              cellspacing="0"
              style="width: 100%"
            >
              <thead
                style="
                  color: white;
                  background-color: #1e90ff;
                  text-align: left;
                "
              >
                <tr>
                  <th>Officer Desig</th>
                  <th>Created DO Letters</th>
                  <th>Pending DO Letters</th>
                  <th>Completed DO Letters</th>
                  <th>% complied</th>
                </tr>
              </thead>

              <tbody></tbody>
              <tfoot></tfoot>
            </table>
          </div>
          <div class="container-fluid" id="summarybuttons">
            <p class="btn btn-lg btn-primary" id="do_total_total_open">
              Total DO Letters : <b>{{total_lodged_count|default:0}}</b>
            </p>
            <p class="btn btn-lg btn-primary" id="do_total_total_pending">
              Total DO Pending : <b>{{total_closed|default:0}}</b>
            </p>
            <p class="btn btn-lg btn-primary" id="do_total_total_closed">
              Total DO Closed: <b>{{total_pending|default:0}}</b>
            </p>
            <p class="btn btn-lg btn-primary" id="do_total_total_per_complied">
              Total % Do Complied: <b>{{total_pendingatudm|default:0}}</b>
            </p>
          </div>
        </form>
      </div>
      <br />
    </div>
    <div
      class="tab-pane fade"
      id="nav-task"
      role="tabpanel"
      aria-labelledby="nav-task-tab"
    >
      <br />

      <div class="row" id="1" style="overflow-x: auto">
        <form method="POST" id="indexForm">
          {% csrf_token %}
          <div id="tablediv" class="box-body no-padding">
            <table
              id="tasktableid"
              name="tasktableid"
              class="table table-entry table-bordered"
              cellspacing="0"
              style="width: 100%"
            >
              <thead
                style="
                  color: white;
                  background-color: #1e90ff;
                  text-align: left;
                "
              >
                <tr>
                  <th>Officer Desig</th>
                  <th>Created Task Tracker</th>
                  <th>Pending Task Tracker</th>
                  <th>Completed Task Tracker</th>
                  <th>% complied Task Tracker</th>
                </tr>
              </thead>

              <tbody></tbody>
              <tfoot></tfoot>
            </table>
          </div>
          <div class="container-fluid" id="summarybuttons">
            <p class="btn btn-lg btn-primary" id="task_total_total_open">
              Total Task Created : <b>{{total_lodged_count|default:0}}</b>
            </p>
            <p class="btn btn-lg btn-primary" id="total_total_task_assign">
              Total Task Pending: <b>{{total_closed|default:0}}</b>
            </p>
            <p class="btn btn-lg btn-primary" id="total_total_task_completed">
              Total Task Completed: <b>{{total_pending|default:0}}</b>
            </p>
            <p class="btn btn-lg btn-primary" id="task_total_total_per_complied">
              Total % Task Complied: <b>{{total_total_item|default:0}}</b>
            </p>
          </div>
        </form>
      </div>
      <br />
    </div>
  </div>
</div>
<!-- END NAV BAR -->

<div
  class="modal left fade"
  id="Search_Modal"
  tabindex="-1"
  role="dialog"
  aria-labelledby="MOM_ModalLabel"
  aria-hidden="true"
>
  <div class="modal-dialog modal-lg" role="document" style="width: 60%">
    <div class="modal-content modal-content-full-width">
      <div class="modal-body" style="text-align: left">
        <div class="row">
          <div id="preiew_mom_pdf">
            <!-- <a class="btn btn-primary" target="_blank" id="aiframetest1" style="float:right">
                    <i class="fas fa-arrow-right" aria-hidden="true"></i></a> -->

            <iframe
              id="iframepreview"
              style="width: 900px; height: 900px"
              frameborder="0"
            ></iframe>
          </div>
        </div>
      </div>
      <!--  Modal Body -->
      <div class="modal-footer modal-footer-full-width">
        <button
          type="button"
          class="btn btn-success"
          data-dismiss="modal"
          id="closereply"
        >
          Close
        </button>
      </div>
      <!-- Modal Footer-->
    </div>
  </div>
</div>

<div
  class="modal left fade"
  id="Insp_Modal"
  tabindex="-1"
  role="dialog"
  aria-labelledby="Insp_ModalLabel"
  aria-hidden="true"
>
  <div class="modal-dialog modal-lg" role="document" style="width: 60%">
    <div class="modal-content modal-content-full-width">
      <div class="modal-body" style="text-align: left">
        <div class="row">
          <div id="preiew_insp_pdf">
            <iframe
              id="iframepreviews"
              style="width: 900px; height: 900px"
              frameborder="0"
            ></iframe>
          </div>
        </div>
      </div>
      <!--  Modal Body -->
      <div class="modal-footer modal-footer-full-width">
        <button
          type="button"
          class="btn btn-success"
          data-dismiss="modal"
          id="closereply"
        >
          Close
        </button>
      </div>
      <!-- Modal Footer-->
    </div>
  </div>
</div>
<!-- Search Inss Para modal End -->

<script>

  // by shashank
  function generate_pdf_Inspection_report() {
    var location_code = $("#location_code").val();
    var location_type = $("#location_type").val();
    var designation = $("#designation").val();
    var dept = $("#dept").val();
    var created_on = $("#created_on").val();
    var status = $("#status").val();
    var query = $("#query").val();
    var selectedValue = document.querySelector('input[name="data"]:checked').value;
    console.log("$$$$$$$",selectedValue)
    console.log("location_code:", location_code);
    console.log("location_type:", location_type);
    console.log("designation:", designation);
    console.log("dept:", dept);
    console.log("created_on:", created_on);
    console.log("status:", status);
    console.log("query:", query);
    var data = {
    location_code: location_code,
    location_type: location_type,
    designation: designation,
    dept: dept,
    created_on: created_on,
    status: status,
    query: query,
    selectedValue: selectedValue
  };

  // Convert the object to a JSON string
  var jsonData = JSON.stringify(data);

    // Send the data to Django views.py using AJAX
    $.ajax({
      url: 'generate_pdf_Inspection_report/',  // Replace with your Django endpoint URL
      method: 'POST',
      data: {
        jsonData: jsonData
      },
      success: function(response) {
        // Handle the success response
        // console.log(response);
        // Create a blob from the response content
        var blob = new Blob([response], { type: 'application/pdf' });
        var url = URL.createObjectURL(blob);

        // Open the PDF in a new window or tab
        var newWindow = window.open(url, "_blank");
        newWindow.focus();
        console.log("BLOBBBBBBBBBBBBBBB!")
      },
      error: function(xhr, status, error) {
        // Handle the error response
        console.error(error);
      }
    });
  }




  $(document).ready(function () {
    $("#location_code").select2();
  });
  $(document).ready(function () {
    $("#location_type").select2();
  });
  $(document).ready(function () {
    $("#dept").select2();
  });
  $(document).ready(function () {
    $("#designation").select2();
  });
  $(document).ready(function () {
    $("#status").select2();
  });

  $(function () {
    $('input[name="created_on"]').daterangepicker({
      autoUpdateInput: false,
      autoApply: true,
      maxDate: new Date(),
      opens: "left",
      locale: {
        cancelLabel: "Clear",
      },
    });

    $('input[name="created_on"]').on(
      "apply.daterangepicker",
      function (ev, picker) {
        $(this).val(
          picker.startDate.format("DD/MM/YY") +
            " to " +
            picker.endDate.format("DD/MM/YY")
        );

        if (
          picker.startDate.format("DD/MM/YY") ==
          picker.endDate.format("DD/MM/YY")
        ) {
          $(this).val(picker.startDate.format("DD/MM/YY"));
        } else {
          $(this).val(
            picker.startDate.format("DD/MM/YY") +
              " to " +
              picker.endDate.format("DD/MM/YY")
          );
        }

        $(".applyButtonClasses").click();
      }
    );

    $('input[name="created_on"]').on(
      "cancel.daterangepicker",
      function (ev, picker) {
        $(this).val("");
      }
    );
  });

  $("#location_type").change(function () {
    var groupss = $("#location_type").val();
    data = {
      groupss: JSON.stringify(groupss),
    };
    $.ajax({
      type: "GET",
      url: "{% url 'search_desig_ajax1' %}",
      dataType: "json",
      data: data,

      success: function (response) {
        //alert("hereeee")
        console.log("0000000000", response);
        $("#designation").find("option").remove();
        $("#designation").append();
        //$("#designation").find('option').remove();
        for (i = 0; i < response.ins.length; i++) {
          $("#designation").append(
            `<option value="${response.ins[i]}">${response.ins[i]}</option>`
          );
        }
      },
    });
  });

  function location_change_add() {
    //alert('hellkkkk')
    var root = $("#location_type").val();
    data = {
      root: JSON.stringify(root),
    };
    $.ajax({
      type: "GET",
      url: "{% url 'search_des_loc_ajax' %}",
      dataType: "json",
      data: data,
      success: function (response) {
        //alert("hereeee")
        console.log("0000000000", response);
        $("#location_code").find("option").remove();
        $("#location_code").append();
        for (i in response.ins) {
          $("#location_code").append(
            `<option selected value="${response.ins[i]}">${response.ins[i]}</option>`
          );
        }
      },
    });
  }

  $("#location_code").change(function () {
    var group = $("#location_code").val();
    // alert(group)
    //alert("heree")
    data = {
      group: JSON.stringify(group),
    };
    $.ajax({
      type: "GET",
      url: "{% url 'search_locat_ajax1' %}",
      dataType: "json",
      data: data,
      success: function (response) {
        $("#location_type").select2("destroy");
        $("#designation").select2("destroy");
        $("#location_type option").remove();

        // $("#location_type").find("option").remove();

        let option = ``;
        for (i = 0; i < response.ins.length; i++) {
          option += `<option value="${response.ins[i]["location_code"]}-${response.ins[i]["location_type"]}" >${response.ins[i]["location_code"]}-${response.ins[i]["location_type"]}</option>`;
        }
        $("#location_type").append(option);

        let option1 = ``;
        $("#designation option").remove();

        for (i = 0; i < response.insdesig.length; i++) {
          option1 += `<option value="${response.insdesig[i]}">${response.insdesig[i]}</option>`;
        }
        $("#designation").append(option1);
        $("#location_type").select2();
        $("#designation").select2();
      },
    });
  });

  //show data in

  $("#tablediv").hide();
  $("#tabledivs").hide();

  var table = $("#tableid").DataTable();
  var Momtable = $("#momtableid").DataTable();
  var Dotable = $("#dotableid").DataTable();
  var Tasktable = $("#tasktableid").DataTable();

  // FNC TO FETCH DATA ON CONTINUE BUTTON
  function myFunction(){
    count = 0;
    //document.getElementById("#myFunction");
    var location_code = $("#location_code").val();
    var location_type = $("#location_type").val();
    var designation = $("#designation").val();
    var dept = $("#dept").val();
    var created_on = $("#created_on").val();
    var status = $("#status").val();
    var query = $("#query").val();
    //alert(query)

    console.log(
      location_code,
      location_type,
      designation,
      dept,
      created_on,
      status,
      query
    );
    data = {
      location_code: JSON.stringify(location_code),
      location_type: JSON.stringify(location_type),
      designation: JSON.stringify(designation),
      dept: JSON.stringify(dept),
      created_on: created_on,
    };
    $(".loader").show();
    $.ajax({
      type: "GET",
      url: "{% url 'fetch_desig_ajax_officerwise_all' %}",
      dataType: "json",
      data: data,
      //data:{location_code,location_type,designation,dept,created_on},

      success: function (response){
        table.destroy();
        Momtable.destroy();
        Dotable.destroy();
        Tasktable.destroy();
        console.log("response67788", response);
        $("#tableid tbody").empty();
        $("#tableid tfoot").empty();

        $("#momtableid tbody").empty();
        $("#momtableid tfoot").empty();

        $("#dotableid tbody").empty();
        $("#dotableid tfoot").empty();

        $("#tasktableid tbody").empty();
        $("#tasktableid tfoot").empty();

        let myhtml2 = "";
        let momhtml = "";
        let dohtml = "";
        let taskhtml = "";
        for (i = 0; i < response.rly_list.length; i++) {
          myhtml2 += "<tr>";
          myhtml2 += " <td>" + response.rly_list[i]["rly"] + "</td>";
          myhtml2 +=
            " <td>" + response.rly_list[i]["total_inspection"] + "</td>";
          myhtml2 += " <td>" + response.rly_list[i]["total_closed"] + "</td>";
          myhtml2 += " <td>" + response.rly_list[i]["total_open"] + "</td>";
          myhtml2 += " <td>" + response.rly_list[i]["total_item"] + "</td>";
          myhtml2 +=
            " <td>" + response.rly_list[i]["total_item_pending"] + "</td>";
          myhtml2 +=
            " <td>" + response.rly_list[i]["total_item_overdue"] + "</td>";
          myhtml2 +=
            " <td>" + response.rly_list[i]["per_complied"].toFixed(2) + "</td>";
          myhtml2 += "</tr>";

          // FOR MOM CREATE ROWS IN TABLE

          momhtml += "<tr>";
          momhtml += " <td>" + response.rly_list[i]["rly"] + "</td>";
          momhtml +=
            " <td>" + response.rly_list[i]["mom_total_inspection"] + "</td>";
          momhtml +=
            " <td>" + response.rly_list[i]["mom_total_closed"] + "</td>";
          momhtml += " <td>" + response.rly_list[i]["mom_total_open"] + "</td>";
          momhtml += " <td>" + response.rly_list[i]["mom_total_item"] + "</td>";
          momhtml +=
            " <td>" + response.rly_list[i]["mom_total_item_pending"] + "</td>";
          momhtml +=
            " <td>" + response.rly_list[i]["mom_total_item_overdue"] + "</td>";
          momhtml +=
            " <td>" +
            response.rly_list[i]["mom_per_complied"].toFixed(2) +
            "</td>";
          momhtml += "</tr>";

          // do letter data
          dohtml += "<tr>";
          dohtml += " <td>" + response.rly_list[i]["rly"] + "</td>";
          dohtml += " <td>" + response.rly_list[i]["do_total_open"] + "</td>";
          dohtml +=
            " <td>" + response.rly_list[i]["do_total_pending"] + "</td>";
          dohtml += " <td>" + response.rly_list[i]["do_total_closed"] + "</td>";
          dohtml +=
            " <td>" +
            response.rly_list[i]["do_per_complied"].toFixed(2) +
            "</td>";
          dohtml += "</tr>";

          // task tracker data
          taskhtml += "<tr>";
          taskhtml += " <td>" + response.rly_list[i]["rly"] + "</td>";
          taskhtml += " <td>" + response.rly_list[i]["totol_open"] + "</td>";
          taskhtml += " <td>" + response.rly_list[i]["task_assigned"] + "</td>";
          taskhtml +=
            " <td>" + response.rly_list[i]["task_completed"] + "</td>";
          taskhtml +=
            " <td>" +
            response.rly_list[i]["task_per_complied"].toFixed(2) +
            "</td>";
          taskhtml += "</tr>";
        }
        myhtml3 = "<tr>";
        myhtml3 += "<td>" + "Total" + "</td>";
        myhtml3 += "<td>" + response.total_total_inspection + "</td>";
        myhtml3 += "<td>" + response.total_total_closed + "</td>";
        myhtml3 += "<td>" + response.total_total_open + "</td>";
        myhtml3 += "<td>" + response.total_total_item + "</td>";
        myhtml3 += "<td>" + response.total_total_item_pending + "</td>";
        myhtml3 += "<td>" + response.total_total_item_overdue + "</td>";
        myhtml3 +=
          "<td>" + response.total_total_per_complied.toFixed(2) + "</td>";
        myhtml3 += "</tr>";

        mommyhtml3 = "<tr>";
        mommyhtml3 += "<td>" + "Total" + "</td>";
        mommyhtml3 += "<td>" + response.mom_total_total_inspection + "</td>";
        mommyhtml3 += "<td>" + response.mom_total_total_closed + "</td>";
        mommyhtml3 += "<td>" + response.mom_total_total_open + "</td>";
        mommyhtml3 += "<td>" + response.mom_total_total_item + "</td>";
        mommyhtml3 += "<td>" + response.mom_total_total_item_pending + "</td>";
        mommyhtml3 += "<td>" + response.mom_total_total_item_overdue + "</td>";
        mommyhtml3 +="<td>" + response.mom_total_total_per_complied.toFixed(2) + "</td>";
        mommyhtml3 += "</tr>";

        domyhtml3 = "<tr>";
        domyhtml3 += "<td>" + "Total" + "</td>";
        domyhtml3 += "<td>" + response.do_total_total_open + "</td>";
        domyhtml3 += "<td>" + response.do_total_total_pending + "</td>";
        domyhtml3 += "<td>" + response.do_total_total_closed + "</td>";
        domyhtml3 +=
          "<td>" + response.do_total_total_per_complied.toFixed(2) + "</td>";
        domyhtml3 += "</tr>";


        trackmyhtml3 = "<tr>";
        trackmyhtml3 += "<td>" + "Total" + "</td>";
        trackmyhtml3 += "<td>" + response.task_total_total_open + "</td>";
        trackmyhtml3 += "<td>" + response.total_total_task_assign + "</td>";
        trackmyhtml3 += "<td>" + response.total_total_task_completed + "</td>";
        trackmyhtml3 +=
          "<td>" + response.task_total_total_per_complied.toFixed(2) + "</td>";
        trackmyhtml3 += "</tr>";
        
        // FOOTER BUTTON DATA OF INSPECTION REPORT
        $("#total_total_inspection")
          .find("b")
          .html(response.total_total_inspection);
        $("#total_total_closed").find("b").html(response.total_total_closed);
        $("#total_total_open").find("b").html(response.total_total_open);
        $("#total_total_item").find("b").html(response.total_total_item);
        $("#total_total_item_pending")
          .find("b")
          .html(response.total_total_item_pending);
        $("#total_total_item_overdue")
          .find("b")
          .html(response.total_total_item_overdue);


        // FOOTER BUTTON DATA OF MOM REPORT
        $("#mom_total_total_inspection")
          .find("b")
          .html(response.mom_total_total_inspection);
        $("#mom_total_total_closed")
          .find("b")
          .html(response.mom_total_total_closed);
        $("#mom_total_total_open")
          .find("b")
          .html(response.mom_total_total_open);
        $("#mom_total_total_item")
          .find("b")
          .html(response.mom_total_total_item);
        $("#mom_total_total_item_pending")
          .find("b")
          .html(response.mom_total_total_item_pending);
        $("#mom_total_total_item_overdue")
          .find("b")
          .html(response.mom_total_total_item_overdue);


        // FOOTER BUTTON DATA OF DO REPORT
        $("#do_total_total_open")
          .find("b")
          .html(response.do_total_total_open);
        $("#do_total_total_pending")
          .find("b")
          .html(response.do_total_total_pending);
        $("#do_total_total_closed")
          .find("b")
          .html(response.do_total_total_closed);
        $("#do_total_total_per_complied")
          .find("b")
          .html(response.do_total_total_per_complied);


         // FOOTER BUTTON DATA OF TASK TRACKER REPORT
         $("#task_total_total_open")
          .find("b")
          .html(response.task_total_total_open);
        $("#total_total_task_assign")
          .find("b")
          .html(response.total_total_task_assign);
        $("#total_total_task_completed")
          .find("b")
          .html(response.total_total_task_completed);
        $("#task_total_total_per_complied")
          .find("b")
          .html(response.task_total_total_per_complied);


        $("#tableid tbody").append(myhtml2);
        $("#tableid tfoot").append(myhtml3);
        $("#momtableid tbody").append(momhtml);
        $("#momtableid tfoot").append(mommyhtml3);

        $("#dotableid tbody").append(dohtml);
        $("#dotableid tfoot").append(domyhtml3);

        $("#tasktableid tbody").append(taskhtml);
        $("#tasktableid tfoot").append(trackmyhtml3);

        $("#tablediv").show();
        $(".loader").hide();

        table = $("#tableid").DataTable({
          iDisplayLength: 15,
          // "ordering": false,
          order: [[1, "desc"]],
          lengthChange: true,
          lengthMenu: [15, 30, 50, 75, 100],
          dom: "Blfrtip",

          buttons: [
            {
              extend: "excel",
              title: function (e) {
                var e1 = $("#datefrom").val();
                console.log("datefrom", e1);
                var e2 = $("#dateto").val();
                var stre = "Inspection Report from " + e1 + " to " + e2;
                return stre;
              },
              // orientation: 'landscape',
              // pageSize: 'LEGAL',
            },
            {
              extend: "pdfHtml5",
              title: function (e) {
                var e1 = $("#datefrom").val();
                var e2 = $("#dateto").val();
                console.log("datefrom1", e1);
                console.log("datefrom1", datefrom);
                var stre = "Inspection Report from " + e1 + " to " + e2;
                console.log("insode inspection report", stre);
                return stre;
              },
              exportOptions: {
                alignment: "right",
              },
              customize: function (doc) {
                console.log("doc", doc);
                console.log("doc", doc.defaultStyle);
                console.log("doc2", doc.styles.tableBodyEven);
                console.log("doc3", doc.styles.tableBodyOdd);
                doc.content.splice(0, 1);

                doc.styles.tableBodyEven.alignment = "center";
                doc.styles.tableBodyOdd.alignment = "center";
              },
              text: "Pdf",
              title: "Inspection Report ",
              fontSize: "LEGAL",
            },
            {
              extend: "print",
              footer: true,
              title: function (e) {
                var s1 = $("#datefrom").val();
                var s2 = $("#dateto").val();
                let date2 = $("#created_on").val();
                var str = "Inspection Report from " + date2;
                return str;
              },
              customize: function (doc) {
                $(doc.document.body)
                  .find("tableid")
                  .css("text-align", "center");
              },
              pagingType: "simple",
              sEmptyTable: "No data available in table",

              // "bSort": true,

              oLanguage: {
                sInfoEmpty: "Page 0 of 0 ",
              },
              language: {
                info: "Page _PAGE_ of _PAGES_",
                paginate: {
                  previous: "Prev",
                },
              },
            },
          ],
        });

        Momtable = $("#momtableid").DataTable({
          iDisplayLength: 15,
          // "ordering": false,
          order: [[1, "desc"]],
          lengthChange: true,
          lengthMenu: [15, 30, 50, 75, 100],
          dom: "Blfrtip",

          buttons: [
            {
              extend: "excel",
              title: function (e) {
                var e1 = $("#datefrom").val();
                console.log("datefrom", e1);
                var e2 = $("#dateto").val();
                var stre = "Inspection Report from " + e1 + " to " + e2;
                return stre;
              },
              // orientation: 'landscape',
              // pageSize: 'LEGAL',
            },
            {
              extend: "pdfHtml5",
              title: function (e) {
                var e1 = $("#datefrom").val();
                var e2 = $("#dateto").val();
                console.log("datefrom1", e1);
                console.log("datefrom1", datefrom);
                var stre = "Inspection Report from " + e1 + " to " + e2;
                console.log("insode inspection report", stre);
                return stre;
              },
              exportOptions: {
                alignment: "right",
              },
              customize: function (doc) {
                console.log("doc", doc);
                console.log("doc", doc.defaultStyle);
                console.log("doc2", doc.styles.tableBodyEven);
                console.log("doc3", doc.styles.tableBodyOdd);
                doc.content.splice(0, 1);

                doc.styles.tableBodyEven.alignment = "center";
                doc.styles.tableBodyOdd.alignment = "center";
              },
              text: "Pdf",
              title: "Inspection Report ",
              fontSize: "LEGAL",
            },
            {
              extend: "print",
              footer: true,
              title: function (e) {
                var s1 = $("#datefrom").val();
                var s2 = $("#dateto").val();
                let date2 = $("#created_on").val();
                var str = "Inspection Report from " + date2;
                return str;
              },
              customize: function (doc) {
                $(doc.document.body)
                  .find("momtableid")
                  .css("text-align", "center");
              },
              pagingType: "simple",
              sEmptyTable: "No data available in table",

              // "bSort": true,

              oLanguage: {
                sInfoEmpty: "Page 0 of 0 ",
              },
              language: {
                info: "Page _PAGE_ of _PAGES_",
                paginate: {
                  previous: "Prev",
                },
              },
            },
          ],
        });

        Dotable = $("#dotableid").DataTable({
          iDisplayLength: 15,
          // "ordering": false,
          order: [[1, "desc"]],
          lengthChange: true,
          lengthMenu: [15, 30, 50, 75, 100],
          dom: "Blfrtip",

          buttons: [
            {
              extend: "excel",
              title: function (e) {
                var e1 = $("#datefrom").val();
                console.log("datefrom", e1);
                var e2 = $("#dateto").val();
                var stre = "Inspection Report from " + e1 + " to " + e2;
                return stre;
              },
              // orientation: 'landscape',
              // pageSize: 'LEGAL',
            },
            {
              extend: "pdfHtml5",
              title: function (e) {
                var e1 = $("#datefrom").val();
                var e2 = $("#dateto").val();
                console.log("datefrom1", e1);
                console.log("datefrom1", datefrom);
                var stre = "Inspection Report from " + e1 + " to " + e2;
                console.log("insode inspection report", stre);
                return stre;
              },
              exportOptions: {
                alignment: "right",
              },
              customize: function (doc) {
                console.log("doc", doc);
                console.log("doc", doc.defaultStyle);
                console.log("doc2", doc.styles.tableBodyEven);
                console.log("doc3", doc.styles.tableBodyOdd);
                doc.content.splice(0, 1);

                doc.styles.tableBodyEven.alignment = "center";
                doc.styles.tableBodyOdd.alignment = "center";
              },
              text: "Pdf",
              title: "Inspection Report ",
              fontSize: "LEGAL",
            },
            {
              extend: "print",
              footer: true,
              title: function (e) {
                var s1 = $("#datefrom").val();
                var s2 = $("#dateto").val();
                let date2 = $("#created_on").val();
                var str = "Inspection Report from " + date2;
                return str;
              },
              customize: function (doc) {
                $(doc.document.body)
                  .find("dotableid")
                  .css("text-align", "center");
              },
              pagingType: "simple",
              sEmptyTable: "No data available in table",

              // "bSort": true,

              oLanguage: {
                sInfoEmpty: "Page 0 of 0 ",
              },
              language: {
                info: "Page _PAGE_ of _PAGES_",
                paginate: {
                  previous: "Prev",
                },
              },
            },
          ],
        });

        Tasktable = $("#tasktableid").DataTable({
          iDisplayLength: 15,
          // "ordering": false,
          order: [[1, "desc"]],
          lengthChange: true,
          lengthMenu: [15, 30, 50, 75, 100],
          dom: "Blfrtip",

          buttons: [
            {
              extend: "excel",
              title: function (e) {
                var e1 = $("#datefrom").val();
                console.log("datefrom", e1);
                var e2 = $("#dateto").val();
                var stre = "Inspection Report from " + e1 + " to " + e2;
                return stre;
              },
              // orientation: 'landscape',
              // pageSize: 'LEGAL',
            },
            {
              extend: "pdfHtml5",
              title: function (e) {
                var e1 = $("#datefrom").val();
                var e2 = $("#dateto").val();
                console.log("datefrom1", e1);
                console.log("datefrom1", datefrom);
                var stre = "Inspection Report from " + e1 + " to " + e2;
                console.log("insode inspection report", stre);
                return stre;
              },
              exportOptions: {
                alignment: "right",
              },
              customize: function (doc) {
                console.log("doc", doc);
                console.log("doc", doc.defaultStyle);
                console.log("doc2", doc.styles.tableBodyEven);
                console.log("doc3", doc.styles.tableBodyOdd);
                doc.content.splice(0, 1);

                doc.styles.tableBodyEven.alignment = "center";
                doc.styles.tableBodyOdd.alignment = "center";
              },
              text: "Pdf",
              title: "Inspection Report ",
              fontSize: "LEGAL",
            },
            {
              extend: "print",
              footer: true,
              title: function (e) {
                var s1 = $("#datefrom").val();
                var s2 = $("#dateto").val();
                let date2 = $("#created_on").val();
                var str = "Inspection Report from " + date2;
                return str;
              },
              customize: function (doc) {
                $(doc.document.body)
                  .find("tasktableid")
                  .css("text-align", "center");
              },
              pagingType: "simple",
              sEmptyTable: "No data available in table",

              // "bSort": true,

              oLanguage: {
                sInfoEmpty: "Page 0 of 0 ",
              },
              language: {
                info: "Page _PAGE_ of _PAGES_",
                paginate: {
                  previous: "Prev",
                },
              },
            },
          ],
        });
      
      },
    });
  }
</script>

<script>
  // saud faisal

  function MarkedByOfficer() {
    let ajaxname = "MarkedByOfficer";
    count = 0;
    //document.getElementById("#myFunction");
    var location_code = $("#location_code").val();
    var location_type = $("#location_type").val();
    var designation = $("#designation").val();
    var dept = $("#dept").val();
    var created_on = $("#created_on").val();
    var status = $("#status").val();
    var query = $("#query").val();
    //alert(query)
    $(".loader").show();
    $.ajax({
      url: "{% url 'fetch_desig_ajax_officerwise_all' %}",
      method: "GET",
      dataType: "JSON",
      data: {
        ajaxname: ajaxname,
        location_code: JSON.stringify(location_code),
        location_type: JSON.stringify(location_type),
        designation: JSON.stringify(designation),
        dept: JSON.stringify(dept),
        created_on: created_on,
      },
      async: false,
      success: function (response) {
        table.destroy();
        Momtable.destroy();
        Dotable.destroy();
        Tasktable.destroy();

        // console.log("response67788", response);
        $("#tableid tbody").empty();
        $("#tableid tfoot").empty();

        $("#momtableid tbody").empty();
        $("#momtableid tfoot").empty();

        $("#dotableid tbody").empty();
        $("#dotableid tfoot").empty();

        $("#tasktableid tbody").empty();
        $("#tasktableid tfoot").empty();

        let myhtml2 = "";
        let momhtml = "";
        let dohtml = "";
        let taskhtml = "";
        for (i = 0; i < response.rly_list.length; i++) {
          myhtml2 += "<tr>";
          myhtml2 += " <td>" + response.rly_list[i]["rly"] + "</td>";
          myhtml2 +=
            " <td>" + response.rly_list[i]["total_inspection"] + "</td>";
          myhtml2 += " <td>" + response.rly_list[i]["total_closed"] + "</td>";
          myhtml2 += " <td>" + response.rly_list[i]["total_open"] + "</td>";
          myhtml2 += " <td>" + response.rly_list[i]["total_item"] + "</td>";
          myhtml2 +=
            " <td>" + response.rly_list[i]["total_item_pending"] + "</td>";
          myhtml2 +=
            " <td>" + response.rly_list[i]["total_item_overdue"] + "</td>";
          myhtml2 +=
            " <td>" + response.rly_list[i]["per_complied"].toFixed(2) + "</td>";
          myhtml2 += "</tr>";

          // FOR MOM CREATE ROWS IN TABLE

          momhtml += "<tr>";
          momhtml += " <td>" + response.rly_list[i]["rly"] + "</td>";
          momhtml +=
            " <td>" + response.rly_list[i]["mom_total_inspection"] + "</td>";
          momhtml +=
            " <td>" + response.rly_list[i]["mom_total_closed"] + "</td>";
          momhtml += " <td>" + response.rly_list[i]["mom_total_open"] + "</td>";
          momhtml += " <td>" + response.rly_list[i]["mom_total_item"] + "</td>";
          momhtml +=
            " <td>" + response.rly_list[i]["mom_total_item_pending"] + "</td>";
          momhtml +=
            " <td>" + response.rly_list[i]["mom_total_item_overdue"] + "</td>";
          momhtml +=
            " <td>" +
            response.rly_list[i]["mom_per_complied"].toFixed(2) +
            "</td>";
          momhtml += "</tr>";

          // do letter data
          dohtml += "<tr>";
          dohtml += " <td>" + response.rly_list[i]["rly"] + "</td>";
          dohtml += " <td>" + response.rly_list[i]["do_total_open"] + "</td>";
          dohtml +=
            " <td>" + response.rly_list[i]["do_total_pending"] + "</td>";
          dohtml += " <td>" + response.rly_list[i]["do_total_closed"] + "</td>";
          dohtml +=
            " <td>" +
            response.rly_list[i]["do_per_complied"].toFixed(2) +
            "</td>";
          dohtml += "</tr>";

          // task tracker data
          taskhtml += "<tr>";
          taskhtml += " <td>" + response.rly_list[i]["rly"] + "</td>";
          taskhtml += " <td>" + response.rly_list[i]["totol_open"] + "</td>";
          taskhtml += " <td>" + response.rly_list[i]["task_assigned"] + "</td>";
          taskhtml +=
            " <td>" + response.rly_list[i]["task_completed"] + "</td>";
          taskhtml +=
            " <td>" +
            response.rly_list[i]["task_per_complied"].toFixed(2) +
            "</td>";
          taskhtml += "</tr>";
        }

        mommyhtml3 = "<tr>";
        mommyhtml3 += "<td>" + "Total" + "</td>";
        mommyhtml3 += "<td>" + response.mom_total_total_inspection + "</td>";
        mommyhtml3 += "<td>" + response.mom_total_total_closed + "</td>";
        mommyhtml3 += "<td>" + response.mom_total_total_open + "</td>";
        mommyhtml3 += "<td>" + response.mom_total_total_item + "</td>";
        mommyhtml3 += "<td>" + response.mom_total_total_item_pending + "</td>";
        mommyhtml3 += "<td>" + response.mom_total_total_item_overdue + "</td>";
        mommyhtml3 +=
          "<td>" + response.mom_total_total_per_complied.toFixed(2) + "</td>";
        mommyhtml3 += "</tr>";

        myhtml3 = "<tr>";
        myhtml3 += "<td>" + "Total" + "</td>";
        myhtml3 += "<td>" + response.total_total_inspection + "</td>";
        myhtml3 += "<td>" + response.total_total_closed + "</td>";
        myhtml3 += "<td>" + response.total_total_open + "</td>";
        myhtml3 += "<td>" + response.total_total_item + "</td>";
        myhtml3 += "<td>" + response.total_total_item_pending + "</td>";
        myhtml3 += "<td>" + response.total_total_item_overdue + "</td>";
        myhtml3 +=
          "<td>" + response.total_total_per_complied.toFixed(2) + "</td>";
        myhtml3 += "</tr>";

        domyhtml3 = "<tr>";
        domyhtml3 += "<td>" + "Total" + "</td>";
        domyhtml3 += "<td>" + response.do_total_total_open + "</td>";
        domyhtml3 += "<td>" + response.do_total_total_pending + "</td>";
        domyhtml3 += "<td>" + response.do_total_total_closed + "</td>";
        domyhtml3 +="<td>" + response.do_total_total_per_complied.toFixed(2) + "</td>";
        domyhtml3 += "</tr>";

        trackmyhtml3 = "<tr>";
        trackmyhtml3 += "<td>" + "Total" + "</td>";
        trackmyhtml3 += "<td>" + response.task_total_total_open + "</td>";
        trackmyhtml3 += "<td>" + response.total_total_task_assign + "</td>";
        trackmyhtml3 += "<td>" + response.total_total_task_completed + "</td>";
        trackmyhtml3 +=
          "<td>" + response.task_total_total_per_complied.toFixed(2) + "</td>";
        trackmyhtml3 += "</tr>";

        $("#total_total_inspection")
          .find("b")
          .html(response.total_total_inspection);
        $("#total_total_closed").find("b").html(response.total_total_closed);
        $("#total_total_open").find("b").html(response.total_total_open);
        $("#total_total_item").find("b").html(response.total_total_item);
        $("#total_total_item_pending")
          .find("b")
          .html(response.total_total_item_pending);
        $("#total_total_item_overdue")
          .find("b")
          .html(response.total_total_item_overdue);

        $("#mom_total_total_inspection")
          .find("b")
          .html(response.mom_total_total_inspection);
        $("#mom_total_total_closed")
          .find("b")
          .html(response.mom_total_total_closed);
        $("#mom_total_total_open")
          .find("b")
          .html(response.mom_total_total_open);
        $("#mom_total_total_item")
          .find("b")
          .html(response.mom_total_total_item);
        $("#mom_total_total_item_pending")
          .find("b")
          .html(response.mom_total_total_item_pending);
        $("#mom_total_total_item_overdue")
          .find("b")
          .html(response.mom_total_total_item_overdue);

        $("#tableid tbody").append(myhtml2);
        $("#tableid tfoot").append(myhtml3);
 
        $("#momtableid tbody").append(momhtml);
        $("#momtableid tfoot").append(mommyhtml3);

        $("#dotableid tbody").append(dohtml);
        $("#dotableid tfoot").append(domyhtml3);

        $("#tasktableid tbody").append(taskhtml);
        $("#tasktableid tfoot").append(trackmyhtml3);

        $("#tablediv").show();
        $(".loader").hide();

        table = $("#tableid").DataTable({
          iDisplayLength: 15,
          // "ordering": false,
          order: [[1, "desc"]],
          lengthChange: true,
          lengthMenu: [15, 30, 50, 75, 100],
          dom: "Blfrtip",

          buttons: [
            {
              extend: "excel",
              title: function (e) {
                var e1 = $("#datefrom").val();
                console.log("datefrom", e1);
                var e2 = $("#dateto").val();
                var stre = "Inspection Report from " + e1 + " to " + e2;
                return stre;
              },
              // orientation: 'landscape',
              // pageSize: 'LEGAL',
            },
            {
              extend: "pdfHtml5",
              title: function (e) {
                var e1 = $("#datefrom").val();
                var e2 = $("#dateto").val();
                console.log("datefrom1", e1);
                console.log("datefrom1", datefrom);
                var stre = "Inspection Report from " + e1 + " to " + e2;
                console.log("insode inspection report", stre);
                return stre;
              },
              exportOptions: {
                alignment: "right",
              },
              customize: function (doc) {
                console.log("doc", doc);
                console.log("doc", doc.defaultStyle);
                console.log("doc2", doc.styles.tableBodyEven);
                console.log("doc3", doc.styles.tableBodyOdd);
                doc.content.splice(0, 1);

                doc.styles.tableBodyEven.alignment = "center";
                doc.styles.tableBodyOdd.alignment = "center";
              },
              text: "Pdf",
              title: "Inspection Report ",
              fontSize: "LEGAL",
            },

            {
              extend: "print",
              footer: true,
              title: function (e) {
                var s1 = $("#datefrom").val();
                var s2 = $("#dateto").val();
                let date2 = $("#created_on").val();
                var str = "Inspection Report from " + date2;
                return str;
              },
              customize: function (doc) {
                $(doc.document.body)
                  .find("tableid")
                  .css("text-align", "center");

                //  $(doc.document.body).find('table').css('border', '1px solid #000');
                //  $(doc.document.body).find('table td').css('border-left', '1px solid #000');
                //  $(doc.document.body).find('table td').css('border-top', '1px solid #000');
                //  $(doc.document.body).find('table td').css('border-right', '1px solid #000');
                //  $(doc.document.body).find('table td').css('border-bottom', '1px solid #000');
              },
              pagingType: "simple",
              sEmptyTable: "No data available in table",

              // "bSort": true,

              oLanguage: {
                sInfoEmpty: "Page 0 of 0 ",
              },
              language: {
                info: "Page _PAGE_ of _PAGES_",
                paginate: {
                  previous: "Prev",
                },
              },
            },
          ],
        });

        Momtable = $("#momtableid").DataTable({
          iDisplayLength: 15,
          // "ordering": false,
          order: [[1, "desc"]],
          lengthChange: true,
          lengthMenu: [15, 30, 50, 75, 100],
          dom: "Blfrtip",

          buttons: [
            {
              extend: "excel",
              title: function (e) {
                var e1 = $("#datefrom").val();
                console.log("datefrom", e1);
                var e2 = $("#dateto").val();
                var stre = "Inspection Report from " + e1 + " to " + e2;
                return stre;
              },
              // orientation: 'landscape',
              // pageSize: 'LEGAL',
            },
            {
              extend: "pdfHtml5",
              title: function (e) {
                var e1 = $("#datefrom").val();
                var e2 = $("#dateto").val();
                console.log("datefrom1", e1);
                console.log("datefrom1", datefrom);
                var stre = "Inspection Report from " + e1 + " to " + e2;
                console.log("insode inspection report", stre);
                return stre;
              },
              exportOptions: {
                alignment: "right",
              },
              customize: function (doc) {
                console.log("doc", doc);
                console.log("doc", doc.defaultStyle);
                console.log("doc2", doc.styles.tableBodyEven);
                console.log("doc3", doc.styles.tableBodyOdd);
                doc.content.splice(0, 1);

                doc.styles.tableBodyEven.alignment = "center";
                doc.styles.tableBodyOdd.alignment = "center";
              },
              text: "Pdf",
              title: "Inspection Report ",
              fontSize: "LEGAL",
            },
            {
              extend: "print",
              footer: true,
              title: function (e) {
                var s1 = $("#datefrom").val();
                var s2 = $("#dateto").val();
                let date2 = $("#created_on").val();
                var str = "Inspection Report from " + date2;
                return str;
              },
              customize: function (doc) {
                $(doc.document.body)
                  .find("momtableid")
                  .css("text-align", "center");

                //  $(doc.document.body).find('table').css('border', '1px solid #000');
                //  $(doc.document.body).find('table td').css('border-left', '1px solid #000');
                //  $(doc.document.body).find('table td').css('border-top', '1px solid #000');
                //  $(doc.document.body).find('table td').css('border-right', '1px solid #000');
                //  $(doc.document.body).find('table td').css('border-bottom', '1px solid #000');
              },
              pagingType: "simple",
              sEmptyTable: "No data available in table",

              // "bSort": true,

              oLanguage: {
                sInfoEmpty: "Page 0 of 0 ",
              },
              language: {
                info: "Page _PAGE_ of _PAGES_",
                paginate: {
                  previous: "Prev",
                },
              },
            },
          ],
        });
      
        Dotable = $("#dotableid").DataTable({
          iDisplayLength: 15,
          // "ordering": false,
          order: [[1, "desc"]],
          lengthChange: true,
          lengthMenu: [15, 30, 50, 75, 100],
          dom: "Blfrtip",

          buttons: [
            {
              extend: "excel",
              title: function (e) {
                var e1 = $("#datefrom").val();
                console.log("datefrom", e1);
                var e2 = $("#dateto").val();
                var stre = "Inspection Report from " + e1 + " to " + e2;
                return stre;
              },
              // orientation: 'landscape',
              // pageSize: 'LEGAL',
            },
            {
              extend: "pdfHtml5",
              title: function (e) {
                var e1 = $("#datefrom").val();
                var e2 = $("#dateto").val();
                console.log("datefrom1", e1);
                console.log("datefrom1", datefrom);
                var stre = "Inspection Report from " + e1 + " to " + e2;
                console.log("insode inspection report", stre);
                return stre;
              },
              exportOptions: {
                alignment: "right",
              },
              customize: function (doc) {
                console.log("doc", doc);
                console.log("doc", doc.defaultStyle);
                console.log("doc2", doc.styles.tableBodyEven);
                console.log("doc3", doc.styles.tableBodyOdd);
                doc.content.splice(0, 1);

                doc.styles.tableBodyEven.alignment = "center";
                doc.styles.tableBodyOdd.alignment = "center";
              },
              text: "Pdf",
              title: "Inspection Report ",
              fontSize: "LEGAL",
            },
            {
              extend: "print",
              footer: true,
              title: function (e) {
                var s1 = $("#datefrom").val();
                var s2 = $("#dateto").val();
                let date2 = $("#created_on").val();
                var str = "Inspection Report from " + date2;
                return str;
              },
              customize: function (doc) {
                $(doc.document.body)
                  .find("dotableid")
                  .css("text-align", "center");
              },
              pagingType: "simple",
              sEmptyTable: "No data available in table",

              // "bSort": true,

              oLanguage: {
                sInfoEmpty: "Page 0 of 0 ",
              },
              language: {
                info: "Page _PAGE_ of _PAGES_",
                paginate: {
                  previous: "Prev",
                },
              },
            },
          ],
        });
      
        Tasktable = $("#tasktableid").DataTable({
          iDisplayLength: 15,
          // "ordering": false,
          order: [[1, "desc"]],
          lengthChange: true,
          lengthMenu: [15, 30, 50, 75, 100],
          dom: "Blfrtip",

          buttons: [
            {
              extend: "excel",
              title: function (e) {
                var e1 = $("#datefrom").val();
                console.log("datefrom", e1);
                var e2 = $("#dateto").val();
                var stre = "Inspection Report from " + e1 + " to " + e2;
                return stre;
              },
              // orientation: 'landscape',
              // pageSize: 'LEGAL',
            },
            {
              extend: "pdfHtml5",
              title: function (e) {
                var e1 = $("#datefrom").val();
                var e2 = $("#dateto").val();
                console.log("datefrom1", e1);
                console.log("datefrom1", datefrom);
                var stre = "Inspection Report from " + e1 + " to " + e2;
                console.log("insode inspection report", stre);
                return stre;
              },
              exportOptions: {
                alignment: "right",
              },
              customize: function (doc) {
                console.log("doc", doc);
                console.log("doc", doc.defaultStyle);
                console.log("doc2", doc.styles.tableBodyEven);
                console.log("doc3", doc.styles.tableBodyOdd);
                doc.content.splice(0, 1);

                doc.styles.tableBodyEven.alignment = "center";
                doc.styles.tableBodyOdd.alignment = "center";
              },
              text: "Pdf",
              title: "Inspection Report ",
              fontSize: "LEGAL",
            },
            {
              extend: "print",
              footer: true,
              title: function (e) {
                var s1 = $("#datefrom").val();
                var s2 = $("#dateto").val();
                let date2 = $("#created_on").val();
                var str = "Inspection Report from " + date2;
                return str;
              },
              customize: function (doc) {
                $(doc.document.body)
                  .find("tasktableid")
                  .css("text-align", "center");
              },
              pagingType: "simple",
              sEmptyTable: "No data available in table",

              // "bSort": true,

              oLanguage: {
                sInfoEmpty: "Page 0 of 0 ",
              },
              language: {
                info: "Page _PAGE_ of _PAGES_",
                paginate: {
                  previous: "Prev",
                },
              },
            },
          ],
        });
      
      },
    });
  }
</script>

{% endblock %}
