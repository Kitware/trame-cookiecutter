from .core import create_engine

def main(server=None, **kwargs):
    engine = create_engine(server)
    engine.server.start(**kwargs)

if __name__ == "__main__":
    main()
