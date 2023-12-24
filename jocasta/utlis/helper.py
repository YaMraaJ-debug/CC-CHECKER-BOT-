
import json
from jocasta.services.language import get_strings, get_strings_dec
from jocasta.services.red import aioredis
from jocasta.utlis.logger import log
from jocasta.dec import register
from jocasta.services.addtodb import user_info_dec
from jocasta import bot
from jocasta.utlis.send_log import send_logs
from jocasta.services.gate_on_off import get_status
import time
from datetime import datetime




async def get_gate_info(gate_name):
    x = await aioredis.get(f'gate_{gate_name.lower()}')
    return json.loads(x) if x else False