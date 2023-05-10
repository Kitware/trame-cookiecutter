from .core import create_engine

def main(server=None, **kwargs):
    create_engine(server)
    server.start(**kwargs)

if __name__ == "__main__":
    main()
