# Output err
def output (*args):
    stack = traceback.extract_stack(limit=2)
    argnames = (stack[0][3]).replace('output(', '').replace(')', '')
    args_dict = {}
    i = 0
    for argname in argnames.replace(' ','').split(','):
        key = argname
        value = args[i]
        args_dict[key] = value
        i += 1
    for name,val in args_dict.items():
        print("%s = %s" % (name, val), file=sys.stderr)
        
def out (arg):
    print(arg, file=sys.stderr)
