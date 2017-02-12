import pytest
from his.forms import HiForm
from thehichannel.factories import UserFactory


@pytest.mark.django_db
def test_hi_form():
    user = UserFactory.create()
    data = {
        "message": "hi",
        "sender": user.id
    }
    form = HiForm(data)
    assert form.is_valid()
