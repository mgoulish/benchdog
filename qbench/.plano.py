from plano import *

@command
def test(app):
    client_dir = get_real_path("client")

    with working_dir("server"):
        with start("plano run"):
            with working_dir(client_dir):
                run("plano run --duration 1")