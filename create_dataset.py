import json

dataset = [
    {
        "pergunta": "Como posso ver minha fatura online?",
        "resposta": "Você pode acessar sua fatura online entrando no site da empresa, na seção 'Minha Conta', e fazendo login com seu CPF e senha."
    },
    {
        "pergunta": "Meu internet está lenta, o que fazer?",
        "resposta": "Recomendamos reiniciar o roteador. Se o problema persistir, entre em contato conosco pelo telefone 0800 123 456."
    },
    {
        "pergunta": "Quais são os planos de internet disponíveis?",
        "resposta": "Temos planos de 100 Mbps, 300 Mbps e 1 Gbps. Para mais detalhes, visite nosso site ou ligue para 0800 123 456."
    },
    {
        "pergunta": "Como alterar meu plano de internet?",
        "resposta": "Você pode alterar seu plano entrando no site da empresa, na seção 'Minha Conta', ou entrando em contato com nosso suporte pelo telefone 0800 123 456."
    },
    {
        "pergunta": "Esqueci minha senha, como recuperar?",
        "resposta": "Você pode recuperar sua senha clicando em 'Esqueci minha senha' na página de login do site. Um e-mail será enviado com instruções."
    },
    {
        "pergunta": "Como configurar meu roteador?",
        "resposta": "Acesse o manual de configuração do roteador no site da empresa ou entre em contato com nosso suporte técnico pelo telefone 0800 123 456."
    },
    {
        "pergunta": "Qual o valor do plano de 300 Mbps?",
        "resposta": "O plano de 300 Mbps custa R$ 129,90 por mês. Para mais informações, visite nosso site."
    },
    {
        "pergunta": "Como entrar em contato com o suporte técnico?",
        "resposta": "Você pode entrar em contato com nosso suporte técnico pelo telefone 0800 123 456 ou pelo chat online no site da empresa."
    },
    {
        "pergunta": "Meu sinal de Wi-Fi está fraco, o que fazer?",
        "resposta": "Tente reposicionar o roteador em um local mais central da casa. Se o problema persistir, entre em contato conosco pelo telefone 0800 123 456."
    },
    {
        "pergunta": "Como cancelar meu plano?",
        "resposta": "Para cancelar seu plano, entre em contato com nosso atendimento pelo telefone 0800 123 456 ou envie um e-mail para cancelamento@empresa.com."
    }
]


def save_dataset(dataset, dataset_name="default_dataset.json"):
    with open(dataset_name, "w", encoding="utf-8") as f:
        json.dump(dataset, f, ensure_ascii=False, indent=4)
    print(f"Dataset saved to {dataset_name}")


save_dataset(dataset, "dataset-atendimento.json")
