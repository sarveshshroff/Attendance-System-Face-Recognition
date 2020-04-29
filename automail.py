import yagmail
import os



filename = "Attendance"+os.sep+"Attendance_2020-03-31_17-02-27.csv"  # attach the file
body = "Attendence File"  # email body
receiver = input("Enter email to send the attendance to: ")

# mail information
yag = yagmail.SMTP(user="############", password="#####")

# sent the mail
yag.send(
    to=receiver,
    subject="Attendance Report",  # email subject
    contents=body,  # email body
    attachments=filename,  # file attached
)
