
def is_owner(ctx):
    return ctx.message.author.id == 595561546470653995

def is_RPG_channel(ctx):
    from lib import get_config
    return ctx.channel.id in get_config()["RPG_channel"]
