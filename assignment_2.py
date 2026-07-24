def report_format(function):
    def wrapper(self):
        print("=" * 40)
        print("Report Start")
        print("=" * 40)
        function(self)
        print("=" * 40)
        print("Report End")
        print("=" * 40)
    return wrapper


class Report:
    def __init__(self, title, section):
        self.title = title
        self.section = section

    @classmethod
    def sample_report(cls):
        return cls("Student Performance Report", "Computer Science")

    def __str__(self):
        return f"Title : {self.title}"

    def __len__(self):
        return len(self.section)

    @report_format
    def generate_report(self):
        print("Title   :", self.title)
        print("Section :", self.section)
        print("Student :", "Sarthak")
        print("Math    :", 85)
        print("Science :", 90)
        print("English :", 88)

        average = (85 + 90 + 88) / 3
        print("Average :", average)

        if average >= 50:
            print("Result  : Pass")
        else:
            print("Result  : Fail")


r = Report.sample_report()

print(r)
print("Length of Section:", len(r))
r.generate_report()
