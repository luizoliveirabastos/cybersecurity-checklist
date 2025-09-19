# checklist_cyber.py - checklist interativo com textos variados

checklist = {
    "Modelos OSI e TCP/IP": [
        "Conhecer as 7 camadas do modelo OSI",
        "Relacionar o modelo TCP/IP com o OSI"
    ],
    "Protocolos de Rede": [
        "Identificar funções do IP (v4 e v6)",
        "Comparar TCP e UDP e seus usos",
        "Explorar o protocolo ICMP e testes como ping",
        "Analisar vulnerabilidades em HTTP/HTTPS",
        "Examinar ataques DNS como Spoofing e Cache Poisoning",
        "Investigar ataques ARP, como spoofing e envenenamento de cache",
        "Avaliar vulnerabilidades do DHCP"
    ],
    "Endereçamento e Sub-redes": [
        "Mapear endereços IPv4 e IPv6",
        "Aplicar máscaras de sub-rede e segmentação",
        "Calcular sub-redes usando CIDR"
    ],
    "Switches, Roteadores e Firewalls": [
        "Compreender funcionamento de switches, roteadores e firewalls",
        "Configurar e analisar VLANs para segmentação",
        "Inspecionar configurações de firewalls em busca de falhas"
    ]
}

# Inicializa todos os itens como não concluídos
status = {categoria: [False]*len(itens) for categoria, itens in checklist.items()}

while True:
    print("\n--- Checklist de Cibersegurança ---")
    for categoria, itens in checklist.items():
        print(f"\n{categoria}:")
        for i, item in enumerate(itens):
            marcado = "[x]" if status[categoria][i] else "[ ]"
            print(f"{i+1}. {marcado} {item}")

    print("\nDigite 'sair' para encerrar.")
    categoria_input = input("Escolha a categoria: ").strip()
    if categoria_input.lower() == "sair":
        break

    if categoria_input not in checklist:
        print("Categoria inválida! Digite exatamente como mostrado.")
        continue

    try:
        item_num = int(input("Digite o número do item para marcar/desmarcar: ")) - 1
        if 0 <= item_num < len(checklist[categoria_input]):
            status[categoria_input][item_num] = not status[categoria_input][item_num]
        else:
            print("Número do item inválido!")
    except ValueError:
        print("Digite um número válido!")
