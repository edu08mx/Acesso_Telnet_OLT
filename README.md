Explicação do Código
host: Endereço IP do host Telnet.
porta: Porta Telnet do host.
usuario: Nome de usuário para o login.
senha: Senha para o login.
O script realiza as seguintes etapas:

Conecta-se ao host Telnet.
Lê a resposta até encontrar a string "login:" e imprime-a.
Envia o nome de usuário codificado em UTF-8.
Lê a resposta até encontrar a string "Password:" e imprime-a.
Envia a senha codificada em UTF-8.
Lê a resposta até encontrar a string "putty" e imprime-a.
Fecha a conexão Telnet.
Se ocorrer algum erro durante a execução, será exibida uma mensagem de erro.

Nota: Certifique-se de usar este script de forma responsável e de acordo com as políticas e permissões do sistema ao qual você está se conectando.