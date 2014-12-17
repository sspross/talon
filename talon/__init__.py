from talon.quotations import register_xpath_extensions


def init():
    register_xpath_extensions()
    try:
        import PyML
    except:
        pass
    else:
        from talon import signature
        signature.initialize()
