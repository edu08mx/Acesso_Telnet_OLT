import telnetlib

host = "0.0.0.0"  
porta = 23  
usuario = "user"
senha = "password"

try:
    tn = telnetlib.Telnet(host, porta)
    print(tn.read_until(b"login: ", timeout=5).decode('utf-8'))    
    tn.write(usuario.encode('utf-8') + b"\n")
    print(tn.read_until(b"Password: ", timeout=5).decode('utf-8'))
    tn.write(senha.encode('utf-8') + b"\n")
    print(tn.read_until(b"putty", timeout=10).decode('utf-8'))
    
    tn.close()    

except Exception as e:
    print("Erro: ", e)
