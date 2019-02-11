def retro_transform(ctx, cmdline, transform):
    action = ctx.copy_last_action()

    num_words = int(cmdline)

    last_words = "".join(ctx.last_words(count = num_words))
    action.prev_replace = last_words
    action.text = transform(last_words)
    action.word = None
    action.prev_attach = True

    return action

def retro_replace_space_(ctx, cmdline):
    action = ctx.copy_last_action()

    args = cmdline.split(":")
    num_words = int(args[0]) + 1
    space_char = args[1]

    last_words = "".join(ctx.last_fragments(count = num_words))
    action.prev_replace = last_words
    action.text = last_words.replace(" ", space_char)
    action.word = None
    action.prev_attach = True

    return action


def retro_capitalise(*args, **kwargs):
    return retro_transform(*args, **kwargs, transform = lambda x: x.capitalize())


def retro_title(*args, **kwargs):
    return retro_transform(*args, **kwargs, transform = lambda x: x.title())


def retro_upper(*args, **kwargs):
    return retro_transform(*args, **kwargs, transform = lambda x: x.upper())


def retro_lower(*args, **kwargs):
    return retro_transform(*args, **kwargs, transform = lambda x: x.lower())


def retro_replace_space(*args, **kwargs):
    return retro_replace_space_(*args, **kwargs)
