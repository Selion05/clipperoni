import subprocess
import clickeroni.config as config


def dmenu(choices=[], **kwargs) -> str:
    args = config.dmenu_args
    for a, v in kwargs.items():
        a = "-" + a
        if len(a) > 2:
            a = "-" + a

        args.append(a)
        args.append(v)
    p = subprocess.Popen(args, stdin=subprocess.PIPE, stdout=subprocess.PIPE)

    for choice in choices:

        line = choice + "\n"
        p.stdin.write(line.encode())
    p.stdin.close()
    p.wait()

    return p.stdout.read().decode().strip("\n")


def select(choices: []) -> str:
    selected = dmenu(choices)
    if selected not in choices:
        raise ValueError(f'Choice "{selected}" not in choices.')
    return selected
