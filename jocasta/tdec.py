import re
from telethon import events
from jocasta.services.tele import tbot


def register(**args):
    pattern = args.get("pattern")
    r_pattern = r"^[/.!?]"

    if pattern is not None and not pattern.startswith("(?i)"):
        args["pattern"] = "(?i)" + pattern

    args["pattern"] = pattern.replace("^/", r_pattern, 1)

    if pattern is not None:
        try:
            cmd = re.search(reg, pattern)
            try:
                cmd = cmd.group(1).replace("$", "").replace("\\", "").replace("^", "")
            except BaseException:
                pass
        except BaseException:
            pass
        tbot.add_event_handler(wrapper, events.NewMessage(**args))
    return wrapper


def chataction(**args):
    """Registers chat actions."""
    def decorator(func):
        tbot.add_event_handler(func, events.ChatAction(**args))
        return func
    return decorator


def userupdate(**args):
    """Registers user updates."""
    def decorator(func):
        tbot.add_event_handler(func, events.UserUpdate(**args))
        return func

    return decorator


def inlinequery(**args):
    """Registers inline query."""
    pattern = args.get("pattern", None)

    if pattern is not None and not pattern.startswith("(?i)"):
        args["pattern"] = "(?i)" + pattern

    def decorator(func):
        tbot.add_event_handler(func, events.InlineQuery(**args))
        return func

    return decorator


def callbackquery(**args):
    """Registers inline query."""

    def decorator(func):
        tbot.add_event_handler(func, events.CallbackQuery(**args))
        return func

    return decorator