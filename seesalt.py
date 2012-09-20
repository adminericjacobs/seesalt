#!/usr/bin/python

from bottle import route, run, template, static_file
import salt.client
import json
import socket

hostname = socket.gethostname()
ip = socket.gethostbyname(socket.gethostname())
if ip == '127.0.1.1':
    host = 'localhost'
else:
    host = hostname
port = '8090'
url_base = 'http://%s:%s' % (host, port)
client = salt.client.LocalClient()


@route('/static/<filename>', name='static')
def static(filename):
    return static_file(filename, root='static')
    
@route('/seesalt')
def home():
    return template('home', url_base=url_base)

@route('/seesalt/license')
def licence():
    return template('license', url_base=url_base)

@route('/seesalt/diskusage')
@route('/seesalt/diskusage/<server>')
@route('/seesalt/diskusage/<server>/<raw:re:raw>')
def diskusage(server='*', raw=False):
    saltresult = client.cmd(server, 'status.diskusage', ['ext?'])
    pretty = json.dumps(saltresult, indent=4) #sort_keys=True can be useful
    if raw == 'raw':
        return saltresult
    else:
        return template('results', result=pretty, url_base=url_base)

@route('/seesalt/pkginstalled')
@route('/seesalt/pkginstalled/<server>')
@route('/seesalt/pkginstalled/<server>/<raw:re:raw>')
def pkginstalled(server='*', raw=False):
    saltresult = client.cmd(server, 'pkg.list_pkgs')
    pretty = json.dumps(saltresult, indent=4)
    if raw == 'raw':
        return saltresult
    else:
        return template('results', result=pretty, url_base=url_base)

@route('/seesalt/pkgupdates')
@route('/seesalt/pkgupdates/<server>')
@route('/seesalt/pkgupdates/<server>/<raw:re:raw>')
def pkginstalled(server='*', raw=False):
    saltresult = client.cmd(server, 'pkg.list_upgrades')
    pretty = json.dumps(saltresult, indent=4)
    if raw == 'raw':
        return saltresult
    else:
        return template('results', result=pretty, url_base=url_base)

@route('/seesalt/servicesenabled')
@route('/seesalt/servicesenabled/<server>')
@route('/seesalt/servicesenabled/<server>/<raw:re:raw>')
def enabledservices(server='*', raw=False):
    saltresult = client.cmd(server, 'service.get_enabled')
    pretty = json.dumps(saltresult, indent=4)
    if raw == 'raw':
        return saltresult
    else:
        return template('results', result=pretty, url_base=url_base)

@route('/seesalt/statecommon')
@route('/seesalt/statecommon/<server>')
@route('/seesalt/statecommon/<server>/<raw:re:raw>')
def statecommon(server=hostname, raw=False):
    saltresult = client.cmd(server, 'state.show_sls', ['common'])
    pretty = json.dumps(saltresult, indent=4)
    if raw == 'raw':
        return saltresult
    else:
        return template('results', result=pretty, url_base=url_base)

@route('/seesalt/statehigh')
@route('/seesalt/statehigh/<server>')
@route('/seesalt/statehigh/<server>/<raw:re:raw>')
def statehigh(server='*', raw=False):
    saltresult = client.cmd(server, 'state.show_highstate')
    pretty = json.dumps(saltresult, indent=4)
    if raw == 'raw':
        return saltresult
    else:
        return template('results', result=pretty, url_base=url_base)

@route('/seesalt/sysinfo')
@route('/seesalt/sysinfo/<server>')
@route('/seesalt/sysinfo/<server>/<raw:re:raw>')
def sysinfo(server='*', raw=False):
    saltresult = client.cmd(server, 'grains.items')
    pretty = json.dumps(saltresult, indent=4)
    if raw == 'raw':
        return saltresult
    else:
        return template('results', result=pretty, url_base=url_base)
    
@route('/seesalt/uptime')
@route('/seesalt/uptime/<server>')
@route('/seesalt/uptime/<server>/<raw:re:raw>')
def uptime(server='*', raw=False):
    saltresult = client.cmd(server, 'status.uptime')
    pretty = json.dumps(saltresult, indent=4)
    if raw == 'raw':
        return saltresult
    else:
        return template('results', result=pretty, url_base=url_base)

@route('/seesalt/userprocs')
@route('/seesalt/userprocs/<server>')
@route('/seesalt/userprocs/<server>/<raw:re:raw>')
def userprocs(server='*', raw=False):
    saltresult = client.cmd(server, 'status.w')
    pretty = json.dumps(saltresult, indent=4)
    if raw == 'raw':
        return saltresult
    else:
        return template('results', result=pretty, url_base=url_base)

if __name__ == '__main__':
    run(host=host, port=port, debug=True)
