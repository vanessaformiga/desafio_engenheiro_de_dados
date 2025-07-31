Contexto da solução com base no arquivo do ERP.json fornecido referente ao uma comando cuja valor é referente a um item do menu.

1. **Descreva o esquema JSON correspondente ao exemplo acima.**
    
    O arquivo ERP.json representa uma comanda de uma rede de restaurante extraída de um ERP, com informações detalhadas sobre um pedido realizado.
    
    Na comanda podem ser valores referentes a unidade da rede de restaurantes, valores referentes ao pedido realizado com quantidade, valor e datas e também são exibidos valores referentes as taxas que serão pagas e valor final do pedido
    
    A comanda pode conter dados sobre o pedido realizado pelo cliente. No exemplo abaixo pode ser citados os itens que posem ser encontrados na comanda.
    
    A unidade da rede de restaurante (localRef)
    
    Informações do pedido (guestCheck)
    
    Itens consumido (detailLines)
    
    Itens do menu (menuItem)
    
    Taxas aplicadas(taxes)
    
    ### Esquema geral do JSON:
    
    ```json
    
    {
      "curUTC": "string (datetime)",
      "locRef": "string",
      "guestChecks": [
        {
          "guestCheckId": number,
          "chkNum": number,
          "opnBusDt": "string (date)",
          "opnUTC": "string (datetime)",
          "opnLcl": "string (datetime)",
          "clsdBusDt": "string (date)",
          "clsdUTC": "string (datetime)",
          "clsdLcl": "string (datetime)",
          "lastTransUTC": "string (datetime)",
          "lastTransLcl": "string (datetime)",
          "lastUpdatedUTC": "string (datetime)",
          "lastUpdatedLcl": "string (datetime)",
          "clsdFlag": boolean,
          "gstCnt": number,
          "subTtl": number,
          "nonTxblSlsTtl": number|null,
          "chkTtl": number,
          "dscTtl": number,
          "payTtl": number,
          "balDueTtl": number|null,
          "rvcNum": number,
          "otNum": number,
          "ocNum": number|null,
          "tblNum": number,
          "tblName": "string",
          "empNum": number,
          "numSrvcRd": number,
          "numChkPrntd": number,
    
          "taxes": [
            {
              "taxNum": number,
              "txblSlsTtl": number,
              "taxCollTtl": number,
              "taxRate": number,
              "type": number
            }
          ],
    
          "detailLines": [
            {
              "guestCheckLineItemId": number,
              "rvcNum": number,
              "dtlOtNum": number,
              "dtlOcNum": number|null,
              "lineNum": number,
              "dtlId": number,
              "detailUTC": "string (datetime)",
              "detailLcl": "string (datetime)",
              "lastUpdateUTC": "string (datetime)",
              "lastUpdateLcl": "string (datetime)",
              "busDt": "string (date)",
              "wsNum": number,
              "dspTtl": number,
              "dspQty": number,
              "aggTtl": number,
              "aggQty": number,
              "chkEmpId": number,
              "chkEmpNum": number,
              "svcRndNum": number,
              "seatNum": number,
    
              "menuItem": {
                "miNum": number,
                "modFlag": boolean,
                "inclTax": number,
                "activeTaxes": "string",
                "prcLvl": number
              }
            }
          ]
        }
      ]
    }
    
    ```
    

**Exemplo do json detalhado**

