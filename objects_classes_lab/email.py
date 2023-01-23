class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"

    def send(self):
        self.is_sent = True


input_line = input()
emails = []

while not input_line == "Stop":
    s, r, c = input_line.split()
    current_email = Email(s, r, c)
    emails.append(current_email)
    input_line = input()

correct_indexes = [int(x) for x in input().split(", ")]

for index in correct_indexes:
    current_email = emails[index]
    current_email.send()

for email in emails:
    print(email.get_info())
