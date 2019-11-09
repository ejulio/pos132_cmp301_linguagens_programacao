from argparse import ArgumentParser


ap = ArgumentParser()

ap.add_argument(
    '--a',
    type=int,
    required=True,
    help='Valor que será usado na soma'
)

ap.add_argument(
    '--b',
    type=int,
    required=True,
    help='Valor que será usado na soma'
)

ap.add_argument(
    '--operacao',
    '-o',
    type=str,
    required=False,
    default='adicao',
    choices=[
        'adicao', 'subtracao',
        'multiplicacao', 'divisao'
    ],
    help='Operação que deve ser realizada'
)

args = ap.parse_args()

operacoes = {
    'adicao': lambda a, b: a + b,
    'subtracao': lambda a, b: a - b,
    'multiplicacao': lambda a, b: a * b,
    'divisao': lambda a, b: a / b,
}

fn = operacoes[args.operacao]
print(fn(args.a, args.b))


