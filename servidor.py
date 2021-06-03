#* coding : utf-8 *
from http.server import HTTPServer, BaseHTTPRequestHandler
import cgi
import subprocess, os, time, socket
import mysql.connector
from datetime import date
from datetime import datetime
import urllib.request as urllib

#


#Fecha actual
nowes = datetime.now()

import sys
version = sys.version[0]

if version == '2':
    import urllib2 as urllib
else:
    import urllib.request as urllib

url1 = None
url2 = None
servidor1 = 'http://www.soporteweb.com'
servidor2 = 'http://www.ifconfig.me/ip'

consulta1 = urllib.build_opener()
consulta1.addheaders = [('User-agent', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:57.0) Gecko/20100101 Firefox/57.0')] 
consulta2=consulta1

try:
    url1 = consulta1.open(servidor1, timeout=17)
    respuesta1 = url1.read()
    if version == '3':
        try:
            respuesta1 = respuesta1.decode('UTF-8')
        except UnicodeDecodeError:
            respuesta1 = respuesta1.decode('ISO-8859-1')

    url1.close()
    #print('Servidor1:'+respuesta1)
  
except:
  #print('Falló la consulta ip a '+servidor1)
    pass

#Datos IP
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("iplocation.com", 80))

ip_publico = respuesta1

ip_equipo = s.getsockname()[0]

hostname = socket.gethostname()

#Base de datos
db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    db="ipcc",
    charset="utf8")
cursor = db.cursor()

def reload():
    cursor.execute("select id,ip_equipo,ip_publico,ip_remoto,hostname,fecha from datos_maquina")
    for base in cursor:
        a = base


class ErrorHandler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        self.send_error(404)
#Web con RequestHandler
class requestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
###########################################################################################          
        if self.path.endswith('/tasklist'):
            self.send_response(200)
            self.send_header('content-type', 'text/html')
            self.end_headers()
            output = ''
            output += '<html><head><link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-eOJMYsd53ii+scO/bJGFsiCZc+5NDVN2yr8+0RDqr0Ql0h+rP48ckxlpbzKgwra6" crossorigin="anonymous"></head><body><meta charset="UTF-8">'
            output += '<h1>ULTIMA EJECUCION</h1>  '
            output += '''
<<<<<<< HEAD
            <html>
<body>

<p>Enter names in the fields, then click "Submit" to submit the form:</p>

<form id="frm1" action="/tasklist/new">
  First name: <input type="text" name="fname"><br>
  Last name: <input type="password" name="lname"><br><br>
  <input type="button" onclick="myFunction()" value="Submit">
</form>

<script>
function myFunction() {
  document.getElementById("pass").submit();
}
</script>

</body>
</html>

=======
            <table class="table">
  <thead>
    <tr>
      <th scope="col">#</th>
      <th scope="col">First</th>
      <th scope="col">Last</th>
      <th scope="col">Handle</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th scope="row">1</th>
      <td>Mark</td>
      <td>Otto</td>
      <td>@mdo</td>
    </tr>
    <tr>
      <th scope="row">2</th>
      <td>Jacob</td>
      <td>Thornton</td>
      <td>@fat</td>
    </tr>
    <tr>
      <th scope="row">3</th>
      <td colspan="2">Larry the Bird</td>
      <td>@twitter</td>
    </tr>
  </tbody>
</table>
>>>>>>> 0add7547bec2dfc220c6dd69daf887270c56ff8a
            '''

            output += '''<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/js/bootstrap.bundle.min.js" integrity="sha384-JEW9xMcG8R+pH31jmWH6WWP0WintQrMb4s7ZOdauHnUtxwoG2vI5DkLtS3qm9Ekf" crossorigin="anonymous"></script>
            <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.1/dist/umd/popper.min.js" integrity="sha384-SR1sx49pcuLnqZUnnPwx6FCym0wLsk5JZuNx2bPPENzswTNFaQU1RDvt3wT4gWFG" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/js/bootstrap.min.js" integrity="sha384-j0CNLUeiqtyaRmlzUHCPZ+Gy5fQu0dQ6eZ/xAww941Ai1SxSY+0EQqNXNE6DZiVc" crossorigin="anonymous"></script>
            '''
            output += f'{reload()}'
        
            output += '</body></html>'
            self.wfile.write(output.encode())
######################################################################################    


        if self.path.endswith('/new'):
            self.send_response(200)
            self.send_header('content-type', 'text/html')
            self.end_headers()
            output = ''
          
            output += '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-eOJMYsd53ii+scO/bJGFsiCZc+5NDVN2yr8+0RDqr0Ql0h+rP48ckxlpbzKgwra6" crossorigin="anonymous">
    <link href="favicon.ico" rel="shortcut icon">
