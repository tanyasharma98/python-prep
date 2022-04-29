import argparse
import sys
#
#
# def calcu(args):
#     if args.o == "add":
#         return args.x + args.y
#     elif args.o == "sub":
#         return args.x - args.y
#     elif args.o == "mul":
#         return args.x * args.y
#     elif args.o == "div":
#         return args.x / args.y
#     else:
#         return "Wrong input"
#
#
# if __name__ == '__main__':
#     parser = argparse.ArgumentParser()
#     parser.add_argument('--x', type=float, default=1.0, help="Call your Tarun sir ")
#
#     parser.add_argument('--y', type=float, default=3.0, help="Call your Tarun sir ")
#
#     parser.add_argument('--o', type=str, default="add", help="Call your Tarun sir ")
#
#     args = parser.parse_args()
#
#     sys.stdout.write(str(calcu(args)))
"""Faulty calculator using python utility"""


def faulty_cal(args):
    if args.o == 'add':
        if args.x == 12 and args.y == 44:
            return f"{args.x} + {args.y} = {58}"
        else:
            return f"{args.x} + {args.y} = {args.x + args.y}"
    elif args.o == 'sub':
        if args.x == 453 and args.y == 120:
            return f"{args.x} - {args.y} = {303}"
        else:
            return f"{args.x} - {args.y} = {args.x - args.y}"
    elif args.o == 'mul':
        if args.x == 45 and args.y == 3:
            return f"{args.x} * {args.y} = {255}"
        else:
            return f"{args.x} * {args.y} = {args.x * args.y}"
    elif args.o == 'div':
        if args.x == 36 and args.y == 6:
            return f"{args.x} / {args.y} = {4}"
        else:
            return f"{args.x} / {args.y} = {args.x / args.y}"


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--x', type=float, default=1.0, help='Give your input')
    parser.add_argument('--y', type=float, default=1.0, help='Give your input')
    parser.add_argument('--o', type=str, default='add', help='What you want to do')

    args = parser.parse_args()

    sys.stdout.write(str(faulty_cal(args)))
