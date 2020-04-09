from faker import Factory as FakerFactory

faker = FakerFactory.create()
methods = [method for method in dir(faker) if callable(getattr(faker, method)) and not method.startswith("_")]
for item in methods:
    try:
        print "- %s:" % item
        print "  %s" % getattr(faker, item)()
    except TypeError:
        pass