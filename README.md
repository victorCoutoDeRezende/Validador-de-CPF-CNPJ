# Validador-de-CPF-CNPJ
Validador de CPF ou CNPJ usando orientação a objetos e o pacote validate_docbr.

Neste projeto temos o arquivo que cria a Classe Documento, que por meio do método cria_documento,
verifica a quantidade de números digitados e caso seja igual à quantidade de números presentes em
um CPF ou um CNPJ, retorna a respectiva classe do documento digitado. Caso o número digitado não 
se enquadre em nenhuma das duas opções, é levantado um erro que alerta o usuário que ele digitou 
algo de errado. Nas Classes DocCPF e DocCNPJ são implementados os métodos "__str__", o método "valida",
que utiliza o pacote validate_docbr para fazer a validação tanto do CPF quanto do CNPJ e retorna True 
ou False de acordo com a validação do documento, e o método "formata", que também usa o pacote para 
implementar uma máscara e retornar os números digitados com suas pontuações de acordo com o documento

Já no arquivo main, é imprimida uma mensagem de abertura e pede-se para o usuário digitar os números, 
depois disso é instanciado um Objeto "doc" que utiliza a Classe Documento e o método cria_documento que
apresenta ao usuário o campo de digitação para o número a ser verificado
