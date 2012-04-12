//Step 3, use javascript to take take input from table(made from list.xml) and parse to php form
//Khan table generator.
//Dips into local file to create a table on the website.
//TODO: include pdf functionality
//
var MAX_TITLE_LENGTH = 28; //how many chars the max length of a title should be.
var i = 0;
function refresh(){
  i=1;
  //reset the table...
  document.getElementById("myTable").innerHTML="<tr><th>Title</th><th>Time</th><th>My Curriculum</th><th>Exercise</th></tr>";
  xmlDoc = getXMLDoc();//go into the xml
  while (i<xmlDoc.getElementsByTagName("video").length)
  {
    var vidTag=xmlDoc.getElementsByTagName("video")[i];
    var title1=vidTag.getElementsByTagName("title")[0].childNodes[0].nodeValue;
    if (title1.length > MAX_TITLE_LENGTH)
    {
		title1 = title1.slice(0,MAX_TITLE_LENGTH) + "...";
	}

    var time1 =(vidTag.getElementsByTagName("time")[0].childNodes[0].nodeValue);
    time1 = Math.floor(time1/60) + (time1%60 < 10 ? ":0" : ":") + time1%60;

    var ex1 =  vidTag.getElementsByTagName("exercise");

    insRow(title1,time1,ex1);
    ++i;
  }
  i = 0;
}
  
function getXMLDoc(){
if (window.XMLHttpRequest)
  {
  xhttp=new XMLHttpRequest();
  }
else // IE 5/6
  {
  xhttp=new ActiveXObject("Microsoft.XMLHTTP");
  }
xhttp.open("GET","list.xml",false);
xhttp.send();
return xhttp.responseXML;
}

function insRow(titleP, timeP, exerciseP)
{
  var table=document.getElementById("myTable").insertRow(i);

  var titleT=table.insertCell(0);
  var timeT=table.insertCell(1);
  var checkT = table.insertCell(2);
  var exT = table.insertCell(3);
  titleT.innerHTML="<p=title_"+i+">"+titleP;
  timeT.innerHTML="<p=time_"+i+">"+timeP;
  checkT.innerHTML="<input class=\"csscheckbox\" type=\"checkbox\" name=\"number_"+i+"\" value="+i+">";//does this work?
  exT.innerHTML="<p>";
  for (var j = 0;j<exerciseP.length;j++)
  {
    exT.innerHTML+=("<p=ex_"+i+"_"+j+">"+exerciseP[j].childNodes[0].nodeValue+"<br>");
  }
}

function selectToggle(toggle, form) {
     var myForm = document.forms[form];
     for( var j=0; j < myForm.length; j++ ) { 
          if(toggle) {
               myForm.elements[j].checked = "checked";
          } 
          else {
               myForm.elements[j].checked = "";
          }
     }
}
var numer = [1,2,4,5,7,9,10,11];//etc
function numeric(form) {
     var myForm = document.forms[form];
     for( var j=0; j < myForm.length; j++ ) 
     {
		 if (numer.indexOf(j) > 0)
			{myForm.elements[j].checked = "checked";}
		else
			{myForm.elements[j].checked = "";}
     }
}

