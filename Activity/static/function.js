function logout(){
    window.location="/";
return false
}

function alltestcase(){
    alert("hello");
        var form_id = document.getElementById("other_testcaseform");
        var ctdiv = document.getElementById("contentdiv");
        var di = document.getElementById("maindiv");
         var troubleshoot_table = document.createElement("table");

         var row0 = document.createElement("tr");
         var row1 = document.createElement("tr");
         var row0_td1 = document.createElement("td");
         var row1_td1 = document.createElement("td");
         var row0_inp1 = document.createElement("input")
         row0_inp1.readOnly = "True";
         row0_inp1.name="labl";
         row0_inp1.value = btn_name+"_"+opname;
         row0_inp1.style.marginLeft = "235px";
         row0_inp1.style.border= "none";
         row0_inp1.style.width= "250px";
         row0_inp1.style.background= "#ECF0D7";
         row0_inp1.style.marginTop = "20px";

         row0_td1.appendChild(row0_inp1);
         row0.appendChild(row0_td1);
         var row1_inp1 = document.createElement("textarea");
         row1_inp1.id = "textareaid";
         row1_inp1.name = "txtareanam";
         row1_inp1.rows = "5";
         row1_inp1.cols = "40";
         row1_inp1.style.marginLeft = "235px";
         row1_inp1.style.marginTop = "1px";

         var row2 = document.createElement("tr");
         var row1_td2= document.createElement("td");
         var row1_inp2 = document.createElement("input");
         row1_inp2.type= "number";
         row1_inp2.id = "effortid";
         row1_inp2.name = "effortname";
         row1_inp2.style.marginLeft = "120px";
         row1_inp2.style.height = "40px";
         row1_inp2.style.width = "140px";
         row1_inp2.placeholder = "Effort in HRS";
         row1_td1.appendChild(row1_inp1);
         row1_td2.appendChild(row1_inp2);
         row1.appendChild(row1_td1);
         row2.appendChild(row1_td2);

         troubleshoot_table.appendChild(row0);
         troubleshoot_table.appendChild(row1);
         troubleshoot_table.appendChild(row2);
         ctdiv.appendChild(troubleshoot_table);
         form_id.appendChild(ctdiv);
         di.appendChild(form_id);
  }