*** Settings ***
Library  rf.AddressBook
Library  Collections
Suite Setup  Init Fixtures
Suite Teardown  Destroy Fixtures

*** Test Cases ***
Add new group
    ${old_group_list}=  Get Group List
    ${group}=  New Group  name1  header1  footer1
    Create Group  ${group}
    ${new_group_list}=  Get Group List
    Append To List  ${old_group_list}  ${group}
    Group Lists Should Be Equal  ${old_group_list}  ${new_group_list}

Delete group
     ${old_group_list}=  Get Group List
     ${len}=  Get Length  ${old_group_list}
     ${index}=  Evaluate  random.randrange(${len})  random
     ${group}=  Get From List  ${old_group_list}  ${index}
     Delete Group  ${group}
     ${new_group_list}=  Get Group List
     Remove Values From List  ${old_group_list}  ${group}
     Group Lists Should Be Equal  ${old_group_list}  ${new_group_list}