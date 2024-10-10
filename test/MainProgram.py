class MainProgram:
    def __init__(self,val):
        self.val = val
        self.var=[]
    def __call__(self,*args,**kwargs):
        try:
            result = self.val(*args,**kwargs)
        except Exception as e:
            self.var.append((args,kwargs,e))
            raise e
        else:
            self.var.append((args,kwargs,result))
            return result
    @classmethod
    def SubProgram(cls,f):
        return cls(f)
    @MainProgram.SubProgram
    def func(x,y):
        return x/y
    print(func(y=6,x=0))