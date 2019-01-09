hairP = '   _~_'
eyes = '  (o o)'
beak = ' /  V  \\'
potbelly = '/(  _  )\\'
feet = '  ^^ ^^ '

n = int(input())
if n < 1000:
    penguins = (hairP + '    ') * n + '\n' + (eyes + '   ') * n + '\n' + (beak + '  ') * n + '\n' + (
                potbelly + ' ') * n + '\n' + (feet + '  ') * n + '\n'
print(penguins)
