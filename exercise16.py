import programmersworld as pw
import pkgutil
import inspect
__author__ = 'kristof'

# print(pw.__dict__)

def printInfo():
    for importer, modname, ispkg in pkgutil.iter_modules(pw.__path__):
        print("Found submodule %s (is a package: %s)" % (modname, ispkg))
        print(dir(modname))
        mod = __import__(modname)
        print(mod.__dict__)
        # print(inspect(modname))

def printKeys():
    import types

    for key, obj in pw.__dict__:
        if type(obj) is types.ModuleType:
            print(key)

print(printInfo())
print(printKeys())
print(locals())