<?php

date_default_timezone_set("UTC"); 
ini_set('mongo.long_as_object', 1); 
 
$dbhost = 'localhost'; 
$dbname = 'cta-db'; 
 
$m = new MongoClient("mongodb://bartolovic:bartolovic@ds019886.mlab.com:19886/cta-db");
$db = $m->$dbname; 
$results; 
$collection = $db->magic; 
if(isset($_POST['submit'])){ 

    $minDate = new MongoDate(strtotime($_POST['datepickerOD']));
    $maxDate = new MongoDate(strtotime($_POST['datepickerDO']));

    $array = array( 
    //'date' => array('$gte' => $_POST['datepickerOD'], '$lte' => $_POST['datepickerDO']),
    'date' => array('$gte' => $minDate, '$lte' => $maxDate),
    'telescope' => $_POST['teleskop'], 
    'name' => $_POST["name"] 
    );
 
    $results = $collection->find($array); 
} 
else
{
    //$minDate1 = new MongoDate(strtotime('2012-12-09T23:00:00.000Z'));
    //$maxDate1 = new MongoDate(strtotime('2012-12-20T23:00:00.000Z'));

    $array1 = array( 
    //'date' => array('$gte' => '2012-12-09T23:00:00.000Z', '$lte' => '2012-12-20T23:00:00.000Z'),
    //'date' => new Mongodate(strtotime('2012-12-10T23:00:00.000Z')),
    //'date' => array('$gte' => $minDate1, '$lte' => $maxDate1),
    'telescope' => 'M1',
    'name' => 'drvdev_daq'
    );

    //$results = $collection->find()->limit(1000);
    $results = $collection->find($array1)->limit(100);
    //$results = $collection->find($array1);
} 

$series = array(); 
$i=0; 
foreach($results as $result){

    //echo $result['date']->toDateTime()->format('Y-m-d');
    //echo date('Y-m-d',$result['date']->sec);
    //echo date('Y-m-d', PHP_INT_MAX);

    //$series[$i]['date']= $result['date']->toDateTime()->format('Y-m-d');
    $series[$i]['date']= date('Y-m-d',$result['date']->sec); 
    $series[$i]['mean']=$result['mean']; 
    $series[$i]['median']=$result['median']; 
    $series[$i]['min']=$result['min']; 
    $series[$i]['max']=$result['max']; 
    $series[$i]['telescope']=$result['telescope']; 
    $series[$i]['rms']=$result['rms'];

    $i++; 
}

$datemin = $series[0]['date'];
$indexmin = 0;
$seriesFinal = array(); 

for ($i = 0; $i < count($series); $i++){

  for ($j = 0; $j < count($series); $j++){
    if ($series[$j]['date'] < $datemin){
      $datemin = $series[$j]['date'];
      $indexmin = $j;
    }
  }
  $seriesFinal[$i]['date'] = $datemin;
  $seriesFinal[$i]['mean']=$series[$i]['mean']; 
  $seriesFinal[$i]['median']=$series[$i]['median']; 
  $seriesFinal[$i]['min']=$series[$i]['min']; 
  $seriesFinal[$i]['max']=$series[$i]['max']; 
  $seriesFinal[$i]['telescope']=$series[$i]['telescope']; 
  $seriesFinal[$i]['rms']=$series[$i]['rms'];
  $series[$indexmin]['date'] = date('Y-m-d', PHP_INT_MAX);
  $datemin = date('Y-m-d', PHP_INT_MAX);
}
 
?>

<html> 
<head> 
<link rel="stylesheet" href="http://www.amcharts.com/lib/3/plugins/export/export.css"> 
<link  rel="stylesheet" href="//code.jquery.com/ui/1.11.4/themes/smoothness/jquery-ui.css"> 
<script src="http://www.amcharts.com/lib/3/amcharts.js"></script> 
<script src="http://www.amcharts.com/lib/3/serial.js"></script> 
<script src="http://www.amcharts.com/lib/3/themes/light.js"></script> 
<script src="http://www.amcharts.com/lib/3/plugins/export/export.js"></script> 
  <script src="//code.jquery.com/jquery-1.10.2.js"></script> 
  <script src="//code.jquery.com/ui/1.11.4/jquery-ui.js"></script> 
<style> 
                #chartdiv { 
            width    : 100%; 
            height    : 500px; 
        } 
#chartdiv > div > div.amcharts-chart-div > a{ 
display:none !important; 
} 
</style> 
    <script> 
      $(function() { 
      $( "#datepickerOD" ).datepicker({ dateFormat: 'yy-mm-dd' }); 
      $( "#datepickerDO" ).datepicker({ dateFormat: 'yy-mm-dd' }); 
      }); 
    </script> 
<script> 

var chartData = <?php echo json_encode($seriesFinal); ?> 

