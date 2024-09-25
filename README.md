class Bio:
    def __init__(self):
        self.name="Kirat"
        self.education="Guru Nanak Dev Engineering College, Ludhiana"
        self.Skills={
            "Programming":["Python","C++","C","Jquery","Javascript","NodeJS"],
            "FrameWorks":["Bootstrap","Tailwind-CSS"],
            "Microsoft-Office":["PPT","Excel","Access","OneNote","Word"],
            }
        self.Experience=[
            "Event Management at FMCRS 90.8 MHZ",
            "Event Management at NSS"
        ]
        self.Email="Kiratanand36@gmail.com/Kiratanand68@gmail.com"
        self.linkedin = "[LinkedIn](https://www.linkedin.com/in/yourusername)"
        self.email = "your.email@example.com"

    def __str__(self):
        return (f"{self.name} - {self.education}," "\n"
                f"Passionate in technologies and fluent in {self.Skills}")

my_bio = Bio()


print(my_bio)
