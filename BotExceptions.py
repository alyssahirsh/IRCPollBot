"""
Custom Exception Classes for vote bot errors.
"""


class BadVoteOption(Exception):
    """No such vote option for a given poll"""
    pass


class BadPollIDValue(Exception):
    """PollID is malformed or already in use"""
    pass

class PollIDTaken(BadPollIDValue):
    """PollID already in use"""
    pass

class PollIDTooLong(BadPollIDValue):
    """Attempt to set PollID value longer than allowed"""
    pass

class HostAlreadyVoted(Exception):
    """host-user tried to vote in a poll they already voted in"""
    pass