<<<<<<< HEAD
    

    <meta name="viewport" content="width=device-width, initial-scale=1">
    

=======
    <meta name="viewport" content="width=device-width, initial-scale=1">
<style>
.footer {
   position: fixed;
   left: 0;
   bottom: 0;
   width: 100%;
   background-color: white;
   color: black;
   text-align: center;
}
</style>
>>>>>>> 0add7547bec2dfc220c6dd69daf887270c56ff8a
    <script>
    
    
    </script>
    <title>Restablecer IPCC</title>
    
</head>
  
<body style="position:relative;">'''


            output += '''
            
            
            
            
            
           
            <nav class="navbar navbar-dark bg-dark">
        <div class="container">
          <a class="navbar-brand" href="#">
            <img src="https://mdybpo.com/wp-content/uploads/2017/11/logo_w.png" alt="" width="80" height="44">
            Reparador MDY
          </a>
        
      </nav>
      </br>
<div class='container'></div>'''

            output += '''<center><form method="POST" enctype="multipart/form-data" action="/tasklist/new"><p>Direccion IP a remotear: <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-arrow-down-circle-fill" viewBox="0 0 16 16">
  <path d="M16 8A8 8 0 1 1 0 8a8 8 0 0 1 16 0zM8.5 4.5a.5.5 0 0 0-1 0v5.793L5.354 8.146a.5.5 0 1 0-.708.708l3 3a.5.5 0 0 0 .708 0l3-3a.5.5 0 0 0-.708-.708L8.5 10.293V4.5z"/>
</svg></i></p>'''
            
            output += '<input name="task" maxlength="15" type="text" placeholder="Ingresa direccion IP">'
            #output += '''</br><h3>Acciones a realizar:</h3></br>'''
            
            output += '''<button type="submit" id="ipcc" value="Restablecer servicio ipcc">Restablecer servicio ipcc <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-bar-chart-fill" viewBox="0 0 16 16">
  <path d="M1 11a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v3a1 1 0 0 1-1 1H2a1 1 0 0 1-1-1v-3zm5-4a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v7a1 1 0 0 1-1 1H7a1 1 0 0 1-1-1V7zm5-5a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v12a1 1 0 0 1-1 1h-2a1 1 0 0 1-1-1V2z"/>
</svg></button>'''
            output += '</br>'
            output += '</br>'
            output += '</form>'
            
            
            output += '''<center><form method="POST" enctype="multipart/form-data" action="/tasklist/now"><p>Direccion IP a remotear: <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-arrow-down-circle-fill" viewBox="0 0 16 16">
  <path d="M16 8A8 8 0 1 1 0 8a8 8 0 0 1 16 0zM8.5 4.5a.5.5 0 0 0-1 0v5.793L5.354 8.146a.5.5 0 1 0-.708.708l3 3a.5.5 0 0 0 .708 0l3-3a.5.5 0 0 0-.708-.708L8.5 10.293V4.5z"/>
</svg></i></p>'''
            
            output += '<input name="now" maxlength="15" type="text" placeholder="Ingresa direccion IP">'
            #output += '''</br><h3>Acciones a realizar:</h3></br>'''
            
            output += '''<button type="submit" id="down" value="Reiniciar PC">Reiniciar Computadora<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-power" viewBox="0 0 16 16">
  <path d="M7.5 1v7h1V1h-1z"/>
  <path d="M3 8.812a4.999 4.999 0 0 1 2.578-4.375l-.485-.874A6 6 0 1 0 11 3.616l-.501.865A5 5 0 1 1 3 8.812z"/>
</svg></button>'''
            output += '</form></center>'
            output += '''
<<<<<<< HEAD
            <footer class="footer" style="position: fixed; left: 0;bottom: 0;width: 100%;background-color: white;color: black;text-align: center">
=======
            <footer class="footer">
