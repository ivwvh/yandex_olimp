class Robot:
    def __init__(self) -> None:
        self.x = 0
        self.y = 0


def get_value(command: str) -> int:
    value = command.split('(')[1][:-1]

    if not value:
        return 1
    return int(value)

def get_loop_iterations(command: str) -> int:
    value = command.split()[3]
    return int(value[-3:-2])


def get_direction(command: str) -> str:
    direction=command[command.index('_') + 1 : command.index('(')]
    return direction

bot = Robot()
commands = []
loop_iterations = 0

while True:
    command = input()
    if command.startswith('#'):
        break
    if command:
        commands.append(command)
        

for command in commands:
    if command.startswith('f'):
        loop_iterations = get_loop_iterations(command)
        continue

    if command.startswith(' '):
        direction = get_direction(command)
        value = get_value(command)
        if direction == 'down':
            bot.y += -value * loop_iterations
        if direction == 'up':
            bot.y += value * loop_iterations
        if direction == 'left':
            bot.x += -value * loop_iterations
        if direction == 'right':
            bot.x += value * loop_iterations
    
    else:
        value = get_value(command)
        direction = get_direction(command)
        if direction == 'down':
            bot.y += -value
        if direction == 'up':
            bot.y += value
        if direction == 'left':
            bot.x += -value
        if direction == 'right':
            bot.x += value
    pass

new_commands = []
if bot.x < 0:
    mod_cords = abs(bot.x)
    if mod_cords == 1:
        new_commands.append('move_left()')
    else:
        new_commands.append(f'move_left({mod_cords})')
if bot.x > 0:
    mod_cords = abs(bot.x)
    if mod_cords == 1:
        new_commands.append('move_right()')
    else:
        new_commands.append(f'move_right({mod_cords})')
if bot.y < 0:
    mod_cords = abs(bot.y)
    if mod_cords == 1:
        new_commands.append('move_down()')
    else:
        new_commands.append(f'move_down({mod_cords})')
if bot.y > 0:
    mod_cords = abs(bot.y)
    if mod_cords == 1:
        new_commands.append('move_up()')
    else:
        new_commands.append(f'move_up({mod_cords})')

if not len(commands) == len(new_commands):
    for i in new_commands:
        print(i)
else:
    print('')