```
 {
  "curUTC": "2025-07-30T17:00:00Z",           // Data e hora atual (UTC)
  "locRef": "loja_01",                         // Referência da loja ou unidade
  "guestChecks": [
    {
      "guestCheckId": 123456,                  // ID único da comanda
      "chkNum": 7890,                          // Número da comanda (interno)
      "opnBusDt": "2025-07-30",                // Data de abertura (negócio)
      "opnUTC": "2025-07-30T16:30:00Z",        // Abertura UTC
      "opnLcl": "2025-07-30T13:30:00-03:00",   // Abertura local
      "clsdBusDt": "2025-07-30",               // Data de fechamento
      "clsdUTC": "2025-07-30T17:00:00Z",       // Fechamento UTC
      "clsdLcl": "2025-07-30T14:00:00-03:00",  // Fechamento local
      "lastTransUTC": "2025-07-30T16:50:00Z",  // Última transação
      "lastTransLcl": "2025-07-30T13:50:00-03:00",
      "lastUpdatedUTC": "2025-07-30T17:00:00Z",// Última atualização UTC
      "lastUpdatedLcl": "2025-07-30T14:00:00-03:00",
      "clsdFlag": true,                        // Comanda fechada?
      "gstCnt": 2,                             // Número de clientes
      "subTtl": 120.00,                        // Subtotal
      "nonTxblSlsTtl": null,                   // Vendas não tributáveis
      "chkTtl": 132.00,                        // Total da comanda
      "dscTtl": 10.00,                         // Total de descontos
      "payTtl": 132.00,                        // Total pago
      "balDueTtl": 0.00,                       // Saldo devedor
      "rvcNum": 1,                             // Número da RVC (área da loja)
      "otNum": 101,                            // Número do operador
      "ocNum": null,                           // Outro código interno
      "tblNum": 5,                             // Número da mesa
      "tblName": "Mesa 5",                     // Nome da mesa
      "empNum": 321,                           // Funcionário responsável
      "numSrvcRd": 1,                          // Rodadas de serviço
      "numChkPrntd": 2,                        // Quantidade de impressões da comanda

      "taxes": [                               // Lista de impostos aplicados
        {
          "taxNum": 1,                         // Número identificador do imposto
          "txblSlsTtl": 120.00,                // Valor tributável
          "taxCollTtl": 12.00,                 // Valor do imposto coletado
          "taxRate": 0.10,                     // Alíquota (10%)
          "type": 1                             // Tipo de imposto
        }
      ],

      "detailLines": [                         // Lista de itens consumidos
        {
          "guestCheckLineItemId": 1,           // ID do item na comanda
          "rvcNum": 1,                         // Número da RVC
          "dtlOtNum": 101,                     // Número do operador
          "dtlOcNum": null,                    // Outro código de controle
          "lineNum": 1,                        // Número da linha do pedido
          "dtlId": 999,                        // ID interno do detalhe
          "detailUTC": "2025-07-30T16:32:00Z", // Data/hora do lançamento (UTC)
          "detailLcl": "2025-07-30T13:32:00-03:00",
          "lastUpdateUTC": "2025-07-30T16:32:00Z",
          "lastUpdateLcl": "2025-07-30T13:32:00-03:00",
          "busDt": "2025-07-30",               // Data do negócio
          "wsNum": 10,                         // Estação de trabalho
          "dspTtl": 60.00,                     // Valor exibido do item
          "dspQty": 1,                         // Quantidade exibida
          "aggTtl": 60.00,                     // Valor total agregado
          "aggQty": 1,                         // Quantidade agregada
          "chkEmpId": 55,                      // ID do funcionário
          "chkEmpNum": 321,                    // Número do funcionário
          "svcRndNum": 1,                      // Número da rodada
          "seatNum": 1,                        // Número do assento

          "menuItem": {                        // Informações do item de menu
            "miNum": 1001,                     // Código do item
            "modFlag": false,                  // Possui modificação?
            "inclTax": 60.00,                  // Valor com imposto incluído
            "activeTaxes": "TX1",              // Impostos aplicáveis
            "prcLvl": 1                        // Nível de preço
          }
        }
      ]
    }
  ]
}

```

### Esquema do JSON:

A estrutura JSON pode ser descrita hierarquicamente da seguinte forma:

```json
{
  "guestCheck": {
    "guestCheckId": 123,
    "chkNum": 456,
    "opnBusDt": "2023-01-01",
    "...": "...",
    "detailLines": [
      {
        "guestCheckLineItemId": 1,
        "lineNum": 1,
        "menuItem": {
          "miNum": 101,
          "modFlag": false,
          "inclTax": 1.50,
          "...": "..."
        }
      }
    ],
    "taxes": [
      {
        "taxNum": 1,
        "txblSlsTtl": 20.00,
        "taxCollTtl": 2.00
      }
    ]
  }
}

```

**Identificação do JSON Mapeados**

- guestCheckId	string	Identificador único da comanda/pedido
- storeId	string	Identificador da loja
- employeeId	string	Funcionário que registrou o pedido
- detailLines	array	Itens do pedido (linhas de detalhe)
- detailLines[].guestCheckLineItemId	string	ID do item na comanda
- detailLines[].menuItem	object	Detalhes do item de menu
- menuItem.menuItemId	string	ID do item de menu
- menuItem.name	string	Nome do item de menu
- menuItem.price	float	Preço unitário do item
- detailLines[].quantity	integer	Quantidade pedida
- detailLines[].total	float	Total (quantidade x preço)
- taxes	array	Impostos aplicados
- taxes[].taxId	string	ID do imposto
- taxes[].name	string	Nome do imposto
- taxes[].amount	float	Valor do imposto
- totalAmount	float	Valor total da comanda
- timestamp	datetime	Data/hora do pedido

**Identificação das entidades mapeadas**

- guestCheck - pedido realizado
- detailLine - item do pedido
- menuItem - item do menu
- taxes - valores referentes as taxas aplicadas

