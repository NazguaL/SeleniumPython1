import re


def test_phones_on_home_page(app):
    first_contact_from_home_page = app.contact.get_contact_list()[0]
    first_contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert first_contact_from_home_page.homephone == clear(first_contact_from_edit_page.homephone)
    assert first_contact_from_home_page.mobilephone == clear(first_contact_from_edit_page.mobilephone)
    assert first_contact_from_home_page.workphone == clear(first_contact_from_edit_page.workphone)
    assert first_contact_from_home_page.secondaryphone == clear(first_contact_from_edit_page.secondaryphone)


def test_phones_on_view_page(app):
    first_contact_from_view_page = app.contact.get_contact_from_view_page(0)
    first_contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert first_contact_from_view_page.homephone == first_contact_from_edit_page.homephone
    assert first_contact_from_view_page.mobilephone == first_contact_from_edit_page.mobilephone
    assert first_contact_from_view_page.workphone == first_contact_from_edit_page.workphone
    assert first_contact_from_view_page.secondaryphone == first_contact_from_edit_page.secondaryphone


def clear(s):
    return re.sub("[() -]", "", s)