
import pandas as pd
from twilio.rest import Client
# Your Account SID from twilio.com/console
account_sid = "AC7c8b4adc2da4fc3ade76965060f8c317"
# Your Auth Token from twilio.com/console
auth_token = "c65dca9ae629aecf81bc9ab524e72214"
client = Client(account_sid, auth_token)

lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        print(f'No mês {mes} a meta foi batida. Pelo vendedor: {vendedor}, Quantidade de vendas: {vendas}')
        message = client.messages.create(
            to="+5521980318203",
            from_="+19402897582",
            body=f'No mês {mes} a meta foi batida pelo vendedor: {vendedor}, quantidade de vendas: {vendas}')
        print(message.sid)

