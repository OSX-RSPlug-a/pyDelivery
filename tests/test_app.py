
def test_app(app):
    assert app.name == 'delivery.app'


def test_config(config):
    assert config["DEBUG"] is False


def test_req_ret_404(client):
    assert client.get("/url_que_n_exist").status_code == 404


# def test_live_req()