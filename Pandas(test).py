import pandas as pd
import smtplib
import email.message


tabela = pd.read_excel("Teste Excel.xlsx")

print(tabela)

#faturamento da loja
loja = (tabela.groupby("Produto")["Valor"].sum()).to_frame()
print(loja)

#quantidades de produtos vendidods na loja
qnt_produto = (tabela["Produto"].value_counts()).to_frame()
print(qnt_produto)


#media de cada produto
loja_media = (tabela.groupby("Produto")["Valor"].mean()).to_frame()
print(loja_media)


corpo_email = f"""
  <p>Olá nome</p>
  <p>Faturamento</p>
    {loja.to_html(formatters={'Valor': "R${:,.2f}".format})}
  <p>Quantidade vendida</p>
    {qnt_produto.to_html()}
  <p>Média de Preço</p>
    {loja_media.to_html(formatters={'Valor': "R${:,.2f}".format})}
  """
msg = email.message.Message()
msg["Subject"] = "Planilha"
msg["From"] = "Email"
msg["To"] = "Email"
password = "zcfasniendla"
msg.add_header("Content-Type", "text/html")
msg.set_payload(corpo_email)

s = smtplib.SMTP("smtp.gmail.com: 587")
s.starttls()

s.login(msg["from"], password)
s.sendmail(msg["From"], [msg["To"]], msg.as_string().encode("utf-8"))
print("Email enviado")
