# WAP to find out whether the student has passed or failed if it requires a total of 40% and at least 33%
# in each subject to pass. Assume 3 subjects and take marks as input from the user.

marks_sub1 = int(input("Enter marks of subject 1:"))
marks_sub2 = int(input("Enter marks of subject 2:"))
marks_sub3 = int(input("Enter marks of subject 3:"))

total_percent = ((marks_sub1 + marks_sub2 + marks_sub3) * 100)/300

if(total_percent>=40 and marks_sub1>=33 and marks_sub2>=33 and marks_sub3>=33):
    print("You passed the exam")

else:
    print("You failed the exam")