>>>>>>> 0add7547bec2dfc220c6dd69daf887270c56ff8a
            <div>
            <span>Copyright © MDY 2021 Innovacion Tecnologica MG
            <div align="right">
             
            Auspiciado por:
            <a class="btn btn-outline-light" target="_blank" hf="https://www.facebook.com/El-Point-Chalaco-108072914697936/">
            <img src="https://raw.githubusercontent.com/D4rksit3/ServerWebPython/master/logo.jpg" width="65" height="65">
            </a></div></div></span>
            </footer>
            
            '''
<<<<<<< HEAD
            output += '''
            <div class="contenido" id="contenido" style="width: 100vw;height: 100vh;position: absolute;top: 0;left: 0;background: white;display: flex;justify-content: center;align-items: center;">
            
            <img src="https://mdybpo.com/wp-content/uploads/2017/11/logo_w.png" alt="" width="250" height="140">
            <div style="display: flex;flex-direction: column;width:15%;heiht:450px;align-items: center;justify-content: space-between;">
            <label for="nombre">Usuario: </label>
            <input type="text" id="nombre">
            
            <label for="contrasena">Contraseña: </label>
            <input type="password" id="contrasena">
            <br>
            <button class="btn btn-success" onclick="myFunction()">Iniciar Sesión</button>
            </div></div>
            
            '''
            
            
            output +=  '''<script>
    function myFunction(){
	    var password;
        var sub;
        var usuario;
        var user = "Admin"
        var pass = "Mdy12345*"
    
	    usuario = document.getElementById("nombre").value;
        password = document.getElementById("contrasena").value;
      cambio = document.getElementById('contenido');

    
        if (usuario == user && password == pass){
            //document.getElementById('pass');
            //ocument.getElementById("pass");
            alert("Sucefull!");
            cambio.style.visibility = "hidden";
            
            }
          //else if (usuario == user){
            //document.getElementById('pass');
            //prompt("Exitoso!2");
          //}
        else{
            alert("Error de credenciales.");
      
          }
    }   
    
    
    
