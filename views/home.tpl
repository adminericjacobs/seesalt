<div id="home">
<p>SeeSalt is a simple web front-end to Salt.</p>

<p>All reports by default return information from all servers. If you want to get data from a single server you can append the hostname to the URL.</p>

<p>Example:<br/>
<a href="{{url_base}}/salt/sysinfo/csdrsdfs">{{url_base}}/salt/sysinfo/csdrsdfs</a></p>

<p>You can also get raw JSON returned by appending "raw" to the URL.</p>

<p>Example:<br/>
<a href="{{url_base}}/salt/sysinfo/csdrsdfs/raw">{{url_base}}/salt/sysinfo/csdrsdfs/raw</a></p>
</div>

<p> </p><br/>
<p> </p><br/>

%rebase layout url_base=url_base
