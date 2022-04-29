import argparse
import sys

# def calc(args):
#     if args.o == 'add':
#         return  args.x + args.y
#     elif args.o == 'sub':
#         return  args.x - args.y
#     elif args.o == 'mul':
#         return  args.x * args.y
#     elif args.o == 'div':
#         return  args.x / args.y
#     else:
#         return "Something Went wrong"
#
# if __name__ == '__main__':
#     parser = argparse.ArgumentParser()
#
#     parser.add_argument('--x', type=float,default=1.0,
#                         help="Enter Argument One, for help COntact yourself ,Do Not Disturb")
#     parser.add_argument('--y', type=float, default=6.0,
#                         help="Enter Argument Two, for help COntact yourself ,Do Not Disturb")
#     parser.add_argument('--o', type=str, default="add",
#                         help="For help COntact yourself ,Do Not Disturb")
#
#     args = parser.parse_args()
#     sys.stdout.write(str(calc(args)))




#==========Faulty Calculator=========Task========================

def fault_cal(args):
    if args.o == "add":
        if args.x == 12 and args.y == 44:
            return "12+ 44 = 58"
        else:
            return args.x, "+", args.y, "=", args.x + args.y
    elif args.o == "sub":
        if args.x == 453 and args.y == 120:
            return "453-120 = 303 "
        else:
            return args.x, "-", args.y, "=", args.x - args.y
    elif args.o == "mul":
        if args.x == 42 and args.y == 14:
            return "42*14 = 4 "
        else:
            return args.x ,"*", args.y, "=", args.x * args.y
    elif args.o =="div":
        if args.x == 100 and args.y == 50:
            return "100/50 = 30 "
        else:
            return args.x ,"/", args.y, "=", args.x / args.y
    else:
        return "Something went wrong"
if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('--x',type=float , default=0.0,
                        help="First Input, Faulty")
    parser.add_argument('--y',type=float,default=2.0,
                        help="Second Input, Dumb")
    parser.add_argument('--o', type=str , default="sub",
                        help="AYa gaya Swadd")
    print("Use: add/mul/sub/div")
    args = parser.parse_args()
    sys.stdout.write(str(fault_cal(args)))