</script>'''
            
            
=======
>>>>>>> 0add7547bec2dfc220c6dd69daf887270c56ff8a
            output += '<html></body>'

            self.wfile.write(output.encode())


        

            


    def do_POST(self):
        if self.path.endswith('/new'):
            ctype, pdict = cgi.parse_header(self.headers.get('content-type'))
            
            pdict['boundary'] = bytes(pdict['boundary'], "utf-8")
            content_len = int(self.headers.get('Content-length'))
            pdict['CONTENT-LENGTH'] = content_len

            #if ctype == 'multipart/form-data':
            fields = cgi.parse_multipart(self.rfile, pdict)
            IP = fields.get('task')  
            a = (''.join(IP))
<<<<<<< HEAD
            subprocess.run("start C:\\xampp\\mysql\\bin\\mysqld.exe", shell=True)
            tipado = str("ipcc")
            sql = f"INSERT INTO datos_maquina(ip_equipo,ip_publico,ip_remoto,hostname,fecha, tipo) values('{ip_equipo}','{ip_publico}','{a}','{hostname}','{nowes}','{tipado}')"
=======
            os.system("C:\\xampp\\mysql\\bin\\mysqld.exe")
            
            sql = f"INSERT INTO datos_maquina(ip_equipo,ip_publico,ip_remoto,hostname,fecha) values('{ip_equipo}','{ip_publico}','{a}','{hostname}','{nowes}')"
>>>>>>> 0add7547bec2dfc220c6dd69daf887270c56ff8a
            cursor.execute(sql)
            db.commit()
            ips = "\\\\"+a

            #os.system("start PsExec -i -accepteula /nobanner")

<<<<<<< HEAD
            subprocess.run(f"start pskill64.exe {ips} -u administrador -p @C0l0n14l# -accepteula -nobanner iexplore.exe", shell=True) and subprocess.run(f"start pskill64.exe {ips} -u administrador -p soporte@ -accepteula -nobanner iexplore.exe", shell=True) 
            
            time.sleep(1)

            subprocess.run(f"start psexec.exe -i {ips} -accepteula -u administrador -p @C0l0n14l# -c reset.bat", shell=True) and subprocess.run(f"start psexec.exe -i {ips} -accepteula -u administrador -p soporte@ -c reset.bat", shell=True)


            #subprocess.run()
            #time.sleep(5)
            #os.system(f"start psexec.exe -i \\\\{a} -accepteula -u administrador -p @C0l0n14l# -c start.bat") and os.system(f"start psexec.exe -i \\\\{a} -accepteula -u administrador -p soporte@ -c start.bat")
            
            #self.end_headers()
            
            #time.sleep(5)
=======
            #os.system("start PsExec -i -accepteula /nobanner")

            subprocess.run(f"start pskill64.exe \\\\{a} -u administrador -p @C0l0n14l# -accepteula -nobanner iexplore.exe", shell=True) and subprocess.run(f"start pskill64.exe \\\\{a} -u administrador -p soporte@ -accepteula -nobanner iexplore.exe",shell=True)
            #subprocess.run()
            time.sleep(5)
            os.system(f"start psexec.exe -i \\\\{a} -accepteula -u administrador -p @C0l0n14l# -c start.bat") and os.system(f"start psexec.exe -i \\\\{a} -accepteula -u administrador -p soporte@ -c start.bat")
            
            #self.end_headers()
            
            time.sleep(5)
>>>>>>> 0add7547bec2dfc220c6dd69daf887270c56ff8a
            #subprocess.run(f"start PsExec \\\\{a} -u administrador #-p @C0l0n14l# -nobanner cscript script.vbs", Shell=True)
            #time.sleep(3)
            if self.send_response(301):
                self.send_header('content-type', 'text/html')
                output = ''
                output += '''<!DOCTYPE html>
                <html lang="en">
                <head>
                <meta charset="UTF-8">
                <meta http-equiv="X-UA-Compatible" content="IE=edge">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-eOJMYsd53ii+scO/bJGFsiCZc+5NDVN2yr8+0RDqr0Ql0h+rP48ckxlpbzKgwra6" crossorigin="anonymous">
                <link href="favicon.ico" rel="shortcut icon">
                <title>Restablecer IPCC</title>
                </head>
                <body>'''
                output += '<div class="alert alert-success" role="alert">'
                output += 'Operacion Exitosa!'
                output += '</div>'
                output += '</html></body>'
                self.wfile.write(output.encode())
            time.sleep(2)
            self.send_header('Location', '/tasklist/new')

            self.end_headers()
            
            
        
        if self.path.endswith('/now'):
            ctype, pdict = cgi.parse_header(self.headers.get('content-type'))
            
            pdict['boundary'] = bytes(pdict['boundary'], "utf-8")
            content_len = int(self.headers.get('Content-length'))
            pdict['CONTENT-LENGTH'] = content_len

<<<<<<< HEAD
            if ctype == 'multipart/form-data':
              fields = cgi.parse_multipart(self.rfile, pdict)
              IP = fields.get('now')  
              a = ("\\\\"+''.join(IP))
              subprocess.run("start C:\\xampp\\mysql\\bin\\mysqld.exe", shell=True)
              tipo = "reinicio"
              sql = f"INSERT INTO datos_maquina(ip_equipo,ip_publico,ip_remoto,hostname,fecha,tipo) values('{ip_equipo}','{ip_publico}','{a}','{hostname}','{nowes}','{tipo}')"
              cursor.execute(sql)
              db.commit()

            #14154
              subprocess.run(f"start psshutdown.exe {a} -accepteula -u administrador -p @C0l0n14l# -r ",shell=True) and subprocess.run(f"start psshutdown.exe -i {a} -accepteula -u administrador -p soporte@ -r ",shell=True)
              time.sleep(0.5)
              subprocess.run(f"start psexec.exe -i {a} -accepteula -u administrador -p @C0l0n14l# -c down.bat",shell=True) and subprocess.run(f"start psexec.exe -i {a} -accepteula -u administrador -p soporte@ -c down.bat",shell=True)

              time.sleep(3)
              if self.send_response(301):
=======
            #if ctype == 'multipart/form-data':
            fields = cgi.parse_multipart(self.rfile, pdict)
            IP = fields.get('now')  
            a = (''.join(IP))
            
            
            sql = f"INSERT INTO datos_maquina(ip_equipo,ip_publico,ip_remoto,hostname,fecha) values('{ip_equipo}','{ip_publico}','{a}','{hostname}','{nowes}')"
            cursor.execute(sql)
            db.commit()

            
            subprocess.run(f"start psshutdown.exe \\\\{a} -u administrador  -p @C0l0n14l# -r ",shell=True) and subprocess.run(f"start psshutdown.exe \\\\{a} -u administrador -p soporte@ -r ",shell=True)

            time.sleep(3)
            if self.send_response(301):

                self.send_header('content-type', 'text/html')
                output = ''
                output += '''<!DOCTYPE html>
            <html lang="en">
                <head>
                <meta charset="UTF-8">
                <meta http-equiv="X-UA-Compatible" content="IE=edge">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-eOJMYsd53ii+scO/bJGFsiCZc+5NDVN2yr8+0RDqr0Ql0h+rP48ckxlpbzKgwra6" crossorigin="anonymous">
                <link href="favicon.ico" rel="shortcut icon">
                <title>Restablecer IPCC</title>
                </head>
                <body>'''
                output += '<div class="alert alert-success" role="alert">'
                output += 'Operacion Exitosa!'
                output += '</div>'
                output += '</html></body>'
                self.wfile.write(output.encode())
              self.send_header('Location', '/tasklist/new')
              self.end_headers()

#Server Web        

def main():
    os.system("cls")
    a = 0
    while True:
        b = time.time()
        if b - a > 2:

            IP = ip_equipo   
            PORT = 8888
            DireccionServer = (IP, PORT)
            server = HTTPServer(DireccionServer, requestHandler)
    
            print(f"Servidor corriendo en {IP} con el puerto {PORT}")
<<<<<<< HEAD
            server = server.serve_forever()
            
            print(server)
=======
            server.serve_forever()

>>>>>>> 0add7547bec2dfc220c6dd69daf887270c56ff8a
if __name__ == '__main__':
    main()