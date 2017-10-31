from hello_jenkins import hello

def test_hello_run():
    assert 'hello' in hello.run()