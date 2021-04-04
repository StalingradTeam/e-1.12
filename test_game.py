import mock
import game

LATIN_LIST = [chr(x) for x in range(ord("a"), ord("z")+1)]

def get_exclusions(word):
    return [ch for ch in LATIN_LIST if ch not in word]


def test_init():
    fake_value = 'chto-gde-kogda'
    def fake_run(self):
        game.Game.fake_attr = fake_value

    with mock.patch.object(game, "__name__", "__main__"):
        with mock.patch.object(game.Game, 'run', fake_run):
            game.init()
            assert game.Game.fake_attr == fake_value
        

def test_win_super():
    g = game.Game()
    input_list = list(g.word)
    with mock.patch('builtins.input', lambda _: input_list.pop(0)):
        g.run()
        assert not [ch for ch in g.tried_symbols if ch not in g.word]
        assert g.is_win == True
        assert g.failures == 0


def test_win_super_empty_repeat():
    g = game.Game()
    input_list = [""] + list(g.word[0] + g.word[0] + g.word[1:])
    with mock.patch('builtins.input', lambda _: input_list.pop(0)):
        g.run()
        assert not [ch for ch in g.tried_symbols if ch not in g.word]
        assert g.is_win == True
        assert g.failures == 0


def test_win_one_false():
    g = game.Game()
    input_list = [get_exclusions(g.word)[0]] + list(g.word)
    with mock.patch('builtins.input', lambda _: input_list.pop(0)):
        g.run()
        assert len([ch for ch in g.tried_symbols if ch not in g.word]) == 1
        assert g.is_win == True
        assert g.failures == 1


def test_lose():
    g = game.Game()
    input_list = get_exclusions(g.word)
    with mock.patch('builtins.input', lambda _: input_list.pop(0)):
        g.run()
        assert len([ch for ch in g.tried_symbols if ch not in g.word]) == game.MAX_FAILURES
        assert g.is_win == False
        assert g.failures == game.MAX_FAILURES
