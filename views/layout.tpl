<html>
<head>

  <title>SeeSalt</title>
  <link rel="stylesheet" type="text/css" href="{{url_base}}/static/style.css" />
</head>

<body>
  <div id="container">
    <div id="header">
        <img id="banner" src="{{url_base}}/static/salt-logo.png"/><br/>
        <hr />
    </div><!-- end header -->

    <div id="left">
      <h3>Remote Execution</h3>

        <a href="{{url_base}}/seesalt/diskusage">Disk Usage</a><br/>
        <a href="{{url_base}}/seesalt/pkginstalled">Packages Installed</a><br/>
        <a href="{{url_base}}/seesalt/pkgupdates">Package Updates</a><br/>
        <a href="{{url_base}}/seesalt/servicesenabled">Services Enabled</a><br/>
        <a href="{{url_base}}/seesalt/sysinfo">System Info</a><br/>
        <a href="{{url_base}}/seesalt/uptime">Uptime</a><br/>
        <a href="{{url_base}}/seesalt/userprocs">Users Processes</a>

      <h3>Config Managment</h3>

        <a href="{{url_base}}/seesalt/statecommon">Common State</a><br/>
        
      %for i in range(3):  
      <p> </p><br/>
      %end

    </div><!-- end left division -->

    <div id="main">
      %include
    </div>

    <div id="footer">
      <hr />

      <p class="left"> | 
      <a href="{{url_base}}/seesalt/license">License</a> | 
      <a href="http://saltstack.org/">SaltStack</a> | 
      <a href="http://bottlepy.org">Bottle</a> |
      </p>

      <p class="right">SeeSalt 2012</p>

      <p> </p><br/>
    </div><!-- end footer -->
  </div><!-- end container -->
</body>
</html>
