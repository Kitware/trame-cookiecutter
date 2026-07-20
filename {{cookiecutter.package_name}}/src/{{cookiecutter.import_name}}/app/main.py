from .core import MyTrameApp


def main(server=None, **kwargs):
    app = MyTrameApp(server)
    app.server.start(**kwargs)


if __name__ == "__main__":
    main()
