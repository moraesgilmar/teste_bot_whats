def verificar_forca_senha(senha):


  comprimento_minimo = 8
  

  # Verificando o comprimento da senha
  if len(senha) < comprimento_minimo:
    print (f"Sua senha e muito curta. Recomenda-se no minimo {comprimento_minimo} caracteres.")

  # TODO: Verifique se a senha contém letras maiúsculas e minúsculas
  elif not any(x.isupper() for x in senha):
    print ("Sua senha nao atende aos requisitos de seguranca.")
  elif not any(x.islower() for x in senha):
    print ("Sua senha nao atende aos requisitos de seguranca.")  
  elif not any(x.isdigit() for x in senha):
    print ("Sua senha nao atende aos requisitos de seguranca.")
  elif not any(x in "!@#$%&*()_+-=[]{}|;:,.<>?/" for x in senha):
    print ("Sua senha nao atende aos requisitos de seguranca.")
  else:
    print ("Sua senha atende aos requisitos de seguranca. Parabens!")

  # Verificando se a senha contém sequências comuns
  sequencias_comuns = ["123456", "abcdef"]
  for sequencia in sequencias_comuns:
    if sequencia in senha:
      return "Sua senha contem uma sequencia comum. Tente uma senha mais complexa."

  # Verificando se a senha contém palavras comuns
  palavras_comuns = ["password", "123456", "qwerty"]
  if senha in palavras_comuns:
    return "Sua senha e muito comum. Tente uma senha mais complexa."

  # TODO: Verificar o comprimento mínimo e critérios de validação



# Obtendo a senha do usuário
senha = input().strip()

# Verificando a força da senha
resultado = verificar_forca_senha(senha)

