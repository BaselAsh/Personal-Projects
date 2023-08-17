"""
This Is The Beginning Of OOP For Me
"""

class Hello:
    """Returns User's Name In Different Ways"""
    user = 0

    @classmethod
    def users_count(cls):
        """Returns Users Count"""
        return f"We Have {cls.user} In The Program"
    
    def __init__(self, first_name, middle_name,  last_name):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        Hello.user += 1

    def __str__(self):
        return "This is where the magic happens :)"
    
    def __len__(self):
        return len(self.first_name) + len(self.middle_name) + len(self.last_name)

    def full_name(self):
        """Returns The Full Name"""
        return f"{self.first_name} {self.middle_name} {self.last_name}"
    
    def formal_name(self):
        """Returns The Formal Name"""
        return f"{self.first_name} {self.middle_name}"
    
    @staticmethod
    def hi_user(name):
        """Returns Hi"""
        return f"hi {name}"
    



def main():
    """This's The Main Function :*)"""
    print(Hello.hi_user("Basel")) # -> From the "hi_user" static method
    print(Hello("Basel", "Ashraf", "Hassan").full_name()) # -> From the "full_name" instance method
    print(Hello("Viga", "Boyka", "Gorge").full_name()) # -> From the "full_name" instance method
    print(Hello.users_count()) # -> From the "user_count" class method
    print(Hello("Omar", "Abdo", "Saleh").full_name()) # -> From the "full_name" instance method
    print(Hello("Peter", "Griffin", "Hogwart's").full_name()) # -> From the "full_name" instance method
    print(Hello.users_count()) # From the "user_count" class method
    print(Hello("Viga", "Boyka", "Gorge")) # -> From the __str__ magic method
    print(len(Hello("Basel", "Ashraf", "Hassan")))


if __name__ == "__main__":
    main()
