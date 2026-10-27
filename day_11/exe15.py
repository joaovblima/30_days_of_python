def show_args(**args):
   for k, v in args.items():
      print(k, "->", v, end=", ") 
    
show_args(nome="joao", idade=30, time="sao paulo")
