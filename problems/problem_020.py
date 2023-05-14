# Complete the has_quorum function to test to see if the number
# of the people in the attendees list is greater than or equal
# to 50% of the number of people in the members list.


def has_quorum(attendees_list, members_list):
  #define has_quorum
  #len of each list
  #if len of attendees list is 50% of len of members list
  #if num in attendees_list >= .5 
    pass


def has_quorum(attendees_list, members_list):
    # num_attendees = the number of attendees
    num_attendees = len(attendees_list)  # solution
    # num_members = the number of members
    num_members = len(members_list)  # solution
    # If the num_attendees divided by the num_members is
    # greater than 0.5
    if num_attendees / num_members >= 0.5:  # solution
        # return True
        return True  # solution
    # Otherwise
    else:  # solution
        # return False
        return False  # solution
    # pass                                              # problem