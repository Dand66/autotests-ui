import pytest
from _pytest.fixtures import SubRequest


@pytest.mark.parametrize('number', [1, 2, 3, -1])
def test_number(number: int):
    assert number > 0


@pytest.mark.parametrize('number, expected', [(1, 1), (2, 4), (3, 9)])
def test_several_numbers(number: int, expected: int):
    assert number ** 2 == expected


@pytest.mark.parametrize('os', ['macos', 'windows', 'linux', 'debian'])
@pytest.mark.parametrize('browser', ['firefox', 'chrome', 'webkit'])
def test_multiplication_of_numbers(os: str, browser: str):
    assert len(os + browser) > 0


@pytest.fixture(params=['firefox', 'chrome', 'webkit'])
def browser(request: SubRequest):
    return request.param


def test_open_browser(browser: str):
    print(f'Running test test on browser: {browser}')


@pytest.mark.parametrize('user', ['Alice', 'Zara'])
class TestOperations:
    @pytest.mark.parametrize('account', ['Credit card', 'Debit card'])
    def test_user_with_operations(self, user: str, account: str):
        print(f'User with operations: {user} and {account}')

    def test_user_without_operations(self, user: str):
        print(f'User without operations: {user}')


users = {
    '+7900000000': 'User with money',
    '+7988888888': 'User without money',
    '+7444444444': 'User with operations'
}

@pytest.mark.parametrize('Phone_number', users.keys(),
                         ids=lambda Phone_number: f'{Phone_number}: {users[Phone_number]}')
def test_identifiers(Phone_number: str):
    ...
