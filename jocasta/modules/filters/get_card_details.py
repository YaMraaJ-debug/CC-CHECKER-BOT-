import re

from jocasta.services.language import get_strings
from jocasta.utlis.logger import log


async def get_cards(message: str, user_id: int):
    try:
        strings = await get_strings(user_id, "card_check_error")
        assert len(message) > 28, strings['card_not_found']
        res = re.findall(r"[0-9]+", message)
        assert len(res) > 3, strings['card_not_found']
        assert len(res[0]) in {15, 16}, strings['invalid_card_length']
        if len(res) == 3:
            mes = res[1][:2]
            ano = res[1][2:]
            ano1 = res[1][2:]
            cvv = res[2]
        else:
            mes = res[1]
            ano = res[2]
            ano1 = res[2]
            cvv = res[3]
        cc = res[0]
        if len(mes) > 2:
            ano = cvv
            cvv = mes
            mes = ano1
        if int(cc[0]) in {1, 2, 7, 8, 9, 0}:
            return strings['invalid_card']
        elif len(mes) not in [1, 2] or (len(mes) == 2 and mes > '12') or (len(mes) == 2 and mes < '01') or (len(mes) == 1 and mes < '1'):
            return strings['invalid_month']
        elif len(ano) not in [2,4] or (len(ano)  == 2 and ano < '22') or (len(ano) ==  2 and ano > '29') or (len(ano) ==  4 and ano < '2022') or (len(ano) == 4 and ano > '2029'):
            return strings['invalid_year']
        elif int(cc[0]) == 3 and len(cvv) != 4 or len(cvv) < 3 or len(cvv) > 4:
            return strings['invalid_cvv']
        else:
            if len(mes) == 1:
                mes = f'0{str(mes)}'
            if len(ano) == 2:
                ano = f'20{str(ano)}'
            return cc, mes, ano, cvv
    except AssertionError as aserr:
        return aserr
    except Exception as e:
        return strings['invalid_card']
