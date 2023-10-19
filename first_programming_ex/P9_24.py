
## Defines a Message class with class variables to log all messages
#  @classvar _no_messages will increase for every line that is added to any message. The name is
#      therefore a bit missleading. To keep track of number of messages it would have to be updated
#      in the constructor of every message
#  @classvar _log will log every message in a dictionary
#  
class Message:
    _no_messages = 0
    _log = {}

    ## Constructs an empty message with a sender and a receiver
    #  @param sender the name of the message sender
    #  @param recipient the name of the message sender
    #
    def __init__(self, sender, recipient):
        self.sender = sender
        self.recipient = recipient
        self._messageBody = ""
    
    ## Append a new line of text to the message body together with a newline character
    #  @param line the line of text
    def append(self, line):
        self._messageBody = self._messageBody + line + "\n"
        self._log_messages()
    
    ## Convert message into one long line of text
    #
    def toString(self):
        fromStr = f"From: {self.sender}\n"
        toStr = f"To: {self.recipient}\n"

        # repr() converts a string into its raw equivalent, in this case one line of text.
        return repr(fromStr + toStr + self._messageBody)
    
    ## Log the messages sent and increase the number of lines added to any message. 
    #
    def _log_messages(self):
        Message._no_messages += 1
        # Check if sender exist in the dictionary
        if self.sender in Message._log:
            # Create the recipient for the sender if it does not exist or just update the message body if it exist
            Message._log[self.sender][self.recipient] = self._messageBody
        
        # If sender does not exist, create sender with recipient and message body, and update number of messages
        else:
            Message._log[self.sender] = {self.recipient: self._messageBody}


## Test program, only executed if this file is executed directly
#
if __name__ == "__main__":
    message1 = Message("Bob", "Alice")
    message1.append("This is the first line of text from Bob to Alice")
    message1.append("A second line of text from Bob to Alice")
    print("Should return the entire message in one line:")
    print(message1.toString())
    message2 = Message("Peter", "Bob")
    message2.append("This is the first line of text from Peter to Bob")
    print()
    print("We have created two messages with a total of three lines of text.")
    print(f"_no_messages: {Message._no_messages}")
    print("Expected: 3")
    print(f"_log: {Message._log}")
    print(r"Expected: {'Bob': {'Alice': 'This is the first line of text from Bob to Alice\nA second line of text from Bob to Alice\n'}, 'Peter': {'Bob': 'This is the first line of text from Peter to Bob\n'}}")
    
