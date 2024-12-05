class Human:
    def __init__(self,name):
        self.name = name
        self.head=self.Head()
    def info(self):
        print(f"Name: {self.name}")
        self.head.talk()
        self.head.Brain.think()
    class Head:
        def __init__(self):
            self.brain=self.Brain()
        def talk(self):
            print("Hello, I am a human")
        class Brain:
            def __init__(self):
                print("brain creation")
            def think(self):
                print("thinking")
human =Human("varshi")
human.info()