var chart = AmCharts.makeChart("chartdiv", { 
    "type": "serial", 
    "theme": "light",
    "dataDateFormat": "YYYY-MM-DD",
    //"dataDateFormat": "YYYY-MM-DDTJJ:NN:SS.QQQZ",
    //"dataDateFormat": "YY-MM-DD",
    //"dataDateFormat": "YYYY-MM-DD JJ:NN:SS",
    "legend": { 
        "useGraphSettings": true 
    }, 
    "dataProvider": chartData, 
    "valueAxes": [{ 
        "id":"v1", 
        "axisColor": "#FF6600", 
        "axisThickness": 2, 
        "gridAlpha": 0, 
        "axisAlpha": 1, 
        "position": "left" 
    }, { 
        "id":"v2", 
        "axisColor": "#FCD202", 
        "axisThickness": 2, 
        "gridAlpha": 0, 
        "axisAlpha": 1, 
        "position": "right" 
    }, { 
        "id":"v3", 
        "axisColor": "#B0DE09", 
        "axisThickness": 2, 
        "gridAlpha": 0, 
        "offset": 50, 
        "axisAlpha": 1, 
        "position": "left" 
    }, 
    { 
        "id":"v4", 
        "axisColor": "#0000FF", 
        "axisThickness": 2, 
        "gridAlpha": 0, 
        "offset": 50, 
        "axisAlpha": 1, 
        "position": "right" 
    }, 
    { 
        "id":"v5", 
        "axisColor": "#003300", 
        "axisThickness": 2, 
        "gridAlpha": 0, 
        "offset": 50, 
        "axisAlpha": 1, 
        "position": "left" 
    } 
    ], 
    "graphs": [{ 
        "valueAxis": "v1", 
        "lineColor": "#FF6600", 
        "bullet": "round", 
        "bulletBorderThickness": 1, 
        "hideBulletsCount": 30, 
        "title": "MAX", 
        "valueField": "max", 
        "fillAlphas": 0 
    }, { 
        "valueAxis": "v2", 
        "lineColor": "#FCD202", 
        "bullet": "round", 
        "bulletBorderThickness": 1, 
        "hideBulletsCount": 30, 
        "title": "MIN", 
        "valueField": "min", 
        "fillAlphas": 0 
    }, { 
        "valueAxis": "v3", 
        "lineColor": "#B0DE09", 
        "bullet": "round", 
        "bulletBorderThickness": 1, 
        "hideBulletsCount": 30, 
        "title": "MEDIAN", 
        "valueField": "median", 
        "fillAlphas": 0 
    }, 
    { 
        "valueAxis": "v4", 
        "lineColor": "#0000FF", 
        "bullet": "round", 
        "bulletBorderThickness": 1, 
        "hideBulletsCount": 30, 
        "title": "MEAN", 
        "valueField": "mean", 
        "fillAlphas": 0 
    }, 
    { 
        "valueAxis": "v5", 
        "lineColor": "#003300", 
        "bullet": "round", 

        "bulletBorderThickness": 1, 
        "hideBulletsCount": 30, 
        "title": "RMS", 
        "valueField": "rms", 
        "fillAlphas": 0 
    } 
    ], 
    "chartScrollbar": {}, 
    "chartCursor": { 
        "cursorPosition": "mouse" 
    }, 
    "categoryField": "date", 
    "categoryAxis": { 
        "parseDates": true, 
        "axisColor": "#DADADA", 
        "minorGridEnabled": true 
    }, 
    "export": { 
        "enabled": true, 
	"position": "bottom-right"
     } 
}); 
 
  chart.addListener("dataUpdated", zoomChart); 
  zoomChart(); 

  function zoomChart() {
	chart.zoomToIndexes(chart.dataProvider.length - 20, chart.dataProvider.length -1);
  }
 

 
  </script> 
  </head> 

  <body> 
    <p align="center"> Grafički prikaz baze podataka CTA teleskopa</p>

    <form method="post" action="index.php" name="submitForm" id="submitForm"> 

    <p>Datum od: <input type="text" name = "datepickerOD" id="datepickerOD"></p> 
    <p>Datum do: <input type="text" name = "datepickerDO" id="datepickerDO"></p> 
    <p>Teleskop: 
      <select name ="teleskop" id="teleskop"> 
        <option value ="M1">M1</option> 
        <option value ="M2">M2</option> 
      </select>
    </p> 

    <p>Naziv parametra: 
      <select name="name" id="name"> 

      <?php 
        $array = array 
        ( 
          //'drvzd' => 'Zenith angle', 
          'drvdev_daq' => 'Control Deviation of the Motors, DAQ data', 
          'camhv_daq' => 'Camera HV, DAQ data', 
          'camdc_daq' => 'Camera DC, DAQ data', 
          'camdt_daq' => 'Discriminator Threshold, DAQ data', 
          'campd_daq' => 'PD, DAQ data', 
          'campixtemp_daq' => 'Pixel Temperature Camera, DAQ data', 
          'meanpixtemp_daq' => 'Pixel Temperature, DAQ data', 
          'camclusttemp' => '(Non-zero) Cluster Temperature', 
          'camvcelbias_daq' => 'VCELs bias, DAQ data', 
          'camlv1temp' => 'LV1 Temperature', 
          'camlv2temp' => 'LV2 Temperature', 
          'camlv1hum' => 'LV1 Humidity', 
          'camlv2hum' => 'LV2 Humidity', 
          'camcoolfcptopleft' => 'Camera Cooling: FCPTopLeft Temperature', 
          'camcoolfcpbottright' => 'Camera Cooling: FCPBottRight Temperature', 
          'camcoolrcptopleft' => 'Camera Cooling: RCPTopLeft Temperature', 
          'camcoolrcpbottright' => 'Camera Cooling: RCPBottRight Temperature', 
          'camcoolchasiastopleft' => 'Camera Cooling: ChasiasTopLeft Temperature', 
          'camcoolchasiasbottright' => 'Camera Cooling: ChasiasBottRight Temperature', 
          'camcoolchasiasftopleft' => 'Camera Cooling: ChasiasFTopLeft Temperature', 
          'camcoolchasiasfbottright' => 'Camera Cooling: ChasiasFBottRight Temperature', 
          'camcoolrearbottleft' => 'Camera Cooling: RearBottLeft Humidity ', 
          'camcoolreartopleft' => 'Camera Cooling: RearTopLeft Humidity', 
          'camcoolfrontbottright' => 'Camera Cooling: FrontBottRight Humidity ', 
          'camcoolfronttopright' => 'Camera Cooling: FrontTopRight Humidity', 
          'amcerr' => 'AMC Number of Panels in Error State', 
          'l1t' => 'L1 Trigger Rate (Before Prescaler)', 
          'l2t' => 'L2 Trigger Rate (After Prescaler)', 
          'l2t_daq' => 'L2 Trigger Rate (After Prescaler), DAQ data', 
          'calbtemp1' => 'Calibration Box Temperature', 
          'calbtemp2' => 'Calibration Box Temperature, next to heating plate', 
          'calbhum' => 'Calibration Box Humidity', 
          'sg_devaz' => 'Azimuthal Misspointing * Sin(Zenith)', 
          'sg_devzd' => 'Zenith Misspointing', 
          'sg_camcx' => 'Camera Centre X', 
          'sg_camcy' => 'Camera Centre Y', 
          'sg_stars' => 'Number of Correlated Stars', 
          'sg_bright' => 'Sky Brightness', 
          'wea_temp' => 'Atmospheric Temperature', 
          'wea_hum' => 'Atmospheric Humidity', 
          'wea_ws' => 'Wind Speed', 
          'wea_gust' => 'Wind Gusts', 
          'wea_see' => 'Seeing (from TNG)', 
          'wea_dust' => 'Dust concentration (from TNG)', 
          'rec_temp' => 'Recievers Temperature', 
          'camtd_daq' => 'Trigger Delay, DAQ data ', 
          'camipr_daq' => 'IPR, DAQ data', 
          'camiprerr_daq' => 'IPR Error, DAQ data', 
          'pyro_cloud' => 'Pyrometer, Cloudiness', 
          'pyro_skyt' => 'Pyrometer, Sky Temperature', 
          'muon_psf' => 'PSF from muons', 
          'muon_psfn' => 'Number of muons for PSF calc', 
          'muon_size' => 'Mean muon size', 
          'calq_cal' => 'Calibration runs: Calibration Charge', 
          'calq_int' => 'Interleaved runs: Calibration Charge ', 
          'calq_sig' => 'Charge for Signal Events ', 
          'bias_sig' => 'Bias of Signal Extractor ', 
          'hitfrac_sig' => 'Hit Fraction of Signal Events ', 
          'arrtm_cal' => 'Calibration runs: Arrival Time', 
          'arrtm_int' => 'Interleaved runs: Arrival Time', 
          'arrtm_sig' => 'Signal events: Arrival Time', 
          'arrtmrms_cal' => 'Calibration runs: Arrival Time RMS ', 
          'arrtmrms_int' => 'Interleaved runs: Arrival Time RMS', 
          'arrtmrms_sig' => 'Signal events: Arrival Time RMS', 
          'ped_ped' => 'Pedestal runs: Pedestal', 
          'ped_int' => 'Interleaved runs: Pedestal', 
          'npe_int' => 'Interleaved runs: Number of Photoelectrons', 
          'pedrms_ped' => 'Pedestal runs: Pedestal RMS', 
          'pedrms_int' => 'Interleaved runs: Pedestal RMS', 
          'cfact_int' => 'Interleaved runs: C Factor' 
        ); 

        foreach ($array as $key => $value){ 
          echo "<option value='".$key."'>".$value."</option>"; 
        } 
      ?>     
      </select> 
    </p> 
 
    <input type="submit" name="submit" value="Submit" /> 
 
    </form> 

    <div id="chartdiv"></div>                         

</body> 
</html>
